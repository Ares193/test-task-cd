from typing import List

from fastapi import HTTPException, status
from pydantic import ValidationError
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from collections import defaultdict

from app.services.database.session import db_service
from app.resources.Metric.db_model import MetricDBModel
from app.schemas.metrics import MetricInDB, MetricsStatisticList, MetricInput, MetricsList, MetricsStatistic


class MetricResource:
    @classmethod
    def create(cls, data: MetricInput) -> MetricInDB:
        try:
            db_model = MetricDBModel(**data.model_dump())
            db_service.add(db_model)
            db_service.commit()
            db_service.refresh(db_model)
            return MetricInDB.model_validate(db_model)
        except ValidationError as e:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f'{str(e)}')
        except SQLAlchemyError:
            db_service.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Ошибка записи в БД')

    @classmethod
    def list_metrics_by_service(cls, service_name: str) -> MetricsStatisticList:
        try:
            list_metrics = db_service.query(MetricDBModel.path,
                                            func.max(MetricDBModel.response_time_ms).label('max'),
                                            func.min(MetricDBModel.response_time_ms).label('min'),
                                            func.avg(MetricDBModel.response_time_ms).label('average'),
                                            func.percentile_cont(0.99).within_group(
                                                MetricDBModel.response_time_ms)).group_by(
                MetricDBModel.path).filter(MetricDBModel.service_name == service_name).all()
            result_list = [
                MetricsStatistic(
                    path=stat[0],
                    max=stat[1],
                    min=stat[2],
                    average=stat[3],
                    p99=stat[4]) for stat in list_metrics
            ]
            return MetricsStatisticList(result_list)
        except SQLAlchemyError:
            db_service.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Ошибка чтения из БД')

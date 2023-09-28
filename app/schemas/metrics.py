from typing import List, Optional

from pydantic import BaseModel, RootModel, ConfigDict, Field

from app.utils.schema_mixins import BaseInDBMixin, ListModelsMixin


class BaseMetric(BaseModel):
    service_name: str = Field(description='Имя сервиса')
    path: str = Field(description='Путь запроса, например /users/me')
    response_time_ms: int = Field(description='Время ответа сервиса в миллисекундах')


class MetricInput(BaseMetric):
    pass


class MetricInDB(BaseInDBMixin, BaseMetric):
    pass


class MetricsStatistic(BaseModel):
    path: str = Field(description='Путь запроса, например /users/me')
    average: float = Field(description='Среднее время ответа в миллисекундах')
    min: int = Field(description='Минимальное время ответа в миллисекундах')
    max: int = Field(description='Максимальное время ответа в миллисекундах')
    p99: Optional[float] = Field(description='99 персентиль времени ответа (Опционально)')


class MetricsList(ListModelsMixin):
    model_config = ConfigDict(from_attributes=True)
    root: List[MetricInDB]


class MetricsStatisticList(ListModelsMixin):
    model_config = ConfigDict(from_attributes=True)
    root: List[MetricsStatistic]

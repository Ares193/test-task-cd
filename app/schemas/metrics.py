from typing import List, Optional

from pydantic import BaseModel, RootModel, ConfigDict, Field, NonNegativeInt, NonNegativeFloat

from app.utils.schema_mixins import BaseInDBMixin, ListModelsMixin


class BaseMetric(BaseModel):
    service_name: str = Field(description='Имя сервиса')
    path: str = Field(description='Путь запроса, например /users/me')
    response_time_ms: NonNegativeInt = Field(description='Время ответа сервиса в миллисекундах')


class MetricInput(BaseMetric):
    pass


class MetricInDB(BaseInDBMixin, BaseMetric):
    pass


class MetricsStatistic(BaseModel):
    path: str = Field(description='Путь запроса, например /users/me')
    average: NonNegativeFloat = Field(description='Среднее время ответа в миллисекундах')
    min: NonNegativeInt = Field(description='Минимальное время ответа в миллисекундах')
    max: NonNegativeInt = Field(description='Максимальное время ответа в миллисекундах')
    p99: Optional[NonNegativeFloat] = Field(description='99 персентиль времени ответа (Опционально)')


class MetricsList(ListModelsMixin):
    model_config = ConfigDict(from_attributes=True)
    root: List[MetricInDB]


class MetricsStatisticList(ListModelsMixin):
    model_config = ConfigDict(from_attributes=True)
    root: List[MetricsStatistic]

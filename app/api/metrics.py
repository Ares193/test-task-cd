from fastapi import APIRouter, status

from app.resources.Metric.main import MetricResource
from app.schemas.metrics import MetricInDB, MetricInput, MetricsStatisticList

router = APIRouter(
    prefix='/metrics',
    tags=["Metrics"]
)


@router.post("/", response_model=MetricInDB, status_code=status.HTTP_201_CREATED)
def create_metric(data: MetricInput) -> MetricInDB:
    return MetricResource.create(data=data)


@router.get("/{service_name}", response_model=MetricsStatisticList, status_code=status.HTTP_200_OK)
def list_metric_stat_by_service(service_name: str) -> MetricsStatisticList:
    return MetricResource.list_metrics_by_service(service_name=service_name)



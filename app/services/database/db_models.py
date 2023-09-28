# Import all the models, so that Base has them before being
# imported by Alembic
from app.services.database.base import Base  # noqa
from app.resources.Metric.db_model import MetricDBModel  # noqa
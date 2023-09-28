"""fill test data

Revision ID: 398ee35afbad
Revises: 6f935b70fa4e
Create Date: 2023-09-28 17:25:44.676161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '398ee35afbad'
down_revision = '6f935b70fa4e'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        INSERT INTO metrics (service_name, path, response_time_ms) VALUES 
        ('API', '/metrics', '144'),
        ('API', '/metrics', '45'),
        ('API', '/metrics', '65'),
        ('API', '/metrics', '111'),
        ('API', '/metrics', '78'),
        ('API', '/user', '56'),
        ('API', '/user', '73'),
        ('API', '/user', '302'),
        ('API', '/user', '230'),
        ('API', '/user', '53'),
        ('API', '/company', '120'),
        ('API', '/company', '122'),
        ('API', '/company', '132'),
        ('API', '/company', '145'),
        ('WEB', '/partners', '57'),
        ('WEB', '/partners', '78'),
        ('WEB', '/partners', '86'),
        ('WEB', '/partners', '145'),
        ('WEB', '/price', '203'),
        ('WEB', '/price', '98'),
        ('WEB', '/price', '66'),
        ('WEB', '/price', '170')
    """)


def downgrade():
    pass

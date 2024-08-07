"""client table delete created

Revision ID: cad8e891d761
Revises: 
Create Date: 2024-07-27 17:11:23.882653

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cad8e891d761'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('registered_date', sa.TIMESTAMP(), nullable=True),
    sa.Column('is_seller', sa.Boolean(), nullable=True),
    sa.Column('is_client', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('gigs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('gigs_title', sa.String(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('seller',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('cv_url', sa.Text(), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('active_gigs', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('certificate',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('pdf_url', sa.Text(), nullable=True),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('experience',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('company_name', sa.String(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('job_title', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gigs_category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('category_name', sa.String(), nullable=False),
    sa.Column('gigs_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gigs_id'], ['gigs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gigs_file',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('file_url', sa.Text(), nullable=True),
    sa.Column('gigs_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gigs_id'], ['gigs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gigs_skill',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('skill_name', sa.String(), nullable=False),
    sa.Column('gigs_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gigs_id'], ['gigs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('language',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('lan_name', sa.String(), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('occupation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('occup_name', sa.String(), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('saved_client',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('saved_seller',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('seller_projects',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('delivery_days', sa.Integer(), nullable=True),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('skills',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('skill_name', sa.String(), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project_files',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('file_url', sa.Text(), nullable=True),
    sa.Column('seller_project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seller_project_id'], ['seller_projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects_skills',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('skill_name', sa.String(), nullable=False),
    sa.Column('seller_project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seller_project_id'], ['seller_projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projects_skills')
    op.drop_table('project_files')
    op.drop_table('skills')
    op.drop_table('seller_projects')
    op.drop_table('saved_seller')
    op.drop_table('saved_client')
    op.drop_table('occupation')
    op.drop_table('language')
    op.drop_table('gigs_skill')
    op.drop_table('gigs_file')
    op.drop_table('gigs_category')
    op.drop_table('experience')
    op.drop_table('certificate')
    op.drop_table('seller')
    op.drop_table('gigs')
    op.drop_table('user')
    # ### end Alembic commands ###

"""Add composite index for chat message session lookups.

Revision ID: 20260315_chat_messages_agent_conv_idx
Revises: 20260313_column_modify
"""

from alembic import op

revision = "20260315_chat_messages_agent_conv_idx"
down_revision = "20260313_column_modify"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_chat_messages_agent_conversation_id "
        "ON chat_messages (agent_id, conversation_id)"
    )


def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS ix_chat_messages_agent_conversation_id")

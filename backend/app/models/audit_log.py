from typing import TYPE_CHECKING, Any, Dict, Optional
from uuid import UUID

from sqlalchemy import JSON, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.user import User


class AuditLog(Base):
    """Audit log model tracking all user actions and security events in the AMLIP system."""

    __tablename__ = "audit_logs"

    action: Mapped[str] = mapped_column(
        String(100), index=True, nullable=False
    )
    entity_type: Mapped[str] = mapped_column(
        String(100), index=True, nullable=False
    )
    entity_id: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True
    )

    user_id: Mapped[Optional[UUID]] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )

    details: Mapped[Dict[str, Any]] = mapped_column(
        JSON, default=dict, nullable=False
    )
    ip_address: Mapped[Optional[str]] = mapped_column(
        String(45), nullable=True
    )

    user: Mapped[Optional["User"]] = relationship(
        "User",
        back_populates="audit_logs",
    )

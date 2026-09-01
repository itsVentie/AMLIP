import enum
from typing import TYPE_CHECKING, Any, Dict, Optional
from uuid import UUID

from sqlalchemy import JSON, Enum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.user import User


class CaseStatus(str, enum.Enum):
    NEW = "NEW"
    IN_PROGRESS = "IN_PROGRESS"
    ESCALATED = "ESCALATED"
    CLOSED_FALSE_POSITIVE = "CLOSED_FALSE_POSITIVE"
    CLOSED_SAR_FILED = "CLOSED_SAR_FILED"


class CasePriority(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    URGENT = "URGENT"


class InvestigationCase(Base):
    """Investigation case model representing a case of suspicious activity in the AMLIP system."""

    __tablename__ = "investigation_cases"

    case_number: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    status: Mapped[CaseStatus] = mapped_column(
        Enum(CaseStatus, native_enum=False),
        default=CaseStatus.NEW,
        index=True,
        nullable=False,
    )
    priority: Mapped[CasePriority] = mapped_column(
        Enum(CasePriority, native_enum=False),
        default=CasePriority.MEDIUM,
        nullable=False,
    )

    subject_id: Mapped[str] = mapped_column(
        String(255), index=True, nullable=False
    )

    assignee_id: Mapped[Optional[UUID]] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )

    metadata_info: Mapped[Dict[str, Any]] = mapped_column(
        JSON, default=dict, nullable=False
    )

    assignee: Mapped[Optional["User"]] = relationship(
        "User",
        back_populates="assigned_cases",
    )

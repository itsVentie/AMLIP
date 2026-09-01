import enum
from typing import TYPE_CHECKING, List

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.audit_log import AuditLog
    from app.models.investigation import InvestigationCase


class UserRole(str, enum.Enum):
    ADMIN = "ADMIN"
    ANALYST = "ANALYST"
    COMPLIANCE_OFFICER = "COMPLIANCE_OFFICER"
    AUDITOR = "AUDITOR"


class User(Base):
    """User model representing a user or compliance officer in the AMLIP system."""

    __tablename__ = "users"

    email: Mapped[str] = mapped_column(
        String(255), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, native_enum=False),
        default=UserRole.ANALYST,
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)

    # Relationships
    assigned_cases: Mapped[List["InvestigationCase"]] = relationship(
        "InvestigationCase",
        back_populates="assignee",
    )
    audit_logs: Mapped[List["AuditLog"]] = relationship(
        "AuditLog",
        back_populates="user",
    )

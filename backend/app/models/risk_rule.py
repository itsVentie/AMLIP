import enum
from typing import Any, Dict, Optional

from sqlalchemy import JSON, Boolean, Enum, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class RuleSeverity(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class RiskRule(Base):
    """AML rule model representing a rule and its severity in the AMLIP system."""

    __tablename__ = "risk_rules"

    code: Mapped[str] = mapped_column(
        String(100), unique=True, index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    severity: Mapped[RuleSeverity] = mapped_column(
        Enum(RuleSeverity, native_enum=False),
        default=RuleSeverity.MEDIUM,
        nullable=False,
    )
    risk_score_impact: Mapped[float] = mapped_column(
        Float, default=10.0, nullable=False
    )
    is_enabled: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )

    parameters: Mapped[Dict[str, Any]] = mapped_column(
        JSON, default=dict, nullable=False
    )
    version: Mapped[int] = mapped_column(Integer, default=1, nullable=False)

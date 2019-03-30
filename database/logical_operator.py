"""operator module"""
from enum import Enum


class LogicalOperator(Enum):
    """Operator enum class"""
    AND = 'AND'
    OR = 'OR'
    AND_NOT = 'AND NOT'
    OR_NOT = 'OR NOT'

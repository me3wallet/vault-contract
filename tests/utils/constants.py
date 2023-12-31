from enum import IntFlag
from utils.helpers import to_bytes32

DAY = 86400
WEEK = 7 * DAY
YEAR = 31_556_952  # same value used in vault
MAX_INT = 2**256 - 1
ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"
MAX_BPS = 10_000


class ROLES(IntFlag):
    ADD_STRATEGY_MANAGER = 1
    REVOKE_STRATEGY_MANAGER = 2
    FORCE_REVOKE_MANAGER = 4
    ACCOUNTANT_MANAGER = 8
    QUEUE_MANAGER = 16
    REPORTING_MANAGER = 32
    DEBT_MANAGER = 64
    MAX_DEBT_MANAGER = 128
    DEPOSIT_LIMIT_MANAGER = 256
    WITHDRAW_LIMIT_MANAGER = 512
    MINIMUM_IDLE_MANAGER = 1024
    PROFIT_UNLOCK_MANAGER = 2048
    DEBT_PURCHASER = 4096
    EMERGENCY_MANAGER = 8192
    ALL = 16383


class StrategyChangeType(IntFlag):
    ADDED = 1
    REVOKED = 2


class RoleStatusChange(IntFlag):
    OPENED = 1
    CLOSED = 2


class ChangeType(IntFlag):
    ADDED = 1
    REMOVED = 2


class AddressIds:
    ROUTER = to_bytes32("ROUTER")
    RELEASE_REGISTRY = to_bytes32("RELEASE REGISTRY")
    REGISTRY_FACTORY = to_bytes32("REGISTRY FACTORY")
    COMMON_REPORT_TRIGGER = to_bytes32("COMMON REPORT TRIGGER")
    BASE_FEE_PROVIDER = to_bytes32("BASE FEE PROVIDER")
    APR_ORACLE = to_bytes32("APR ORACLE")

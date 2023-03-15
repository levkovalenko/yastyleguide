from collections.abc import Generator
from typing import Any

ERROR = tuple[int, int, str, Any]
ERROR_GENERATOR = Generator[ERROR, None, None]

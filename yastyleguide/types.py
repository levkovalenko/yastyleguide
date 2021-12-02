from typing import Any, Generator, Tuple

ERROR = Tuple[int, int, str, Any]
ERROR_GENERATOR = Generator[ERROR, None, None]

from .models.comm import Comm
from .utils.comm import comm_config

try:
    from importlib.metadata import version
    __version__ = version("databricks-engtoolkits")
except Exception:
    __version__ = "0.0.0"

__all__ = ["Comm", "comm_config", "__version__"]

<<<<<<< HEAD
=======
# logger/__init__.py
>>>>>>> fec7536a17c28757f785d798e7fed0291bccea99
from .custom_logger import CustomLogger
# Create a single shared logger instance
GLOBAL_LOGGER = CustomLogger().get_logger("doc_portal")
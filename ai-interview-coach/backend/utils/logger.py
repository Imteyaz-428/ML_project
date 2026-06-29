import logging
import os

# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("AIInterviewCoach")
logger.setLevel(logging.INFO)

# Prevent duplicate logs
logger.handlers.clear()

# Terminal output
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# File output
file_handler = logging.FileHandler(
    "logs/app.log",
    encoding="utf-8"
)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
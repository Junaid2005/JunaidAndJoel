import logging

logger = logging.getLogger("logger")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s: %(message)s",
)

logger.info("Logger initialised")

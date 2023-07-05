import coloredlogs
import logging


logger = logging.getLogger(__name__)

coloredlogs.install(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)",
    datefmt='%Y-%m-%d %H:%M:%S',
    isatty=True
)

logger.info('Logger has been initialized.')

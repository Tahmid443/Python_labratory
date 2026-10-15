import logging

# Basic config
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")

# Exception logging
try:
    1 / 0
except ZeroDivisionError:
    logger.exception("Something failed")

# Multiple loggers
a = logging.getLogger("app.a")
b = logging.getLogger("app.b")
a.setLevel(logging.WARNING)
b.setLevel(logging.DEBUG)
a.debug("not shown")
b.debug("shown")

# Handlers
import sys
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s: %(message)s")
handler.setFormatter(formatter)

custom = logging.getLogger("custom")
custom.addHandler(handler)
custom.info("Custom handler")

# File handler
import os
fh = logging.FileHandler("app.log")
fh.setLevel(logging.WARNING)
custom.addHandler(fh)
custom.warning("Logged to file")
custom.removeHandler(fh)
fh.close()

if os.path.exists("app.log"):
    print(open("app.log").read())
    os.remove("app.log")

# Logging best practices
# - One logger per module using __name__
# - Use appropriate levels
# - Don't use root logger directly
# - Use lazy formatting
logger.info("User %s logged in from %s", "alice", "NYC")
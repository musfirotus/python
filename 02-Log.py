import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('app.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

class Log:
    def info(self):
        logger.info("This is an information about something.")

    def error(self):
        logger.error("We can't divide any numbers by zero.")

    # def notice(self):
    #     logger.notice("This is an information about something.")

    def warning(self):
        logger.warning("Insufficient funds.")

    def debug(self):
        logger.debug("This is debug message.")

    # def alert(self):
    #     logger.alert("This is an information about something.")

    def critical(self):
        logger.critical("Medic!! We've got critical damages.")

    def emergency(self):
        logger.emergency("This is an information about something.")

log = Log()
log.info()
log.error()
# log.notice()
log.warning()
log.debug()
# log.alert()
log.critical()
log.emergency()
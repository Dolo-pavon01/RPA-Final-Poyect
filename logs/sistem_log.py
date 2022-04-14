
import logging


FORMAT = '%(asctime)s-%(levelname)s : %(message)s'
FILENAME = 'SystemTest.log'

DEBUG_LEVEL= 'debug.log'
INFO_LEVEL = 'info.log'
WARNING_LEVEL = 'warning.log'
ERROR_LEVEL = 'error.log'
CRITICAL_LEVEL = 'critical.log'

DEBUG_INDEX= 0
INFO_INDEX = 1
WARNING_INDEX = 2
ERROR_INDEX = 3
CRITICAL_INDEX =4

LEVEL_LIST = [(DEBUG_LEVEL, logging.DEBUG),
                     (INFO_LEVEL, logging.INFO),
                     (WARNING_LEVEL, logging.WARNING),
                     (ERROR_LEVEL, logging.ERROR),
                     (CRITICAL_LEVEL, logging.CRITICAL)]

class LevelFilter(logging.Filter):

    def __init__(self, levelFilter):
        self.levelFilter = levelFilter

    def filter(self, record):
        return record.levelno == self.levelFilter


class MySystemLogs():

    def __init__(self,name):

        
        self.__logger = logging.getLogger(name)
        self.__filename = FILENAME
        self.__format = logging.Formatter(FORMAT)
        self.__levels= set()
        
        self.__logger.setLevel(logging.DEBUG)

        mainHandler = logging.FileHandler(self.__filename)
        mainHandler.setLevel(logging.DEBUG)
        mainHandler.setFormatter(self.__format)

        self.__logger.addHandler(mainHandler)

    

    def __addLevelHandlers(self, level):

        # Create the different handlers of each logging level,
        #  and adds them to the main logger.

        levelName, levelNumber = level
        handlerLevel = self.__LevelHandlerCreate(levelName, levelNumber)
        self.__logger.addHandler(handlerLevel)
        self.__levels.add(levelName)

    def __LevelHandlerCreate(self, levelName, levelNumber):

        # This function should receive a levelName and the int level of logging,
        # and create a handler and a filter to receive only logs of that level.

        
        handlerLevel = logging.FileHandler(levelName)
        handlerLevel.setLevel(levelNumber)
        handlerLevel.setFormatter(self.__format)
        handlerLevel.addFilter(LevelFilter(levelNumber))

        return handlerLevel

    def LogDebug(self, message):
        if(DEBUG_LEVEL not in self.__levels):
            self.__addLevelHandlers(LEVEL_LIST[DEBUG_INDEX])
        self.__logger.debug(message)

    def LogInfo(self, message):
        if(INFO_LEVEL not in self.__levels):
            self.__addLevelHandlers(LEVEL_LIST[INFO_INDEX])
        self.__logger.info(message)

    def LogWarning(self, message):
        if(WARNING_LEVEL not in self.__levels):
            self.__addLevelHandlers(LEVEL_LIST[WARNING_INDEX])
        self.__logger.warning(message)

    def LogError(self, message,exception = False):
        if(ERROR_LEVEL not in self.__levels):
            self.__addLevelHandlers(LEVEL_LIST[ERROR_INDEX])
        self.__logger.error(message,exc_info= exception)

    def LogCritical(self, message):
        if(CRITICAL_LEVEL not in self.__levels):
            self.__addLevelHandlers(LEVEL_LIST[CRITICAL_INDEX])
        self.__logger.critical(message)


import logging

class Logging:
    
   def simple_logging(lvl,msg):
        logger = logging.getLogger('logging')

        #Default level is warning
        logging.basicConfig(level = logging.DEBUG, filename = 'errorLog.log')

        if lvl == 'debug':
            logger.debug('DEBUG:  ' + msg)
        elif lvl == 'info':
            logger.info('INFORMATION:  ' + msg)
        elif lvl == 'warning':
            logger.warning('WARNING:  ' + msg)
        elif lvl == 'error':
            logger.error('ERROR:  ' + msg)
        else:
            logger.critical('CRITICAL:  ' + msg)



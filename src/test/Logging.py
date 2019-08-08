import logging


    
def main():
    simple_logging()

    def simple_logging(lvl,msg):
        logger = logging.getLogger('logging')

        #Default level is warning
        logging.basicConfig(level = logging.DEBUG, filename = '/error/errorLog.log')

        if lvl == 'debug':
            logger.debug('This is a debug message.  ' + msg)
        elif lvl == 'info':
            logger.info('Info is good for people.  ' + msg)
        elif lvl == 'warning':
            logger.warning('Rhut-ro! Something\'s happening.  ' + msg)
        elif lvl == 'error':
            logger.error('Hey, that hurts!  ' + msg)
        else:
            logger.critical('My mama is gonna get you!  ' + msg)


if __name__ == '__main__':
            main()

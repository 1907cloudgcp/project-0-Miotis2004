import logging

class Bank:

                
    def loadCust():
        try:
            cust = {}
            with open('customerFile.txt', 'r') as f:
                for line in f:
                    custList = line.split(',')
                    custList[2] = custList[2][:-1]
                    cust.update({custList[0]:{'pswd':custList[1], 'bal':custList[2]}})
        except:
            logger = logging.getLogger('logging')
            msg = 'Could not open customer file.  Quitting application.'
            print(msg)
            logging.basicConfig(level = logging.DEBUG, filename = 'errorLog.log')
            logger.error('Hey, that hurts!  ' + msg)
            exit()
            
            
        print('Customers loaded.')
        return cust

    def loadHist():
        hist = {}
        lastEntry = ''
        with open('historyFile.txt', 'r') as f:
        
            for line in f:
            
                hList = line.split(',')
            
                hList[2] = hList[2][:-1]
                hist.update({hList[0]:{'name':hList[1], 'change':hList[2]}})
            
                lastEntry = hList[0]

        loadedData = [hist, lastEntry]
        return loadedData

    def simpleLogging(lvl,msg):
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
    
    def __init__(self):
        print('Bank created.')

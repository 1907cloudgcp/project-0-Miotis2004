import logging

class Bank:

    #try loading customer file with correct file name
    def loadCustGood():
        print('Test 1 - Part 2:  Try to load customers with a file.  Log errors.')
        
        try:
            
            cust = {}
            with open('customerFile.txt', 'r') as f:
                for line in f:
                    custList = line.split(',')
                    custList[2] = custList[2][:-1]
                    cust.update({custList[0]:{'pswd':custList[1], 'bal':custList[2]}})
            
            print('Customers loaded.')
            print('\n\n')
            return cust
    
        except:
            logger = logging.getLogger('logging')
            msg = 'Could not open customer file. File not found.'
            print(msg)
            logging.basicConfig(level = logging.DEBUG, filename = 'errorLog.log')
            logger.error('Hey, that hurts!  ' + msg)
            exit()
        

    #try loading customer file with incorrect file name            
    def loadCust():
        print('Test 1 - Part 1:  Try to load customers without a file.  Log errors.')
        
        try:
            
            cust = {}
            with open('customerFileBad.txt', 'r') as f:
                for line in f:
                    custList = line.split(',')
                    custList[2] = custList[2][:-1]
                    cust.update({custList[0]:{'pswd':custList[1], 'bal':custList[2]}})

            print('\n\n')
            return cust
        except:
            logger = logging.getLogger('logging')
            msg = 'Could not open bad customer file.  Quitting application.'
            print(msg)
            logging.basicConfig(level = logging.DEBUG, filename = 'errorLog.log')
            logger.error('Hey, that hurts!  ' + msg)
            
            
            
        

    
            
            
        

    def loadHist():
        try:
            hist = {}
            lastEntry = ''
            with open('historyFile.txt', 'r') as f:
            
                for line in f:
                
                    hList = line.split(',')
                
                    hList[2] = hList[2][:-1]
                    hist.update({hList[0]:{'name':hList[1], 'change':hList[2]}})
                
                    lastEntry = hList[0]

        except:
            logger = logging.getLogger('logging')
            msg = 'Could not open history file.  Quitting application.'
            print(msg)
            logging.basicConfig(level = logging.DEBUG, filename = 'errorLog.log')
            logger.error('Hey, that hurts!  ' + msg)
            exit()

        loadedData = [hist, lastEntry]
        return loadedData

    
    
    def __init__(self):
        print('Bank created.')

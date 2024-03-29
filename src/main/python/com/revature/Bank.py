from Logging import *

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
            
            msg = 'Could not open customer file.'
            print(msg)
            Logging.simple_logging('error',msg)
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

    
    
    def __init__(self):
        print('Bank created.')

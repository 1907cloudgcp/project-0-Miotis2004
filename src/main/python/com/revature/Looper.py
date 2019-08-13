from Logging import *

class Looper:
    def loggedLoop(cust,hist,lastEntry,name):
        #Logged in loop
        isLogged = True
        
        while isLogged == True:
            balance = cust[name]['bal']
            command = input('"v" = View balance  "w" = Withdraw  "d" = Deposit "h" = History  "q" = Quit ')

            if command == 'v':
                print('Current balance: ' + balance)
            elif command == 'w':
                amount = input('Current balance: ' + balance + '  How much to withdraw?  (Whole dollars only): ')
                if int(amount) > int(balance):
                    msg = name + ':  Insufficient funds.'
                    print(msg)
                    Logging.simple_logging('info',msg)
                else:
                    intBal = int(balance) - int(amount)
                    balance = str(intBal)
                    cust.update({name:{'pswd':pswd,'bal':balance}})
                    newEntry = int(lastEntry)
                    newEntry += 1
                    lastEntry = str(newEntry)
                    hist.update({newEntry:{'name':name, 'change':'-'+amount}})
                    #hist.update({newEntry:{name:{'change':'-'+amount,'bal':balance}}})
                    print('Remaining balance: ' + balance)
                    #Write new data to file
                    with open('customerFile.txt', 'a') as f:
                        writeStr = name + ',' + pswd + ',' + balance + '\n'
                        f.write(writeStr)
                    with open('historyFile.txt', 'a') as f:
                        writeStr = lastEntry + ',' + name + ',' + '-' + amount + '\n'
                        f.write(writeStr)
                        
            elif command == 'd':
                amount = input('Current balance: ' + balance + '  How much to deposit?  (Whole dollars only): ')
                intBal = int(balance) + int(amount)
                balance = str(intBal)
                cust.update({name:{'pswd':pswd,'bal':balance}})
                newEntry = int(lastEntry) + 1
                lastEntry = str(newEntry)
                hist.update({newEntry:{'name':name, 'change':'+'+amount}})
                    #hist.update({newEntry:{name:{'change':'+'+amount,'bal':balance}}})
                print('New balance: ' + balance)
                    #Write new data to file
                with open('customerFile.txt', 'a') as f:
                    writeStr = name + ',' + pswd + ',' + balance + '\n'
                    f.write(writeStr)
                    
                with open('historyFile.txt', 'a') as f:
                    writeStr = lastEntry + ',' + name + ',' + '+' + amount + '\n'
                    f.write(writeStr)
                        
            elif command == 'q':
                    #Quit
                    
                print('Good-bye!')
                isLogged = False

            elif command == 'h':
                for k,v in hist.items():
                    for i,j in v.items():
                        if j == name:
                            v1 = str(k)
                            v2 = str(v['change'])
                            print('Transaction: ' + v1 + ' Activity: ' + v2)
                        
                    
            else:
                print('That is not acceptable input.')


    def loop(cust,hist,lastEntry):
        isActive = True
        isLogged = False
        
        #Active loop
        while isActive == True:
            logReg = input('Select "s" to sign in or "r" to register.  "q" to quit.  ')
            if logReg == 'r':
                #Register a new account
                print('Register account.')
                name = input('Select a user name: ')
                pswd = input('Select a password: ')
                balc = input('Enter your starting balance: ')

                #Add new customer to dictionary
                cust.update({name:{'pswd':pswd, 'bal':balc}})
                
                #Write new data to file
                with open('customerFile.txt', 'a') as f:
                    writeStr = name + ',' + pswd + ',' + balc + '\n'
                    f.write(writeStr)

                #Set status to logged in
                isLogged = True 
            elif logReg == 's':
                #Sign into account
                print('Sign into account.')
                name = input('User name: ')
                pswd = input('Password: ')

                correctPW = cust[name]['pswd']
                if pswd == correctPW:
                    print('Logged in.')
                    isLogged = True
                else:
                    msg = name + ':  Authentication failure.'
                    print(msg)
                    Logging.simple_logging('info',msg)
                    print('Authentication failure.  Try again.')
                    isLogged = False
            elif logReg == 'q':
                #Quit
                print('Good-bye!')
                isActive = False
            elif logReg == 'a':
                for k,v in cust.items():
                    print(str(k) + ': ' + str(v['pswd']))
                
            else:
                print('That is not acceptable input.')

            if isLogged == True:
                Looper.loggedLoop(cust,hist,lastEntry,name)

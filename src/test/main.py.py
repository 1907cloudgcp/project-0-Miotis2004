from Bank import *
    


def loop(cust,hist,lastEntry):
    isActive = True
    isLogged = False
    tryNumber = 0
    
    #Active loop
    while isActive == True:
        #logReg = input('Select "s" to sign in or "r" to register.  "q" to quit.  ')
        
        
        

        for i in range(0,2):
            print(i)
            logReg = 's'
            if i == 0:
                print('TEST 2 - PART 1: FAIL LOGIN')
            else:
                print('TEST 2 - PART 2: GOOD LOGIN')

            print('Select "s" to sign in or "r" to register.  "q" to quit. s')

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
                #name = input('User name: ')
                #pswd = input('Password: ')
                
                if i == 0:
                    name = 'bob'
                    pswd = 'password'
                elif i == 1:
                    name = 'bob'
                    pswd = 'pass1'

                print('User name: ' + name)
                print('Password: ' + pswd)
                
                
                correctPW = cust[name]['pswd']
                if pswd == correctPW:
                    print('Logged in.')
                    print('\n\n')
                    isLogged = True
                else:
                    print('Authentication failure.  Try again.')
                    print('\n\n')
                    isLogged = False
                    tryNumber += 1
                    if tryNumber == 3:
                        print('3 failed login attempts.  Goodbye!')
                        exit()
                        
            elif logReg == 'q':
                #Quit
                print('Good-bye!')
                isActive = False
                
            else:
                print('That is not acceptable input.')

            #Logged in loop
            while isLogged == True:
                balance = cust[name]['bal']
                command = input('"v" = View balance  "w" = Withdraw  "d" = Deposit "h" = History  "q" = Quit ')

                if command == 'v':
                    print('Current balance: ' + balance)
                elif command == 'w':
                    amount = input('Current balance: ' + balance + '  How much to withdraw?  (Whole dollars only): ')
                    if int(amount) > int(balance):
                        print('You do not have enough money.')
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

            
def main():
    
    cust = Bank.loadCust()
    cust = Bank.loadCustGood()
    
    loadedData = Bank.loadHist()
    hist = loadedData[0]
    lastEntry = loadedData[1]
    
    
    loop(cust,hist,lastEntry)
    
'''
For the brave souls who get this far: You are the chosen ones,
the valiant knights of programming who toil away, without rest,
fixing our most awful code. To you, true saviors, kings of men,
I say this: never gonna give you up, never gonna let you down,
never gonna run around and desert you. Never gonna make you cry,
never gonna say goodbye. Never gonna tell a lie and hurt you.    
'''



if __name__ == '__main__':
        main()
    

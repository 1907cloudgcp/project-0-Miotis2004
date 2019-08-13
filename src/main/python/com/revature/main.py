from Bank import *
from Looper import *
    

            
def main():
       
    cust = Bank.loadCust()
    
    loadedData = Bank.loadHist()
    hist = loadedData[0]
    lastEntry = loadedData[1]
    Looper.loop(cust,hist,lastEntry)

    #loop(cust,hist,lastEntry)
    
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
    

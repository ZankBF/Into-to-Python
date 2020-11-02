#Zank Week 7

print ("Welcome to ticket symbol")
symbol = {'t' :27.33,
          'wmt' :144.71,
          'tsla' : 419.07,
          'lvgo' : 138.45,
          'zm' :  465.50,
           'immu' : 85.25,
           'mrfa' : 70.52,
           'tgt' : 164.92,
          'aapl' : 119.02,
           'shldq' : 0.19,
          }
while(True):
    ticker = input("Please enter stock symbol to see price. (enter goodbye to close)")
    if ticker == 'goodbye':
        break
    if ticker in symbol.keys():
        print ('The current price of ' + ticker + ' is ' + str('{:,}'.format(symbol[ticker])))
    else:
        print ("Symbol not found for" ,ticker, "please try again")
        
print ("Goodbye")

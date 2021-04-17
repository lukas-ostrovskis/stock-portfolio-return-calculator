import yfinance as yf

def returns(input,startDate,endDate):
    info = input.split('\n')
    notFound = []
    
    totalReturn = 0.00
    for i in info:
        # Current ticker
        currentTicker = yf.Ticker(i.split(' ')[0])

        # Some tickers may not be found by the API so check if history exists
        if (len(currentTicker.history(start=startDate,end=endDate)) != 0):
            # Size of the period
            sz = currentTicker.history(start=startDate,end=endDate)['Close'].size

            # Starting price of the ticker
            startingPrice = currentTicker.history(start=startDate,end=endDate)['Close'][0]
            # Final price of the ticker
            finalPrice = currentTicker.history(start=startDate,end=endDate)['Close'][sz-1]
            # Target percentage of the ticker in the porfolio
            targetPercentage = float(i.split(' ')[1][:-1])

            totalReturn += ((finalPrice-startingPrice)/startingPrice) * targetPercentage
        else:
            # The ticker is not found, so add it to the list of such tickers
            notFound.append(i.split(' ')[0])
    return (totalReturn, notFound)

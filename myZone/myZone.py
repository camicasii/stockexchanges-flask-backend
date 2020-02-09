from pytz import  timezone
from datetime import datetime
import datetime as dt

London_StockExchange={
   "open":(dt.time(9, 30, 00),),
    "close":(dt.time(17, 30, 00),)
}
TYO_StockExchange={
   "open":(dt.time(16, 00, 00),dt.time(22, 00, 00)),
    "close":(dt.time(18, 00, 00),dt.time(00, 45, 00))
}
ASX_StockExchange={
   "open":(dt.time(10, 00, 00),),
    "close":(dt.time(19, 30, 00),)
}
NYSE_StockExchange={
   "open":(dt.time(9,30, 00),),
    "close":(dt.time(4, 00, 00),)
}
VenezuelaTimeZone = [timezone('America/Caracas')]
#ASX (Australian Securities Exchange)
ASXTimeZone = (timezone('Australia/Sydney'), ASX_StockExchange)
#TYO (Bolsa de Tokio)
TYOTimeZone = (timezone('Asia/Tokyo'),TYO_StockExchange)
#London Stock Exchange
LondonTimeZone = (timezone('Europe/London'),London_StockExchange)
#New York Stock Exchange (Bolsa de Nueva York)
NYSETimeZone = (timezone('America/New_York'),NYSE_StockExchange)

StockExchanges=[ASXTimeZone,TYOTimeZone,LondonTimeZone,NYSETimeZone]

def isWeekEnd() -> bool:
    #["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    weekEnd_ = datetime.now().weekday()
    if weekEnd_ == 5 or weekEnd_ == 6:
        return True
    else:
        return False

def timeStockExchange(date):
        """if isWeekEnd():
            return [False,"is Weekend"]"""

        [StockExchangeHours,openClose]=date
        timeStock=datetime.now(StockExchangeHours).time()
        for state in  openClose:
            if len(openClose[state])>1:
                break
            [openState] = openClose["open"]
            [closeState] = openClose["close"]
            state_= closeState>timeStock>openState
            return [state_, timeStock]

        [open_, close_] = openClose.items()
        [_,[open_one,open_two]]=open_
        [_, [close_one, close_two]] = close_
        state_=close_one>timeStock>open_one  or close_two>timeStock>open_two
        return  [state_,timeStock]

def stateStockExchange(data):

    for date in data:
        [timeZone_,StockExchange]=date
        print(timeZone_,timeStockExchange(date))
    return



stateStockExchange(StockExchanges)
print()




import ibapi
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
#streaming data
from ibapi.contract import Contract
from ibapi.order import *
import threading
import time

class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
    # Listen to the real time data
    def realtimeBar(self, reqId, time: int, open_: float, high: float, low: float, close: float, volume: int, wap: float, count: int):
        super().realtimeBar(reqId, time, open_, high, low, close, volume, wap, count)
        try:
            bot.on_bar_update(reqId, time, open_, high, low, close, volume, wap, count)
        except Exception as e:
            print("Error", e)
    def error(self, reqId, errorCode: int, errorString: str):
        return super().error(reqId, errorCode, errorString)

class Bot():
    ib = None
    def __init__(self):
        self.ib = IBApi()
        self.ib.connect("127.0.0.1", 0000, 1) # change port to the one you are using
        ib_thread = threading.Thread(target=self.run_loop, daemon=True)
        ib_thread.start()
        time.sleep(1)
        #get instruement
        instrument = "AMZN"
        contract = Contract()
        contract.symbol = instrument
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        #get data
        self.ib.reqRealTimeBars(0, contract, 5, "TRADES", False, [])
        #sumbit order
        #create Order object
        #Buy
        MktBuyOrder = Order()
        MktBuyOrder.orderType = "MKT"
        MktBuyOrder.action = "BUY"
        MktBuyOrder.totalQuantity = 1
        MktBuyOrder.eTradeOnly = False
        MktBuyOrder.firmQuoteOnly = False
        #Sell
        MktSellOrder = Order()
        MktSellOrder.orderType = "MKT"
        MktSellOrder.action = "SELL"
        MktSellOrder.totalQuantity = 1
        MktSellOrder.eTradeOnly = False
        MktSellOrder.firmQuoteOnly = False
        #create Contract object
        contract = Contract()
        contract.symbol = instrument
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.primaryExchange = "ISLAND"
        contract.currency = "USD"
        #Run trading strategy
        self.tradingStrategy
    #run socket in a sperated thread
    def run_loop(self):
        self.ib.run()
    #Pass real time data to the bot
    def on_bar_update(self, reqId, time, open_, high, low, close, volume, wap, count):
        print("Time:", time, "Open:", open, "High:", high, "Low:", low, "Close:", close, "Volume:", volume, "Count:", count, "WAP:", wap)
    def tradingStrategy(self): 
        pass #implement your trading strategy here

#start bot
bot = Bot()
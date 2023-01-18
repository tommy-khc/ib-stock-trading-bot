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

class Bot():
    ib = None
    def __init__(self):
        self.ib = IBApi()
        self.ib.connect("127.0.0.1", 7497, 1)
        ib_thread = threading.Thread(target=self.run_loop, daemon=True)
        ib_thread.start()
        time.sleep(1)
        #get instruement

    #run socket in an new thread
    def run_loop(self):
        self.ib.run()

bot = Bot()
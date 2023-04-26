import asyncio
import websockets
import json
import requests
import hmac
import base64
import zlib
import datetime
import time

from okex import consts


def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"


def get_local_timestamp():
    return int(time.time())


def login_params(timestamp, api_key, passphrase, secret_key):
    message = timestamp + 'GET' + '/users/self/verify'

    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    sign = base64.b64encode(d)

    login_param = {"op": "login", "args": [{"apiKey": api_key,
                                            "passphrase": passphrase,
                                            "timestamp": timestamp,
                                            "sign": sign.decode("utf-8")}]}
    login_str = json.dumps(login_param)
    return login_str


class WSTradeAPI():


    def __init__(self, api_key, passphrase, secret_key):

        self.url = consts.WS_URL
        self.api_key = api_key
        self.passphrase = passphrase
        self.secret_key = secret_key
        self.ws = None

    async def run(self):
        while True:
            try:
                self.ws = await websockets.connect(self.url)
                timestamp = str(get_local_timestamp())
                login_str = login_params(timestamp, self.api_key, self.passphrase, self.secret_key)
                await self.ws.send(login_str)
                last_ping_time=datetime.datetime.now()
                while True:
                    try:
                        res = await asyncio.wait_for(self.ws.recv(), timeout=0.1)
                        print(res)
                    except (asyncio.TimeoutError, websockets.exceptions.ConnectionClosed) as e:
                        try:
                            if(last_ping_time+datetime.timedelta(seconds=10)<datetime.datetime.now()):
                                await self.ws.send('ping')
                                last_ping_time=datetime.datetime.now()
                                # res = await self.ws.recv()
                                # print(res)
                            continue
                        except Exception as e:
                            print(f"连接关闭，正在重连……,{e}")
                            break
                    print(get_timestamp() + res)
                    print("\n")
            except Exception as e:
                print(f"连接断开，正在重连……,异常：{e}")
                continue

    async def trade(self, trade_param):
        sub_str = json.dumps(trade_param)
        trade_async_rsp = await self.ws.send(sub_str)
        return trade_async_rsp

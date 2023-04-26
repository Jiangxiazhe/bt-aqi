import okex.Public_api as Public
import okex.Trade_api as Trade
import trade_ws_api


class APIWrapper:

    def __int__(self):
        pass

    def __init__(self, api_key, secret_key, passphrase, is_sim):
        self.public_api = Public.PublicAPI(api_key, secret_key, passphrase, False, is_sim)
        self.trade_api = Trade.TradeAPI(api_key, secret_key, passphrase, False, is_sim)
        self.wa_trade_api = trade_ws_api.WSTradeAPI(api_key, passphrase, secret_key)

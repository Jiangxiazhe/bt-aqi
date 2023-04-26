import asyncio
import datetime
import sys
import threading
import time

from PySide6 import QtCore

from PySide6.QtCore import QStringListModel, QTime, Qt, Slot, Signal, QObject, QThread, QDateTime
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QAbstractItemView, QMessageBox

from Config import Config
from api_wrapper import APIWrapper
# from common import get_setting_data,save_setting_data
from common import get_config_data, set_config_data
from mainwindow import Ui_mainWindow
from okex import consts
from okex.consts import API_URL
import okex.Public_api as Public

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class MessageBox(QtCore.QObject):
    messageBox_signal = Signal()


def connect_trade(loop):
    api_key = Context.api_key
    secret_key = Context.secret_key
    passphrase = Context.passphrase
    # flag是实盘与模拟盘的切换参数 flag is the key parameter which can help you to change between demo and real trading.
    is_sim = '1'  # 模拟盘 demo trading
    # is_sim = '0'  # 实盘 real trading
    Context.api_wrapper=APIWrapper(api_key=api_key,secret_key=secret_key,passphrase=passphrase,is_sim=is_sim)
    # 为子线程设置自己的事件循环
    # asyncio.set_event_loop(loop)
    # loop=asyncio.get_running_loop(loop)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    Context.loop=loop
    # loop=asyncio.get_event_loop()
    c=Context.api_wrapper.wa_trade_api.run()
    task = loop.create_task(c)
    loop.run_until_complete(task)
    print("task")


class Context():
    api_wrapper=None
    best_lag=datetime.timedelta.max
    avg_lag = datetime.timedelta(seconds=0.5)
    server_time=datetime.datetime.max
    record_local_time=datetime.datetime.now()
    api_key=None
    secret_key=None
    passphrase=None
    site_addr=None
    ws_addr=None
    loop=None

class UpdateTimeThread(QThread):

    update_time = Signal(datetime.datetime,datetime.timedelta)

    def __init__(self,parent=None)->None:
        super().__init__(parent)

    def run(self):
       while Context.api_wrapper==None:
           print("交易所未连接成功，等待中")
           time.sleep(5)
       while True:
            try:
                now = datetime.datetime.utcnow()
                time_res = Context.api_wrapper.public_api.get_system_time()
                time_stamp_ms = int(time_res['data'][0]['ts'])
                b = datetime.datetime.utcfromtimestamp(time_stamp_ms / 1000.)
                time_span = datetime.datetime.utcnow() - now
                lag=time_span *0.8
                Context.server_time=b + lag
                Context.record_local_time = datetime.datetime.now()
                print(f"交易所时间:{Context.server_time}")
                if Context.best_lag > lag:
                    Context.best_lag = lag
                Context.avg_lag=Context.avg_lag*0.5+lag*0.5
                print(f"全链路延迟:{time_span}")
                self.update_time.emit(Context.server_time,time_span)
                time.sleep(1)
            except Exception as e:
                print(e)
                time.sleep(0.2)


# 继承QWidget类，以获取其属性和方法
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.update_time_thread = UpdateTimeThread(self)
        # self.workerThread = QThread()
        # self.update_time_thread.moveToThread(self.workerThread)
        self.update_time_thread.update_time.connect(self.update)
        self.ui.start_order_button.clicked.connect(lambda:start_order(self))
        self.ui.save_setting_pushButton.clicked.connect(self.save_config_data)
        self.ui.load_setting_pushButton.clicked.connect(self.load_config_data)
        self.ui.connect_pb.clicked.connect(self.connect_to_exchange)

        self.ui.order_start_time_dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.ui.order_start_time_dateTimeEdit.setDisplayFormat("yyyy-MM-dd hh:mm:ss.zzz")

        # self.workerThread.run=self.update_time_thread.get_exch_time
        self.update_time_thread.start()
        self.load_config_data()


    @Slot(datetime.datetime,datetime.timedelta)
    def update(self,exchange_time:datetime.datetime,best_lag:datetime.timedelta):
        self.ui.exch_time_display_label.setText(exchange_time.strftime("%Y-%m-%d, %H:%M:%S:%f"))
        self.ui.best_lag_display_label.setText(f"{str(best_lag.total_seconds())} s")

    @Slot()
    def save_config_data(self):
        config_data={Config.API_ADDR:self.ui.site_addr_lineEdit.text(),Config.WS_ADDR:self.ui.ws_addr_le.text()
                     ,Config.API_KEY:self.ui.api_key_lineEdit.text(),Config.SECRET_KEY:self.ui.secret_key_lineEdit.text()
                     ,Config.PASS_PHRASE:self.ui.passphrase_le.text()}

        try:
            # 保存到环境变量中
            Context.site_addr = config_data[Config.API_ADDR]
            Context.ws_addr = config_data[Config.WS_ADDR]
            Context.api_key = config_data[Config.API_KEY]
            Context.secret_key = config_data[Config.SECRET_KEY]
            Context.passphrase = config_data[Config.PASS_PHRASE]
            if(Context.site_addr=="" or Context.ws_addr=="" or Context.api_key=="" or Context.secret_key=="" or Context.passphrase==""):
                raise KeyError()
            consts.API_URL = Context.site_addr
            consts.WS_URL = Context.ws_addr
        except KeyError as e:
            QMessageBox.information(None, "配置信息不全", "配置信息不全，请重新填写配置",
                                    QMessageBox.Ok,
                                    QMessageBox.Ok)
            return
        result= set_config_data(config_data)
        if result is None:
            QMessageBox.information(None, "保存失败", "保存失败",
                                    QMessageBox.Ok,
                                    QMessageBox.Ok)
        else:
            QMessageBox.information(None, "保存成功", "配置保存成功",
                                    QMessageBox.Ok,
                                    QMessageBox.Ok)

    @Slot()
    def load_config_data(self):
        config_data= get_config_data()
        if(config_data is None):
            QMessageBox.information(None, "未获取到配置文件", "请重新填写配置",
                                    QMessageBox.Ok,
                                    QMessageBox.Ok)
            return
        try:
            self.ui.site_addr_lineEdit.setText(config_data[Config.API_ADDR])
            self.ui.ws_addr_le.setText(config_data[Config.WS_ADDR])
            self.ui.api_key_lineEdit.setText(config_data[Config.API_KEY])
            self.ui.secret_key_lineEdit.setText(config_data[Config.SECRET_KEY])
            self.ui.passphrase_le.setText(config_data[Config.PASS_PHRASE])
            # 保存到环境变量中
            Context.site_addr=config_data[Config.API_ADDR]
            Context.ws_addr = config_data[Config.WS_ADDR]
            Context.api_key = config_data[Config.API_KEY]
            Context.secret_key = config_data[Config.SECRET_KEY]
            Context.passphrase = config_data[Config.PASS_PHRASE]
            if (Context.site_addr == "" or Context.ws_addr == "" or Context.api_key == "" or Context.secret_key == "" or Context.passphrase == ""):
                raise KeyError()
            consts.API_URL = Context.site_addr
            consts.WS_URL = Context.ws_addr
        except KeyError as e:
            QMessageBox.information(None, "配置信息不全", "配置信息不全，请重新填写配置",
                                    QMessageBox.Ok,
                                    QMessageBox.Ok)
            return

        QMessageBox.information(None, "配置已读取成功", "配置已读取成功",
                                QMessageBox.Ok,
                                QMessageBox.Ok)

    @Slot()
    def connect_to_exchange(self):
        if (Context.api_key == None or Context.secret_key == None or Context.passphrase == None or Context.site_addr == None or Context.ws_addr == None
        or Context.site_addr == "" or Context.ws_addr == "" or Context.api_key == "" or Context.secret_key == "" or Context.passphrase == ""):
            QMessageBox.information(None, "未成功获取配置", "请到设置页输入配置并保存",
                                    QMessageBox.Ok,
                                    QMessageBox.Ok)

        try:
            t1 = threading.Thread(target=connect_trade, args=(self.loop,))
            t1.setDaemon(True)
            t1.start()
        except Exception as e:
            print(f"连接交易所出错，异常信息:{e}")
            self.ui.connect_pb.setDisabled(False)
        self.ui.connect_pb.setDisabled(True)
        self.ui.connect_pb.setText("交易所已连接")
        # t1.join()




def trade(start_time:datetime.datetime, instId:str,price:str,volume:float,order_type:str,side:str,loop):

    Context.record_local_time

    order_id=datetime.datetime.now().timestamp()
    trade_param = {
                    "id": "1512",
                    "op": "order",
                    "args": [{
                        "side": side,
                        "instId": instId,
                        "tdMode": "cash",
                        "ordType": order_type,
                        "sz": volume,
                        "px":price,
                        "tgtCcy":"base_ccy"
                    }]
                    }
    calculate_start_time=start_time-Context.avg_lag
    current_server_time= Context.server_time + (datetime.datetime.now() - Context.record_local_time)
    count = 300
    while calculate_start_time>current_server_time:
        time.sleep(0.01)
        current_server_time = Context.server_time + (datetime.datetime.now() - Context.record_local_time)
        calculate_start_time = start_time-Context.avg_lag
    while count>0:
        print(f"{datetime.datetime.now()},开始下单:{trade_param}")
        fn = Context.api_wrapper.wa_trade_api.trade(trade_param)
        task = Context.loop.create_task(fn)
        count=count-1
        time.sleep(0.01)


def start_order(ui:MyWidget):
    try:
        if(Context.server_time>datetime.datetime.now()+datetime.timedelta(days=10)):
            QMessageBox.information(None, "未连接到交易所", f"请先连接交易所",
                                    QMessageBox.Ok,
                                    QMessageBox.Ok)
            return
        ui.ui.start_order_button.setText("正在运行中")
        ui.ui.start_order_button.setDisabled(True)
        instId=ui.ui.trade_pair_line_edit.text()
        price=ui.ui.order_price_doubleSpinBox.value()
        volume=str(ui.ui.order_volume_doubleSpinBox.value()/ui.ui.order_price_doubleSpinBox.value())
        side=None
        order_type=None
        if(ui.ui.direction_cb.currentText()=="买入"):
            side="buy"
        elif (ui.ui.direction_cb.currentText()=="卖出"):
            side="sell"

        if (ui.ui.order_type_cb.currentIndex() == 0):
            order_type= "limit"
        elif (ui.ui.order_type_cb.currentIndex()  == 1):
            order_type="fok"
        elif (ui.ui.order_type_cb.currentIndex() == 1):
            order_type = "ioc"

        start_time=ui.ui.order_start_time_dateTimeEdit.dateTime().toPython()
        t1=threading.Thread(target=trade,args=(start_time,instId,price,volume,order_type,side,ui.loop))
        t1.start()
    except Exception as e:
        ui.ui.start_order_button.setText("开始运行")
        ui.ui.start_order_button.setDisabled(False)

        QMessageBox.information(None, "下单任务发生异常，请检查参数后重试", f"异常信息:{e}",
                                QMessageBox.Ok,
                                QMessageBox.Ok)


if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)
    # 初始化并展示我们的界面组件
    window = MyWidget()
    loop = asyncio.get_event_loop()
    window.loop=loop
    window.show()
    # 结束QApplication
    sys.exit(app.exec())
    loop.close()
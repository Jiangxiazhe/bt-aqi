# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDoubleSpinBox,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(948, 615)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.main_tab = QTabWidget(self.centralwidget)
        self.main_tab.setObjectName(u"main_tab")
        self.monitor_tab = QWidget()
        self.monitor_tab.setObjectName(u"monitor_tab")
        self.gridLayout_6 = QGridLayout(self.monitor_tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 3, 3, 1, 1)

        self.start_order_button = QPushButton(self.monitor_tab)
        self.start_order_button.setObjectName(u"start_order_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_order_button.sizePolicy().hasHeightForWidth())
        self.start_order_button.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.start_order_button, 3, 2, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.best_lag_label = QLabel(self.monitor_tab)
        self.best_lag_label.setObjectName(u"best_lag_label")

        self.horizontalLayout_8.addWidget(self.best_lag_label)

        self.best_lag_display_label = QLabel(self.monitor_tab)
        self.best_lag_display_label.setObjectName(u"best_lag_display_label")

        self.horizontalLayout_8.addWidget(self.best_lag_display_label)


        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.trade_pair_label = QLabel(self.monitor_tab)
        self.trade_pair_label.setObjectName(u"trade_pair_label")

        self.gridLayout_3.addWidget(self.trade_pair_label, 0, 0, 1, 1)

        self.direction_lab = QLabel(self.monitor_tab)
        self.direction_lab.setObjectName(u"direction_lab")

        self.gridLayout_3.addWidget(self.direction_lab, 2, 0, 1, 1)

        self.order_volume_label = QLabel(self.monitor_tab)
        self.order_volume_label.setObjectName(u"order_volume_label")

        self.gridLayout_3.addWidget(self.order_volume_label, 1, 0, 1, 1)

        self.direction_cb = QComboBox(self.monitor_tab)
        self.direction_cb.addItem("")
        self.direction_cb.addItem("")
        self.direction_cb.setObjectName(u"direction_cb")

        self.gridLayout_3.addWidget(self.direction_cb, 2, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)

        self.order_type_cb = QComboBox(self.monitor_tab)
        self.order_type_cb.addItem("")
        self.order_type_cb.addItem("")
        self.order_type_cb.addItem("")
        self.order_type_cb.setObjectName(u"order_type_cb")

        self.gridLayout_3.addWidget(self.order_type_cb, 5, 1, 1, 1)

        self.order_start_time_label = QLabel(self.monitor_tab)
        self.order_start_time_label.setObjectName(u"order_start_time_label")

        self.gridLayout_3.addWidget(self.order_start_time_label, 4, 0, 1, 1)

        self.order_price_label = QLabel(self.monitor_tab)
        self.order_price_label.setObjectName(u"order_price_label")

        self.gridLayout_3.addWidget(self.order_price_label, 3, 0, 1, 1)

        self.order_type_lab = QLabel(self.monitor_tab)
        self.order_type_lab.setObjectName(u"order_type_lab")

        self.gridLayout_3.addWidget(self.order_type_lab, 5, 0, 1, 1)

        self.order_price_doubleSpinBox = QDoubleSpinBox(self.monitor_tab)
        self.order_price_doubleSpinBox.setObjectName(u"order_price_doubleSpinBox")
        self.order_price_doubleSpinBox.setDecimals(4)
        self.order_price_doubleSpinBox.setMaximum(1000000.000000000000000)

        self.gridLayout_3.addWidget(self.order_price_doubleSpinBox, 3, 1, 1, 1)

        self.trade_pair_line_edit = QLineEdit(self.monitor_tab)
        self.trade_pair_line_edit.setObjectName(u"trade_pair_line_edit")

        self.gridLayout_3.addWidget(self.trade_pair_line_edit, 0, 1, 1, 1)

        self.order_volume_doubleSpinBox = QDoubleSpinBox(self.monitor_tab)
        self.order_volume_doubleSpinBox.setObjectName(u"order_volume_doubleSpinBox")
        self.order_volume_doubleSpinBox.setDecimals(4)
        self.order_volume_doubleSpinBox.setMaximum(10000000.000000000000000)

        self.gridLayout_3.addWidget(self.order_volume_doubleSpinBox, 1, 1, 1, 1)

        self.order_start_time_dateTimeEdit = QDateTimeEdit(self.monitor_tab)
        self.order_start_time_dateTimeEdit.setObjectName(u"order_start_time_dateTimeEdit")

        self.gridLayout_3.addWidget(self.order_start_time_dateTimeEdit, 4, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exch_time_label = QLabel(self.monitor_tab)
        self.exch_time_label.setObjectName(u"exch_time_label")

        self.horizontalLayout.addWidget(self.exch_time_label)

        self.exch_time_display_label = QLabel(self.monitor_tab)
        self.exch_time_display_label.setObjectName(u"exch_time_display_label")

        self.horizontalLayout.addWidget(self.exch_time_display_label)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 2, 1, 1)

        self.connect_pb = QPushButton(self.monitor_tab)
        self.connect_pb.setObjectName(u"connect_pb")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.connect_pb.sizePolicy().hasHeightForWidth())
        self.connect_pb.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.connect_pb, 3, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.main_tab.addTab(self.monitor_tab, "")
        self.setting_tab = QWidget()
        self.setting_tab.setObjectName(u"setting_tab")
        self.gridLayout_4 = QGridLayout(self.setting_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.setting_label = QLabel(self.setting_tab)
        self.setting_label.setObjectName(u"setting_label")
        self.setting_label.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(10)
        sizePolicy3.setVerticalStretch(10)
        sizePolicy3.setHeightForWidth(self.setting_label.sizePolicy().hasHeightForWidth())
        self.setting_label.setSizePolicy(sizePolicy3)
        self.setting_label.setSizeIncrement(QSize(5, 2))

        self.verticalLayout.addWidget(self.setting_label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.setting_tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.ws_addr_lab = QLabel(self.setting_tab)
        self.ws_addr_lab.setObjectName(u"ws_addr_lab")

        self.gridLayout_2.addWidget(self.ws_addr_lab, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.load_setting_pushButton = QPushButton(self.setting_tab)
        self.load_setting_pushButton.setObjectName(u"load_setting_pushButton")

        self.horizontalLayout_2.addWidget(self.load_setting_pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.save_setting_pushButton = QPushButton(self.setting_tab)
        self.save_setting_pushButton.setObjectName(u"save_setting_pushButton")

        self.horizontalLayout_2.addWidget(self.save_setting_pushButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 5, 2, 1, 1)

        self.label_3 = QLabel(self.setting_tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.api_key_lineEdit = QLineEdit(self.setting_tab)
        self.api_key_lineEdit.setObjectName(u"api_key_lineEdit")

        self.gridLayout_2.addWidget(self.api_key_lineEdit, 2, 2, 1, 1)

        self.ws_addr_le = QLineEdit(self.setting_tab)
        self.ws_addr_le.setObjectName(u"ws_addr_le")

        self.gridLayout_2.addWidget(self.ws_addr_le, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.secret_key_lineEdit = QLineEdit(self.setting_tab)
        self.secret_key_lineEdit.setObjectName(u"secret_key_lineEdit")

        self.gridLayout_2.addWidget(self.secret_key_lineEdit, 3, 2, 1, 1)

        self.site_addr_lineEdit = QLineEdit(self.setting_tab)
        self.site_addr_lineEdit.setObjectName(u"site_addr_lineEdit")

        self.gridLayout_2.addWidget(self.site_addr_lineEdit, 0, 2, 1, 1)

        self.label_4 = QLabel(self.setting_tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.label = QLabel(self.setting_tab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)

        self.passphrase_le = QLineEdit(self.setting_tab)
        self.passphrase_le.setObjectName(u"passphrase_le")

        self.gridLayout_2.addWidget(self.passphrase_le, 4, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.main_tab.addTab(self.setting_tab, "")

        self.gridLayout_5.addWidget(self.main_tab, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        self.main_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u62a2\u5355\u5c0f\u5de5\u5177", None))
#if QT_CONFIG(tooltip)
        mainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.main_tab.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.start_order_button.setText(QCoreApplication.translate("mainWindow", u"\u5f00\u59cb\u8fd0\u884c", None))
        self.best_lag_label.setText(QCoreApplication.translate("mainWindow", u"\u6700\u5c11\u5ef6\u8fdf\u79d2\u6570", None))
        self.best_lag_display_label.setText(QCoreApplication.translate("mainWindow", u"0 s", None))
        self.trade_pair_label.setText(QCoreApplication.translate("mainWindow", u"\u4ea4\u6613\u5bf9", None))
        self.direction_lab.setText(QCoreApplication.translate("mainWindow", u"\u65b9\u5411", None))
        self.order_volume_label.setText(QCoreApplication.translate("mainWindow", u"\u59d4\u6258\u91cf", None))
        self.direction_cb.setItemText(0, QCoreApplication.translate("mainWindow", u"\u4e70\u5165", None))
        self.direction_cb.setItemText(1, QCoreApplication.translate("mainWindow", u"\u5356\u51fa", None))

        self.order_type_cb.setItemText(0, QCoreApplication.translate("mainWindow", u"\u9650\u4ef7\u5355", None))
        self.order_type_cb.setItemText(1, QCoreApplication.translate("mainWindow", u"\u9650\u4ef7\u59d4\u6258\uff0c\u5168\u90e8\u6210\u4ea4\u6216\u7acb\u5373\u53d6\u6d88", None))
        self.order_type_cb.setItemText(2, QCoreApplication.translate("mainWindow", u"\u9650\u4ef7\u59d4\u6258\uff0c\u7acb\u5373\u6210\u4ea4\u5e76\u53d6\u6d88\u5269\u4f59", None))

        self.order_start_time_label.setText(QCoreApplication.translate("mainWindow", u"\u5f00\u59cb\u4e0b\u5355\u65f6\u95f4", None))
        self.order_price_label.setText(QCoreApplication.translate("mainWindow", u"\u4ef7\u683c", None))
        self.order_type_lab.setText(QCoreApplication.translate("mainWindow", u"\u8ba2\u5355\u7c7b\u578b", None))
        self.order_price_doubleSpinBox.setSuffix(QCoreApplication.translate("mainWindow", u"    usdt", None))
#if QT_CONFIG(tooltip)
        self.order_volume_doubleSpinBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u5730\u65b9</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.order_volume_doubleSpinBox.setSuffix(QCoreApplication.translate("mainWindow", u"    usdt", None))
        self.order_start_time_dateTimeEdit.setDisplayFormat(QCoreApplication.translate("mainWindow", u"yyyy-MM-dd hh:mm:ss.zzz", None))
        self.exch_time_label.setText(QCoreApplication.translate("mainWindow", u"\u4ea4\u6613\u6240\u65f6\u95f4", None))
        self.exch_time_display_label.setText(QCoreApplication.translate("mainWindow", u"\u672a\u8fde\u63a5", None))
        self.connect_pb.setText(QCoreApplication.translate("mainWindow", u"\u8fde\u63a5\u4ea4\u6613\u6240", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.monitor_tab), QCoreApplication.translate("mainWindow", u"\u76d1\u63a7", None))
        self.setting_label.setText(QCoreApplication.translate("mainWindow", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"SecretKey", None))
        self.ws_addr_lab.setText(QCoreApplication.translate("mainWindow", u"WS\u5730\u5740", None))
        self.load_setting_pushButton.setText(QCoreApplication.translate("mainWindow", u"\u8bfb\u53d6", None))
        self.save_setting_pushButton.setText(QCoreApplication.translate("mainWindow", u"\u4fdd\u5b58", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"API\u7f51\u5740", None))
        self.api_key_lineEdit.setText("")
        self.ws_addr_le.setText("")
        self.secret_key_lineEdit.setText("")
        self.site_addr_lineEdit.setText("")
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"APIKey", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u5bc6\u7801", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.setting_tab), QCoreApplication.translate("mainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi


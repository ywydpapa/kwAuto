from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from config.errCode import *


class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        print("Kiwoom() class start")

        self.login_event_loop = QEventLoop()

        self.get_ocx_instance()
        self.event_slots()
        self.signal_login_commConnect()
        self.get_account_info()

    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot)

    def signal_login_commConnect(self):
        self.dynamicCall("CommConnect()")

        self.login_event_loop.exec_()

    def login_slot(self,err_code):
        print(errors(err_code)[1])

        self.login_event_loop.exit()

    def get_account_info(self):
        account_list = self.dynamicCall("GetLoginInfo(QString)", "ACCNO")
        account_num = account_list.split(';')[0]

        self.account_num = account_num

        print("계좌번호 : %s" % account_num)

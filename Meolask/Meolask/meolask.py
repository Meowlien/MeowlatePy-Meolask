﻿from flask import Flask
from MeowkitPy.logging.logger import log
from Meolask.template import (
    DatabaseContextRegisterTemplate,
    ServiceTemplate,
    ControllerRegisterTemplate
)

class Meolask(Flask):

    services = {}
    services_info = {}

    def register_service(self, svc: ServiceTemplate, key: str, more_info: str=None):
        if key in self.services:
            log.LogError(f'Registered (Service) Fail >> {key} >> key is already in use')
        else:
            self.services[key] = svc
            self.services_info[key] = more_info
            log.LogInfomation(f'Registered (Service) >> {key}')

    # 注冊：資料庫
    def register_database(self, database_register: DatabaseContextRegisterTemplate) -> None:
        database_register.register()

    # 注冊：控制器
    def register_controller(self, controller_register: ControllerRegisterTemplate) -> None:
        controller_register.register()





    '''
    **前置檢查-資料頭**
    - parameter: 需要驗證的欄位名稱 {
        範例： parameter = @"A,B..."; 檢查請求正文是否擁有欄位 A, B...
        注意： parameter = @"A,B,C..."; 欄位之間不可以有空格
    }
    - return: 是否存在必要資料欄位
    '''
    def check_valid_data(self, headers: dict, parameter: str, default_value: str='null'):
        result: dict = {}

        # No need to check
        if parameter == '':
            return True, result
        
        for key in parameter.split(','):
            value = headers.get(key, default_value)
            if value == default_value:
                return False, None
            result[key] = value
        return True, result

    def check_has_Cors_Policy(self):
        # todo: 未實作
        return True

    def check_comparison_data(self):
        # todo: 未實作
        return True

    def check_data_decrypt(self):
        # todo: 未實作
        return True
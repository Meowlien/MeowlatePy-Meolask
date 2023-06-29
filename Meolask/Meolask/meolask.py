from flask import Flask
from MeowkitPy.logging.logger import log
from Meolask.template import *
from Meolask.modules.service import ServiceTemplate
import typing as t

class Meolask(Flask):
    
    mode_debug: bool = True

    # 觸發注冊：服務(不屬於控制器)
    def register_services(self, services: IRegister) -> None:
        services.trigger_registration(self)

    # 觸發注冊：資料庫上下文清單
    def register_database(self, dbCtxs: IRegister, db: ServiceTemplate) -> None:
        dbCtxs.trigger_registration(self, db)

    # 注冊：資料庫上下文清單.MongoDbCtx
    def register_mongodbCtx(self, dbCtxs: dict[str,ServiceTemplate]):
        self.mongodbCtxs = dbCtxs # BUG: 把注冊上下文給 Meowlask 不合適

    # 注冊：資料庫上下文清單.PgSQLDbCtx
    # todo:

    # 觸發注冊：控制器清單
    def register_controllers(self, controllers: IRegister) -> None:
            controllers.trigger_registration(self)


    # 注冊：視圖(New)
    def register_view(self, view: any, url_prefix: str='/api/view', svc_registration_info: dict[str, str]=None) -> None:
        try:
            view(self, url_prefix, svc_registration_info)
        except Exception as e:
            log.LogError(f'{e}')

    # 注冊：方法視圖
    def register_method_view(self, view: MethodViewTemplate, svc_registration_info: dict[str, str]=None) -> None:
        view.register(self)
        if svc_registration_info != None:
            view.service_register(svc_registration_info)

    ## 注冊：藍圖
    #def register_blueprint(self, blueprint: BlueprintTemplate, **options: t.Any) -> None:
    #    self.register_blueprint(blueprint, **options)

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

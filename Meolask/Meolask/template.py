from flask import Flask # 導入 Meolask 會造成循環呼叫
from flask import Blueprint
from flask.views import MethodView
from MeowkitPy.logging.logger import log

# 模板-方法視圖
class MethodViewTemplate(MethodView):

    @property
    def view(self):
        return self._view
    @view.setter
    def view(self, view):
        self._view = view

    # 構建式
    def __init__(self, name: str='_view`', rule: str=None) -> None:
        super().__init__()
        self.name = name.replace('.', '_') + '_view'
        self.rule = rule
    
    # 一般路由注冊器
    def register(self, app: Flask) -> None:
        pass

    # 服務注冊器
    def service_register(self, service: object) -> None:
        self._service = service

# 模板-藍圖
class BlueprintTemplate(Blueprint):

    def __init__(self, name: str='_bp`', name_import: str=__name__, url_prefix=None, mode_debug: bool=False) -> None:
        super().__init__(name, name_import, url_prefix=url_prefix)
        self.register_local()
        #if mode_debug == True:
        #    log.LogInfomation("Registered >> '" + self.url_prefix + "'")

    def register_local(self) -> None:
        pass

# 模板-服務
class ServiceTemplate():

    def __init__(self, name: str=None) -> None:
        self.name = name

# 模板-注冊器
class RegisterTemplate():

    # [abstruct]
    def register(self, app: Flask) -> None:
        pass

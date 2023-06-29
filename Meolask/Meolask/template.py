'''
TODO: 模板方法拆分，避免循環呼叫
'''
from flask import Flask # 導入 Meolask 會造成循環呼叫
from flask import Blueprint
from flask.views import MethodView
from abc import ABC, abstractmethod
from MeowkitPy.logging.logger import log
#from Meolask.meolask import Meolask

# Test
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Meolask.meolask import Meolask
class TEST():
    @staticmethod
    def TTT(t: 'Meolask') -> None:
        print(f'TEST >>> : {id(t)}')

# 模板-方法視圖
class MethodViewTemplate(ABC, MethodView):

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
    @abstractmethod
    def register(self, app: Flask) -> None:
        pass

    # 服務注冊器
    def service_register(self, service: object) -> None:
        self._service = service

# 模板-藍圖
class BlueprintTemplate(ABC, Blueprint):

    def __init__(self, name: str='_bp`', name_import: str=__name__, url_prefix=None, mode_debug: bool=False) -> None:
        super().__init__(name, name_import, url_prefix=url_prefix)
        self.register_local()
        #if mode_debug == True:
        #    log.LogInfomation("Registered >> '" + self.url_prefix + "'")

    @abstractmethod
    def register_local(self) -> None:
        pass

# Interface(界面)-注冊器：
class IRegister(ABC):

    # 注冊器-觸發器：(觸發注冊行爲) >> Meolask
    def trigger_registration(self, app: Flask) ->None:
        self.register(app)

    @abstractmethod # 注冊行爲
    def register(self, app: Flask) -> None: pass

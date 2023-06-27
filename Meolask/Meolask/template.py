from flask import Flask # 導入 Meolask 會造成循環呼叫
from flask import Blueprint
from flask.views import MethodView
from abc import ABC, abstractmethod
from MeowkitPy.logging.logger import log

# 模板-服務
class ServiceTemplate(ABC):

    def __init__(self, id: str=None, name: str=None) -> None:
        self.id = id
        self.name = name
        #log.LogInfomation(f'Registered >> {self.id}')

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

# 注冊表 >> 改成 注冊器： Register >> 用於保存注冊内容
# 注冊表只有一個(Registry)，注冊器可以有很多個(Register) >> 注意注冊的基底類型
class Registry(ABC):
    _registry: dict[str, ServiceTemplate] = None

    @staticmethod
    def initialize():
        Registry._registry = {}


# 模板-注冊器 >> 改成 interface >> IRegister(ABC):
class RegisterTemplate(ABC):

    # 注冊表
    _registry: dict[str, ServiceTemplate] = None

    def __init__(self) -> None:
        super().__init__()
        if RegisterTemplate._registry is None:
            raise Exception('\n\n>>>> Pls setup container of register before first instance!\n')

    @staticmethod
    def initialize(
        container_registry: dict[str, ServiceTemplate]
    ):
        container_registry = RegisterTemplate._registry = {}
        print(f'TEST: {id(RegisterTemplate._registry)} >> origin')
        print(f'TEST: {id(container_registry)} >> argument')

    # 注冊
    @abstractmethod
    def register(self, app: Flask) -> None:
        pass

    # 登記
    def _register(self, services: list[ServiceTemplate]):
        for svc in services:
            if self._registry.get(svc.id) is None:
                self._registry[svc.id] = svc
            else:
                log.LogWarning(f'{svc.id} is already in Registry')

    # 打包服務
    def _package(self, services: list[ServiceTemplate], register: bool=False) -> dict[str, ServiceTemplate]:

        # 打包服務
        table: dict[str, ServiceTemplate] = {}
        for svc in services:
            if table.get(svc.id) is None:
                table[svc.id] = svc
            else:
                log.LogWarning(f'Fail >> {svc.id} is repeat in services list')

        # 是否需要注冊
        if register == True:
            self._register(services)

        return table

    @staticmethod
    def get(key: str, default: any=None):
        return RegisterTemplate._registry.get(key, default)

    @staticmethod
    def show():
        for key, val in RegisterTemplate._registry.items():
            log.LogInfomation(f'Registered (Service) >> {val.id}')

    # DEBUG 驗證
    @staticmethod
    def debug_compare_registry(container):
        print(f'TEST: {id(RegisterTemplate._registry)} >> origin')
        print(f'TEST: {id(container)} >> argument')

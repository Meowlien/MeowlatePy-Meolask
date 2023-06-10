from flask import Flask
from flask import Blueprint
from flask.views import MethodView

from MeowkitPy.logging.logger import log

import typing as t

# 模板-方法視圖
class MethodViewTemplate(MethodView):

    @property
    def view(self):
        return self._view
    @view.setter
    def view(self, view):
        self._view = view

    # 構建式
    def __init__(self, name: str='_view`', rule: str=None, dbgInfo: bool=False) -> None:
        super().__init__()
        self.name = name.replace('.', '_') + '_view'
        self.rule = rule
        if dbgInfo == True:
            log.LogInfomation("Registered >> '" + self.rule + "'")

    
    # 一般路由注冊器
    def register(self, app: Flask) -> None:
        pass

    # 服務注冊器
    def service_register(self, service: object) -> None:
        self._service = service

# 模板-藍圖
class BlueprintTemplate(Blueprint):

    def __init__(self, name: str='_bp`', name_import: str=__name__, url_prefix=None, dbgInfo: bool=False) -> None:
        super().__init__(name, name_import, url_prefix=url_prefix)
        self.register_local()
        if dbgInfo == True:
            log.LogInfomation("Registered >> '" + self.url_prefix + "'")

    def register_local(self) -> None:
        pass

# 模板-控制器注冊
class ControllerRegisterTemplate():

    '''
    :param app: Type >> Meolask
    '''
    def __init__(self, app, mode_debug: bool=False) -> None:
        self._app = app
        self._mode_debug = mode_debug
        self._init()

    # [abstruct]
    def _init(self) -> None:
        pass

    # [abstruct]
    def register(self) -> None:
        pass

    # 注冊：視圖
    def _register_view(self, view: any, url_prefix: str='/api/view', mode_debug: bool=False, service: object=None) -> None:
        try:
            view(self._app, url_prefix, mode_debug, service)
        except Exception as e:
            log.LogError(f'View Register Fail! >> {e}')

    # 注冊：方法視圖
    def _register_method_view(self, view: MethodViewTemplate, service: object=None) -> None:
        view.register(self._app)
        if service != None:
            view.service_register(service)

    # 注冊：藍圖
    def _register_blueprint(self, blueprint: BlueprintTemplate, **options: t.Any) -> None:
        self._app.register_blueprint(blueprint, **options)



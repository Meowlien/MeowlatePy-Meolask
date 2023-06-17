'''
範例：方法視圖控制器
'''
from flask import request
from Meolask.meolask import Meolask
from Meolask.template import MethodViewTemplate
from MeowkitPy.logging.logger import log

class ExampleMethodViewController(MethodViewTemplate):

    # Constructor 建構式
    def __init__(self, rule: str='/api') -> None:
        super().__init__(__name__, rule)
        self.view = ExampleMethodViewController.as_view(self.name)

    # [Override] 路由注冊
    def register(self, app: Meolask) -> None:
        self._app = app
        self._app.add_url_rule(self.rule + '/', view_func=self.view, methods=['GET','POST'])

    # methods=['GET']
    def get(self):
        return '[Get]: Method View Controller'

    # methods=['POST']
    def post(self):
        data = request.json
        log.LogInfomation(f"Post data >> {data}")
        return f'[Post]: Method View Controller >> {data}'

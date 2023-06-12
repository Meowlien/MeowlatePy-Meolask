'''
範例：藍圖控制器
'''
from flask import Flask
from Meolask.template import BlueprintTemplate
from MeowkitPy.logging.logger import log

class ExampleBlueprintController(BlueprintTemplate):

    def __init__(self,
        url_prefix=None,
        mode_debug: bool=False
    ) -> None:
        super().__init__(
            name=self.__class__.__name__,
            name_import=__name__.replace('.', '_') + '_bp',
            url_prefix=url_prefix,
            mode_debug=mode_debug
        )

    # 路由注冊
    def register_local(self) -> None:
        self.add_url_rule('/', view_func=self.index) # 導向指定方法
        # More...

    def index(self):
        return 'Blueprint Controller'

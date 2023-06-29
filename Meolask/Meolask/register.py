'''
注冊頁面(標準)
'''
from Meolask.meolask import Meolask
from Meolask.modules.service import ServiceRegister

# 引入：目標
from Meolask.swagger.meowagger import Meowagger
# More...

# 一般注冊器 (汎用型)
class BaseControllers(ServiceRegister):

    # [Vir:Override]
    def register(self, app: Meolask) -> None:
        app.register_blueprint(Meowagger('/api/swagger').blueprint) # OpenApi
        # More...
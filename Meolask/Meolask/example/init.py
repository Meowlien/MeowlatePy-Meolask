'''
範例：專案初始化
'''
from Meolask.meolask import Meolask
from MeowkitPy.logging.logger import log
from Meolask.register import BaseControllers
from Meolask.example.register import ExampleControllers

# 創建 app 實體
app = Meolask(__name__)

# 注冊：控制器
app.register_controllers(BaseControllers())
app.register_controllers(ExampleControllers())

# Debug
with app.test_request_context(): # 獲取所有已注冊的路由
    routes = [str(rule) for rule in app.url_map.iter_rules()]
for route in routes: # 輸出所有已注冊的路由
    log.LogInfomation(f'Registered >> {route}')
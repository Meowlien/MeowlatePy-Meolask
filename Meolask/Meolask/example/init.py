'''
範例：專案初始化
'''
from Meolask.meolask import Meolask
from MeowkitPy.logging.logger import log
from Meolask.register import ControllerRegister
from Meolask.example.register import ExampleControllerRegister

# 創建 app 實體
app = Meolask(__name__)

# Config
# -----------------------------------------------------
mode_debug: bool = True
# -----------------------------------------------------

# 準備：控制器注冊表單
controllers = ControllerRegister(app, mode_debug)
ex_controllers = ExampleControllerRegister(app, mode_debug)

# 注冊：控制器
app.register_controller(controllers)
app.register_controller(ex_controllers)

# Debug
with app.test_request_context(): # 獲取所有已注冊的路由
    routes = [str(rule) for rule in app.url_map.iter_rules()]
for route in routes: # 輸出所有已注冊的路由
    log.LogInfomation(f'Registered >> {route}')
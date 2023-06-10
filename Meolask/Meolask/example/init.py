'''
範例：專案初始化
'''
from Meolask.meolask import Meolask
from Meolask.register import ControllerRegister
from Meolask.example.controllers.registers.register_controller import ExampleControllerRegister

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
'''
範例：專案初始化
'''
from Meolask.meolask import Meolask
from MeowkitPy.logging.logger import log
from Meolask.register import BaseControllers
from Meolask.example.register import ExampleControllers

# 初始化:前置
# -----------------------------------------------------
# todo:

# 服務項
# -----------------------------------------------------
app = Meolask(__name__)

# 注冊列表:(每個注冊都以組為單位，即一個注冊内容中，有許多注冊項)
# -----------------------------------------------------
app.register_controllers(BaseControllers())
app.register_controllers(ExampleControllers())

# 初始化:後置
# -----------------------------------------------------
# todo:

# Debug 日志
# -----------------------------------------------------
if app.mode_debug == True:

    # 顯示 <服務-注冊表> 清單
    # todo:
    #log.dividers('-')

    # 顯示 <資料庫上下文-注冊表> 清單
    # todo:
    #log.dividers('-')

    # 顯示 <控制器-注冊表> 清單
    with app.test_request_context(): # 獲取所有已注冊的路由
        routes = [str(rule) for rule in app.url_map.iter_rules()]
    for route in routes: # 輸出所有已注冊的路由
        log.LogInfomation(f'Registered (Route) >> {route}')
    log.dividers('-')


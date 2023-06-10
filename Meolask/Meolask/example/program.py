'''
範例：主程式
'''
from Meolask.example.init import app    # from <你的專案(初始化程式碼)> import app
from MeowkitPy.logging.logger import log
import settings as config

# 主程式
if __name__ == '__main__':

    HOST = config.HOST
    PORT = config.PORT

    app.run(HOST, PORT)

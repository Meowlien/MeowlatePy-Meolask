'''
- 請勿參考：如需參考(主程式)範例 >> 請至 example.program.py
'''
from doctest import debug
from MeowkitPy.logging.logger import log

proj_test: bool = True

if proj_test == True:
    log.LogInfomation('Start >> Project <TEST>')

    '''
    <Start> 以下程式會作爲參考範例，因此請記得同步到 example.program.py
    '''
    from Meolask.example.init import app
    from MeowkitPy.logging.logger import log
    import settings as config

    # 主程式
    if __name__ == '__main__':

        HOST = config.HOST
        PORT = config.PORT

        app.run(HOST, PORT)
    '''
    <End> =======================================================
    '''
else:
    log.LogInfomation('Start >> Project')
    from Meolask import app
    import settings as config

    # 主程式
    if __name__ == '__main__':

        HOST = config.HOST
        PORT = config.PORT

        app.run(HOST, PORT, debug=False)

from flask import request, render_template
from datetime import datetime
from Meolask.meolask import Meolask
from MeowkitPy.logging.logger import log

def example_view(app: Meolask, url_prefix: str='/api/example/view', service: object=None):

    mode_debug = app.mode_debug

    # 前置檢查：是否有服務對象
    #if service == None:
    #    log.LogWarning(f'Registering [Fail] >> {url_prefix}')
    #    raise AttributeError(f'Service cannot be None!')

    # Post 範例
    @app.route(url_prefix + '/post', methods=['POST'])
    def post():

        '''
        前置檢查 
        -----------------------------------------------------
        '''
        # 資料頭(Head)
        check_conditions = '' # 檢查條件
        is_header_pass, headers = app.check_valid_data(request.headers, check_conditions)
        # 資料體(Body)
        check_conditions = '' # 檢查條件
        is_body_pass, request_data = app.check_valid_data(request.data, check_conditions)
        # 跨域資訊(CorsPolicy)
        is_Cors_pass = app.check_has_Cors_Policy()
        # 高速資料庫比對資料(Redis)
        is_redis_pass = app.check_comparison_data()
        # 數據解密(Decryption)
        is_decrypt_pass = app.check_data_decrypt()

        # 是否-通過檢查
        if (is_header_pass == True
            and is_body_pass == True
            and is_Cors_pass == True
            and is_redis_pass == True
            and is_decrypt_pass == True
        ):
            '''
            執行請求 
            -----------------------------------------------------
            '''
            # todo: 呼叫資料庫 | 執行請求
            print("Do Somthing")

        return 'example_view >> result'

    # Home
    @app.route(url_prefix + '/')
    @app.route(url_prefix + '/home')
    def home():
        """Renders the home page."""
        return render_template(
            'index.html',
            title='Home Page',
            year=datetime.now().year,
        )

    # Contact
    @app.route(url_prefix + '/contact')
    def contact():
        """Renders the contact page."""
        return render_template(
            'contact.html',
            title='Contact',
            year=datetime.now().year,
            message='Your contact page.'
        )

    # About
    @app.route(url_prefix + '/about')
    def about():
        """Renders the about page."""
        return render_template(
            'about.html',
            title='About',
            year=datetime.now().year,
            message='Your application description page.'
        )

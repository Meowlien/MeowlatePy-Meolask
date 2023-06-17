'''
範例：控制器注冊單
'''
from Meolask.meolask import Meolask
from Meolask.template import RegisterTemplate

# 引入：目標
from Meolask.example.controllers.example_view import example_view as ExampleViewController
from Meolask.example.controllers.example_method_view import ExampleMethodViewController
from Meolask.example.controllers.example_blueprint import ExampleBlueprintController
# More...

# 注冊器
class ExampleControllers(RegisterTemplate):

    # [Abs:Override]：注冊器
    def register(self, app: Meolask) -> None:
        app.register_view(        ExampleViewController,          '/api/example/view')
        # More...
        app.register_method_view( ExampleMethodViewController(    '/api/example/methodView'))
        # More...
        app.register_blueprint(   ExampleBlueprintController(     '/api/example/blueprint'))
        # More...
'''
範例：控制器注冊單
'''
from Meolask.template import ControllerRegisterTemplate

# 引入：目標
from Meolask.example.controllers.example_view import example_view as ExampleViewController
from Meolask.example.controllers.example_method_view import ExampleMethodViewController
from Meolask.example.controllers.example_blueprint import ExampleBlueprintController
# More...

# 注冊器
class ExampleControllerRegister(ControllerRegisterTemplate):
    # [Override]
    def register(self) -> None:
        self._register_view(        ExampleViewController,          '/api/example/view',             self._mode_debug)
        # More...
        self._register_method_view( ExampleMethodViewController(    '/api/example/methodView',       self._mode_debug))
        # More...
        self._register_blueprint(   ExampleBlueprintController(     '/api/example/blueprint',        self._mode_debug))
        # More...
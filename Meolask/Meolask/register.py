from Meolask.template import ControllerRegisterTemplate

# 引入：目標
from Meolask.swagger.meowagger import Meowagger
# More...

# 一般注冊器 (汎用型)
class ControllerRegister(ControllerRegisterTemplate):
    # [Override]
    def register(self) -> None:
        self._register_blueprint(Meowagger(          '/api/swagger',       mode_debug=self._mode_debug).blueprint) # OpenApi
        # More...
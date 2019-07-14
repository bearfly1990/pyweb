from app.main import main
from app.main.controller.json_controller import json_controller


DEFAULT_BLUEPRINT = (
    (main, '/'),
    (json_controller,'/data')

)


# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)

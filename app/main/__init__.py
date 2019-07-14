from flask import render_template
from flask import Blueprint
from flask import url_for
from flask import jsonify
import json
main = Blueprint('main', __name__) # template_folder='templates', static_folder='static', static_url_path="/static"

# @main.route('/', defaults={'path': ''})
# @main.route('/<path:path>')
@main.route('/',methods=['GET', 'POST'], defaults={'path': ''})
def index(path):
  return render_template('index.html')

@main.route('/app/static',methods=['GET', 'POST'], defaults={'path': ''})
def static(path):
  return render_template('index.html')


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

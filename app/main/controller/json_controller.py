from flask import jsonify
from flask import Blueprint
import json
json_controller = Blueprint('render_json', __name__)# template_folder='templates', static_folder='static', static_url_path="/static"

@json_controller.route('/')
def return_json():
    print('coming???!!!')
    json_str = '''
    {
    "data": [
      {
        "title": "湘潭夜跑",
        "author": "张三",
        "date": "2018年9月20日"
      },
      {
        "title": "爬岳麓山",
        "author": "李四",
        "date": "2018年9月30日"
      },
      {
        "title": "湘潭夜跑",
        "author": "张三",
        "date": "2018年9月20日"
      }
    ]
    }'''

    return  jsonify(json.loads(json_str))

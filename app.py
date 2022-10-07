import requests
from controller import order_controller

from flask import *
from flask_restx import Api, Resource
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__, template_folder="templates")

app.register_blueprint(order_controller.order_router, url_prefix="/order")

@app.route('/index')
def index():
  return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
  path = []
  print(len(path))
  if (len(path) == 0):
    print("path","is", 0)
  return render_template('error/page_not_found.html', path=path)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=3001)
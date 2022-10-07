import requests
from flask import *
from flask_restx import Api, Resource
from jinja2 import Environment, PackageLoader, select_autoescape

order_router = Blueprint('order', __name__, template_folder="templates")

@order_router.route('/home')
def renderHome():
  response = requests.get("http://localhost:3000/order/home")
  result = response.json()
  recMenus = result['recMenus']
  path = result['path']
  
  return render_template('order/home.html', recMenus=recMenus, path=path)

@order_router.route('/recommend/all')
def renderRecommendHome():
  response = requests.get("http://localhost:3000/order/recommend/all")
  result = response.json()
  recMenus = result['recMenus']
  path = result['path']
  
  return render_template('order/recommend.html', recMenus=recMenus, path=path)

@order_router.route('/recommend/set-menu')
def renderSetMenuHome():
  response = requests.get("http://localhost:3000/order/recommend/set-menu")
  result = response.json()
  recMenus = result['recMenus']
  path = result['path']

  return render_template('order/recommend.html', recMenus=recMenus, path=path)

@order_router.route('/recommend/single-menu')
def renderSingleMenuHome():
  response = requests.get("http://localhost:3000/order/recommend/single-menu")
  result = response.json()
  recMenus = result['recMenus']
  path = result['path']

  return render_template('order/recommend.html', recMenus=recMenus, path=path)

@order_router.route('/recommend/side-menu')
def renderSideMenuHome():
  response = requests.get("http://localhost:3000/order/recommend/side-menu")
  result = response.json()
  recMenus = result['recMenus']
  path = result['path']

  return render_template('order/recommend.html', recMenus=recMenus, path=path)
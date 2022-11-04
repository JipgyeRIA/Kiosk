import requests
from flask import *
from flask_restx import Api, Resource
from jinja2 import Environment, PackageLoader, select_autoescape
from kiosk_face import get_single_face_data, face_age_gender_checker
import cv2;

order_router = Blueprint('order', __name__, template_folder="templates")
server_url = "http://localhost:3000";
# server_url = "https://jipgyeria.herokuapp.com"
cam_stream = cv2.VideoCapture(0)

@order_router.route('/home')
def renderHome():
  path = "order/home";
  return render_template('index.html', path=path)

@order_router.get('/item/<item_id>')
def renderItemDetail(item_id):
  print("ORDER!!!!")
  response = requests.get(server_url + "/order/item/" + item_id)
  result = response.json()
  item = result['item']
  path = result['path']
  print(result)

  return render_template('order/item-detail.html', item=item, path=path)

@order_router.route('/recommend/all')
def renderRecommendHome():
  response = requests.get(server_url + "/order/recommend/all")
  result = response.json()
  recMenus = result['recMenus']
  path = result['path']
  
  return render_template('order/recommend.html', recMenus=recMenus, path=path)

@order_router.route('/recommend/set-menu')
def renderSetMenuHome():
  response = requests.get(server_url + "/order/recommend/set-menu")
  result = response.json()
  recMenus = result['recMenus']
  path = result['path']

  return render_template('order/recommend.html', recMenus=recMenus, path=path)

@order_router.route('/recommend/single-menu')
def renderSingleMenuHome():
  response = requests.get(server_url + "/order/recommend/single-menu")
  result = response.json()
  recMenus = result['recMenus']
  path = result['path']

  return render_template('order/recommend.html', recMenus=recMenus, path=path)

@order_router.route('/recommend/side-menu')
def renderSideMenuHome():
  response = requests.get(server_url + "/order/recommend/side-menu")
  result = response.json()
  recMenus = result['recMenus']
  path = result['path']

  return render_template('order/recommend.html', recMenus=recMenus, path=path)

@order_router.route('/recommend/group')
def recommendGroupMenu():
  emb = get_single_face_data(cam_stream)
  if emb == -1:
    response = requests.get(server_url + "/order/recommend/all")
    result = response.json()
    recMenus = result['recMenus']
    path = result['path']
    
    return render_template('order/recommend.html', recMenus=recMenus, path=path)
  
  else:
    body = json.dumps({"emb": emb})
    response = requests.post(server_url + "/order/recommend/group", data=body, headers= {"content-type": "application/json"})
    result = response.json()

    if result['result'] is False:
      path = "order/home";
      return render_template('index.html', path=path)
    
    recMenus = result['recMenus']
    path = result['path']
    
    return render_template('order/recommend.html', recMenus=recMenus, path=path)

@order_router.route('/recommend/single')
def recommendSingleMenu():
  single_info = face_age_gender_checker(cam_stream)
  if single_info == -1:
    path = "order/home";
    return render_template('index.html', path=path)

  response = requests.post(server_url + "/order/recommend/single", data=json.dumps({"single_info": single_info}), headers= {"content-type": "application/json"})
  result = response.json()  
  recMenus = result['recMenus']
  path = result['path']

  return render_template('order/recommend.html', recMenus=recMenus, path=path)

# @order_router.route('/recommend/group')
# def recommendGroupMenu():
#   response = requests.post(server_url + "/order/recommend/group")
#   result = response.json()
#   recMenus = result['recMenus']
#   path = result['path']

#   return render_template('order/recommend.html', recMenus=recMenus, path=path)
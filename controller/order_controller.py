import requests
from flask import *
from flask_restx import Api, Resource
from jinja2 import Environment, PackageLoader, select_autoescape
from kiosk_face import get_single_face_data
import cv2;

order_router = Blueprint('order', __name__, template_folder="templates")
server_url = "http://localhost:3000";
cam_stream = cv2.VideoCapture(0)

@order_router.route('/home')
def renderHome():
  response = requests.get(server_url + "/order/home")
  result = response.json()
  recMenus = result['recMenus']
  path = result['path']
  
  return render_template('order/home.html', recMenus=recMenus, path=path)

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
def getGroupRecommendMenu():
  emb = get_single_face_data(cam_stream)
  if emb == -1:
    response = requests.get(server_url + "/order/recommend/all")
    result = response.json()
    recMenus = result['recMenus']
    path = result['path']
    
    return render_template('order/recommend.html', recMenus=recMenus, path=path)
  
  else:
    print("emb입니당 ", emb)
    body = json.dumps({"emb": emb})
    response = requests.post(server_url + "/order/recommend/group", data=body, headers= {"content-type": "application/json"})
    result = response.json()
    recMenus = result['recMenus']
    path = result['path']
    
    return render_template('order/recommend.html', recMenus=recMenus, path=path)
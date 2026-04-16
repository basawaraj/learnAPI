from flask import Blueprint,request,jsonify
from learnAPI.API2.services.user_service import get_user_data

user_bp = Blueprint('user_bp', __name__)            

@user_bp.route('/user/<name>')
def get_user(name):
    user_data = get_user_data(name)
    return jsonify(user_data)               
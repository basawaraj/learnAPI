from flask import Blueprint,request,jsonify
from services.user_service import get_user_data,search_data

user_bp = Blueprint('user_bp', __name__)            

@user_bp.route('/user/<name>')
def get_user(name):
    user_data = get_user_data(name)
    return jsonify(user_data)               

@user_bp.route("/search")
def search():
    query=request.args.get("query")

    if not query:
        return jsonify({
                 "error": "query parameter is required"
        })
    result=search_data(query)
    return jsonify(result)
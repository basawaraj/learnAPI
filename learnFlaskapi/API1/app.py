from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "hello mac"

@app.route('/user/<name>')
def users(name):
    return f'hello {name}'

@app.route('/json')
def json():
    test_json = {"name":"mac","age":20}
    return jsonify(test_json)

@app.route('/search')
def search():
    query = request.args.get('query')
    return f'you searched for: {query}'

@app.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    return jsonify({
    "status": "success",
    "user": username
}), 200

@app.route('/login-auth',methods=['POST'])
def login_auth():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")
    if username=="admin" and password=="1234":
        return jsonify({
            "status":"success",
            "user":username
        }),200
    else: 
        return jsonify({
            "error": "invalid user"

        }), 401

if __name__=="__main__":
    app.run(debug=True)

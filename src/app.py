from flask import Flask, request, make_response, jsonify

PORT = 5789
HOST = '0.0.0.0'

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is the default message'

@app.route('/classify', methods=['GET'])
def classify():
    if request.method == 'GET' and request.args:
        # if req.args exists then it will give us a dict
        req = request.args
        img = req['img']

        # gender = classify_image(img)
        res = make_response( jsonify( {"response","Default gender for test"} ), 200)
        return res
    
    res = make_response( jsonify( {"error","Error either its not a get request or args are not prresent in the request"} ), 400)
    return res
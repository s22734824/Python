from flask import  Flask, request
import base64
import io
from PIL import Image
app=Flask(__name__)

@app.route('/')
def print_hi():
    rr = "123123"
    print(123123)
    return "acc"

@app.route('/showImg', methods=['POST'])
def process_json():
    img = stringToImage(request.data)
    img.show()
    return request.data


def stringToImage(base64_string):
    imgdata = base64.b64decode(base64_string)
    return Image.open(io.BytesIO(imgdata))

if __name__ == '__main__':
    app.run(debug=True)

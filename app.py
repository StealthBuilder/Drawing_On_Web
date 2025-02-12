from flask import Flask, render_template, request, send_file
from PIL import Image
import base64
import io

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    data = request.json["image"]
    image_data = base64.b64decode(data.split(",")[1])
    
    image = Image.open(io.BytesIO(image_data))
    image_path = "static/drawing.png"
    image.save(image_path)
    
    return {"url": image_path}

if __name__ == "__main__":
    app.run(debug=True)
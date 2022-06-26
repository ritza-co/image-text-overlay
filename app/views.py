from app import app, conn
from app.utils import process_job
import redis, time, os, base64
from rq import Queue
from flask import render_template, request, send_file, redirect, url_for
from PIL import Image, ImageFont, ImageDraw

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/handle_submit', methods=['POST'])
def handle_submit():
    que = Queue(connection=conn)

    logo = request.files['logo']
    logo = Image.open(logo)
    logo.save("logo.png")

    with open("logo.png", "rb") as img_file:
        print("res")
        b64_string = base64.b64encode(img_file.read())

    result = que.enqueue(process_job, request.form['overlay_text'], b64_string)
    time.sleep(3)
    return send_file("../result.jpg", mimetype='image/jpg', as_attachment=True, download_name="result.jpg")
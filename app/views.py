from app import app, que
from app.utils import process_job
import os
from flask import render_template, request, send_file, redirect, url_for
from PIL import Image, ImageFont, ImageDraw

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/handle_submit', methods=['POST'])
def handle_submit():
    result = que.enqueue(process_job, request.form['overlay_text'], request.files)
    return redirect(url_for(''))

    # overlay_text = request.form['overlay_text']
    # title_font = ImageFont.truetype('PlayfairDisplay-Black.ttf', 20)

    # my_image = Image.open("fall-season.jpeg")
    # width, height = my_image.width, my_image.height

    # image_editable = ImageDraw.Draw(my_image)
    # x, y = (width - 510, height-400)

    # if len(overlay_text) > 25:
    #     string_center_index = len(overlay_text) / 2
    #     overlay_text = overlay_text[:int(string_center_index)] + "\n" + overlay_text[int(string_center_index):]

    #     w, h = title_font.getsize(overlay_text[:int(string_center_index)])
    #     image_editable.rectangle((x, y, x + w, y + 2*h), fill='black')
    # else:
    #     w, h = title_font.getsize(overlay_text)
    #     image_editable.rectangle((x, y, x + w, y + h), fill='black')

    # image_editable.text((x,y), overlay_text, (247, 250, 251), font=title_font)

    # if request.files:
    #     logo = request.files['logo']
    #     logo = Image.open(logo)
    #     logo_width, logo_height = logo.size
    #     logo = logo.convert("RGBA")
    #     my_image.paste(logo, (width - logo_width, height - logo_height))

    # my_image.save("result.jpg")
    # return send_file("../result.jpg", mimetype='image/jpg', as_attachment=True, download_name="result.jpg")
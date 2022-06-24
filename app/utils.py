from flask import send_file
import io, base64
from PIL import Image, ImageFont, ImageDraw

def process_job(logo):
    overlay_text = "form_data_dict['overlay_text']"
    #logo = form_data_dict['logo']

    title_font = ImageFont.truetype('PlayfairDisplay-Black.ttf', 20)

    my_image = Image.open("fall-season.jpeg")
    width, height = my_image.width, my_image.height

    image_editable = ImageDraw.Draw(my_image)
    x, y = (width - 510, height-400)

    slice_str = str(logo)[2:-1]

    print("Job started ",slice_str)

    if len(overlay_text) > 25:
        string_center_index = len(overlay_text) / 2
        overlay_text = overlay_text[:int(string_center_index)] + "\n" + overlay_text[int(string_center_index):]

        w, h = title_font.getsize(overlay_text[:int(string_center_index)])
        image_editable.rectangle((x, y, x + w, y + 2*h), fill='black')
    else:
        w, h = title_font.getsize(overlay_text)
        image_editable.rectangle((x, y, x + w, y + h), fill='black')

    image_editable.text((x,y), overlay_text, (247, 250, 251), font=title_font)

    if logo:
        img = Image.open(io.BytesIO(base64.decodebytes(bytes(slice_str, "utf-8"))))
        #logo = logo['logo']
        #logo = Image.open(logo)
        logo_width, logo_height = img.size
        logo = logo.convert("RGBA")
        my_image.paste(logo, (width - logo_width, height - logo_height))

    my_image.save("result.jpg")
    print("Job processed")
    return "Done"
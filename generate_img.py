from PIL import Image, ImageDraw, ImageFont
import qrcode

# Importar Pandas
import pandas as pd


# Configuracion del carnet
font = "Candarab.ttf"
font_size = 14
pixels_per_character = font_size / 2


def generar_carnet(name, employee_id, campaign):
    # Load background template
    card_template = Image.open("fondo.png")
    # Resize background template to 305 x 530
    card_template = card_template.resize((305, 530))
    # Load employee photo
    photo = Image.open(f"fotos/{employee_id}.png")  # formato fotos?
    photo = photo.resize((160, 224))  # Resize photo to fit the card
    # Calculate coordinates for centering
    photo_x = (card_template.width - photo.width) // 2
    photo_y = 75
    name_x = (card_template.width - len(name) * pixels_per_character) // 2
    name_y = photo_y + 230
    campaign_x = (card_template.width - len(campaign) * pixels_per_character) // 2
    campaign_y = name_y + 25  # 250
    qr_x = (card_template.width - 100) // 2  # Assuming QR code size of 100x100 pixels
    qr_y = campaign_y + 30  # 300
    # here
    id_x = (card_template.width - len(employee_id) * pixels_per_character) // 2
    id_y = qr_y + 120  # 420
    # Paste the photo onto the template
    card_template.paste(photo, (photo_x, photo_y))
    # Create a drawing context
    draw = ImageDraw.Draw(card_template)
    # Load fonts
    font_name = ImageFont.truetype(font, font_size)
    font_campaign = ImageFont.truetype(font, font_size)
    font_id = ImageFont.truetype(font, font_size)
    # Write employee name
    draw.text((name_x, name_y), name, fill="black", font=font_name)
    # Write campaign title
    draw.text((campaign_x, campaign_y), f"{campaign}", fill="black", font=font_campaign)
    # Generate and paste the QR code
    qr = qrcode.QRCode(version=1, box_size=5, border=1)
    qr.add_data(employee_id)
    qr.make()
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img = qr_img.resize((100, 100))  # Resize the QR code image
    card_template.paste(qr_img, (qr_x, qr_y))
    # Write employee ID
    draw.text((id_x, id_y), f"{employee_id}", fill="black", font=font_id)
    # Save the generated ID card
    card_template.save(f"{employee_id}_id_card.png")
    print("ID card generated successfully.")


# Leer el archivo de Excel en un DataFrame
df = pd.read_excel("empleados.xlsx")

for indice, fila in df.iterrows():
    generar_carnet(fila["Nombre agente"], str(fila["Documento"]), fila["Campaña"])

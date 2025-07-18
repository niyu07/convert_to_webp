import os
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

image_dir = os.getenv("IMAGE_DIR")
output_dir = os.getenv("OUTPUT_DIR")

valid_extensions = [".png", ".jpg", ".jpeg"]

for filename in os.listdir(image_dir):
    name, ext = os.path.splitext(filename)
    if ext.lower() in valid_extensions:
        input_path = os.path.join(image_dir, filename)
        output_path = os.path.join(output_dir, name + ".webp")

        img = Image.open(input_path).convert("RGB")
        img.save(output_path, "webp")
        print(f"{filename} → WebPに変換")
    
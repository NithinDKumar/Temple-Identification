import io
import numpy as np
from PIL import Image

def preprocess_image(image, target_size):
    image = Image.open(io.BytesIO(image))
    image = image.convert("RGB")
    image.thumbnail(target_size, Image.LANCZOS)
    new_image = Image.new("RGB", target_size)
    new_image.paste(
        image, ((target_size[0] - image.size[0]) // 2, (target_size[1] - image.size[1]) // 2)
    )
    image_array = np.array(new_image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

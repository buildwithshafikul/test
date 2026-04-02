from PIL import Image
import os

# Jey image-ti ke base dhore kaj korben (source image)
source_image_path = "StoreLogo.jpg" 

# Kothay save hobe shei folder
output_folder = "generated_images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List of dictionaries: Name, Size (Width, Height), ebong Format
image_configs = [
    {"name": "StoreLogo 720X1080", "size": (720, 1080), "format": "png"},
    {"name": "StoreLogo 1080X1080", "size": (1080, 1080), "format": "png"},
    {"name": "StoreLogo 300X300", "size": (300, 300), "format": "png"},
    {"name": "StoreLogo 150X150", "size": (150, 150), "format": "png"},
    {"name": "StoreLogo 71X71", "size": (71, 71), "format": "png"},
    {"name": "StoreLogo 584X800", "size": (584, 800), "format": "png"},
    {"name": "StoreLogo 1920X1080", "size": (1920, 1080), "format": "png"},
    # {"name": "banner_high", "size": (1920, 1080), "format": "jpg"},
    # {"name": "favicon_icon", "size": (32, 32), "format": "ico"},
    # {"name": "StoreLogo", "size": (256, 256), "format": "ico"}
]

def create_images():
    try:
        # Original image open kora
        with Image.open(source_image_path) as img:
            for config in image_configs:
                # Resize kora
                resized_img = img.resize(config["size"])
                
                # File path toiri kora
                file_name = f"{config['name']}.{config['format']}"
                save_path = os.path.join(output_folder, file_name)
                
                # Image save kora
                # Note: 'jpg' format-er khetre Pillow 'JPEG' likhte hoy
                img_format = config["format"].upper()
                if img_format == "JPG":
                    img_format = "JPEG"
                
                resized_img.save(save_path, format=img_format)
                print(f"Created: {file_name} with size {config['size']}")
                
    except FileNotFoundError:
        print("Error: 'original_photo.jpg' file-ti khuje paowa jayni!")

if __name__ == "__main__":
    create_images()
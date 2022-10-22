import os

class Settings:
    # PATHS
    output_save_path = os.path.abspath('output')
    # From client
    image_name = 'image.jpg'
    background_image_name = 'background.jpg'
    # From server
    rgba_name = 'rgba.png' # Predicted alpha channel with original image
    merged_image_name = 'fg_bg_merged.png'

    image_path = os.path.join(output_save_path, image_name)
    background_image_path = os.path.join(output_save_path, background_image_name)
    rgba_path = os.path.join(output_save_path, rgba_name)
    merged_image_path = os.path.join(output_save_path, merged_image_name)

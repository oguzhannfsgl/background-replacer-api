import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from PIL import Image
import numpy as np
import uvicorn

from settings import Settings as sett
from utils import clear_file

from PaddleSeg.Matting.deploy.python.infer import get_default_predictor
from PaddleSeg.Matting.tools.bg_replace import merge_fg_bg
predictor = get_default_predictor('PaddleSeg/Matting/output/export/deploy.yaml')


app = FastAPI()


@app.get('/')
def home():
    return {'Homepage'}

@app.post('/upload-image', status_code=200,
          description='Upload an image.')
def upload_image(image_file:UploadFile, background_file:UploadFile, background_tasks:BackgroundTasks):
    background_tasks.add_task(clear_file, sett.output_save_path)
    img = None
    try:
        img = np.array(Image.open(image_file.file))
        background = np.array(Image.open(background_file.file))
    except:
        raise HTTPException(status_code=400, detail='Not a valid file type. Choose an image file.')
        return
    print(img.shape)
    Image.fromarray(img).save(sett.image_path)
    Image.fromarray(background).save(sett.background_image_path)
    predictor.run(sett.image_path, sett.rgba_path)
    # output: ../output/fg_bg_merged.png
    merge_fg_bg(sett.rgba_path, sett.background_path, sett.merged_image_path)
    return FileResponse(sett.merged_image_path)


if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000)

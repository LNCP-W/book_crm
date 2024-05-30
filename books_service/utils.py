import requests
import magic
from pathlib import Path

def get_author_img(name):
    req = '+'.join(name.split())
    url = f'https://www.google.com/search?q={req}+фото+автора&tbm=isch'
    return  get_first_image(name, url)

def get_book_image(name):
    req = '+'.join(name.split())
    url=f'https://www.google.com/search?q={req}+фото+книги&tbm=isch'
    return  get_first_image(name, url)

def get_first_image(name, url, path='static/'):
    try:
        r = requests.request(method='get', url=url)
        if r.status_code != 200:
            raise
        im_link = str(r.content).split('<img')[2].split('src=')[1].split('"')[1]
        img_resp = requests.request(method='get', url=im_link)
        if img_resp.status_code != 200:
            raise
        img = img_resp.content
        content_type, file_extension = magic.from_buffer(img, mime=True).split("/")
        file_name = f'{"_".join(name.split())}.{file_extension}'
        return file_name, img

    except Exception:
        return False, False
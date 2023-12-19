import requests
import json
import os 



url = 'http://127.0.0.1:8000/api/get_status/list/'

image_path = os.path.join(os.getcwd(), 'download.jpg')


def do(method='get' , data={} , is_json=True, img_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    if img_path is not None:
        with open(img_path, 'rb') as image:
            file_data = {
                'image':image
            }
            r = requests.request(method , url , data=data , headers=headers, files=file_data)
    else:
        r = requests.request(method , url , data=data , headers=headers)
    print(r.status_code)
    print(r.text)
    return r


#do(data={'id':7})
#do(method='post', data={'user':2, 'content':'Hello From Shariq'})
#do(method='delete', data={'id':150})
do(method='put', data={'id':8, 'user':2 ,'content':''} ,img_path=image_path, is_json=False)
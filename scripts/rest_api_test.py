import requests
import json
import os 

auth_url = 'http://127.0.0.1:8000/api/auth/jwt/'

auth_url_3 = 'http://127.0.0.1:8000/api/auth/user/'

auth_url_2 = 'http://127.0.0.1:8000/api/auth/'

url = 'http://127.0.0.1:8000/api/status/list/'

image_path = os.path.join(os.getcwd(), 'download.jpg')



post_headers ={
    'content-type':'application/json',
    'Authorization': 'Bearer '+ 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAzMDgyODA0LCJpYXQiOjE3MDI5OTY0MDQsImp0aSI6IjM1YmNhODZkZTMwYjQxOGI4ZmNiNTRlMDkyM2IwYjgzIiwidXNlcl9pZCI6Mn0.gyLBz9dZrLdT8jmTiup2PZmVX47S41fh3KyrjF0ivCg'
}

# username = str(input("Enter username : "))
# email = str(input("Enter Email : "))
# password = str(input("Enter Password : "))
# password2 = str(input("Confirm Password : "))   ,data=json.dumps(post_user_data),


post_user_data = {
    'username':'Habib'
}
#Checking that user is already exists or not
post_user_response = requests.get(auth_url_3+str(post_user_data['username'])+'/',  headers=post_headers)
print(post_user_response.status_code)
print(post_user_response.text)
#token = post_user_response.json()['access']
# print(token.text)

# user_data = {
#     'username':username,
#     'password':password,
# }

# Generating the token for user after validation from bd
# post_user_response = requests.post(auth_url, data=json.dumps(user_data) , headers=post_headers)
# print("Your Login/Registered Token to Use Api")
# print(post_user_response.status_code)
# print(post_user_response.text)

















# get_response= requests.get(url + str(12))
# print(get_response.text)

# print("Status Code for GET Response: ", get_response.status_code)


post_headers={
     'content-type':'application/json',
    #  'Authorization': 'Bearer '+ token
}

post_user_data_2 = {
    'username': 'ShariqShafiq',
    'password':'admin',
 #   'token': token
}

#post_request = requests.post(auth_url_2 , data = post_user_data_2 , headers=post_headers)
# print(post_request.text)
# print(post_request.status_code)

# update_request = requests.put(url+str(18)+"/", data = post_data , headers=post_headers)
# print(update_request.text)
# print(update_request.status_code)


# def do(method='get' , data={} , is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#         with open(img_path, 'rb') as image:
#             file_data = {
#                 'image':image
#             }
#             r = requests.request(method , url , data=data , headers=headers, files=file_data)
#     else:
#         r = requests.request(method , url , data=data , headers=headers)
#     print(r.status_code)
#     print(r.text)
#     return r


#do(data={'id':7})
#do(method='post', data={'user':2, 'content':'Hello From Shariq'})
#do(method='delete', data={'id':150})
#do(method='put', data={'id':8, 'user':2 ,'content':''} ,img_path=image_path, is_json=False)
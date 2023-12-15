import json
import requests  # Thirds Party library for http requests

#update_number = int(input("Enter update Id: "))


url = 'http://127.0.0.1:8000/'

end_points = 'api/list/'
end_points_seperate = f'api/detail/'
# Retrieving Endpoint of Api
def get_list():   # --> Lists out all the data
    r = requests.get(url+end_points)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 200:
        print("something bad happens to your request! Do Check That")
    data = r.json()
    for objs in data:
        print(f"The Id Number {objs['id']} of Update Number {objs['id']} :",objs['id'])   
        if objs['id']: # --> This is for user interaction for each id
            r = requests.get(url+end_points_seperate+str(objs['id'])+"/")
            data = r.json()
            print(data)
    return data

# Create Endpoint of Api
def create_update():
    new_data = {
        'user':1,
        'content':"This is new update cost",
    }
    r = requests.post(url+end_points , data=new_data)
    print(r.headers)
    if r.status_code == requests.codes.ok:
        #print(r.json())
        return r.json()
    return r.text

# Delete Endpoint of Api
def delete_update():
    new_data = {
        'user':1,
        'content':"This is new update cost",
    }
    r = requests.post(url+end_points , data=new_data)
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print(r.json())
        return r.json()
    return r.json()



print(create_update())


get_list()

print(delete_update())
#print(get_list())    


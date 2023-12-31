import json
import requests  # Thirds Party library for http requests

#update_number = int(input("Enter update Id: "))


url = 'http://127.0.0.1:8000/'

end_points = 'api/list/'
end_points_seperate = f'api/detail/'
# Retrieving Endpoint of Api
def get_list(id=None):   # --> Lists out all the data
    data = json.dumps({})
    if id is not None:
        data = json.dumps({'id':id})
    r = requests.get(url+end_points, data=data)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 200:
        print("something bad happens to your request! Do Check That")
    data = r.json()
    return data

# Create Endpoint of Api
def create_update():
    new_data = {
        'user':1,
        'content':"Shariq",
        "image":"shariq.jpg",
    }
    r = requests.post(url+end_points , data=json.dumps(new_data))
    #print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
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


def do_obj_update():
    new_data = {
        'id':3,
        'user':1,
        'content':"New Api Call By M. Shariq",
    }
    print(new_data['id'])
    r = requests.put(url+end_points+str(new_data['id'])+"/" , data=json.dumps(new_data))
    #print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print(r.json())
        return r.json()
    return r.text



def do_obj_delete():
    
    #id = int(input("Enter Integer id to delete the update : "))
    new_data = {
        'id':3,
     #'content':'update 2',
    }
    #print("Update No . ",new_data['id']," is requested to be deleted")
    r = requests.delete(url+end_points , data = json.dumps(new_data))
    #print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


#print(do_obj_update())

#print(do_obj_delete())
#print(create_update())


#get_list()

# print(delete_update())
print(get_list())    


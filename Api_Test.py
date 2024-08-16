import requests

def fectch():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    # print(type(response))
    # print(response)
    data=response.json()
    print(f"Data :{data}")
    print(type(data))

    if data["success"]  and "data" in data:
        user_data=data["data"]
        user_name=user_data["login"]["username"]
        country= user_data["location"]["country"]

        return user_name,country
    else:
        raise Exception("faild to fetch user data")
    

def main():
    try:
        username,country=fectch()
        print(f"User Name : {username} , Country : {country}")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()


#post request 

url="https://jsonplaceholder.typicode.com/posts"
data={
    "title":"pinkush gole",
    "body":'Indore',
    "userIdL":1
}
headers={
    'Content-type': 'application/json; charset=UTF-8',
  }
response=requests.post(url,headers=headers,json=data)
print(response.text)
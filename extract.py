import requests

r = requests.get('https://jsonplaceholder.typicode.com/users')
list_of_dict = r.json()

# transform
len_ = len(list_of_dict)
def variables():
    for some in range(len_):
        list_of_variables = list_of_dict[some]

        id_ = list_of_variables['id']
        name_ = list_of_variables['name']
        username_ = list_of_variables['username']
        email_ = list_of_variables['email']
        city_ = list_of_variables['address']['city']
        
        use = [id_, name_, username_,email_,city_]
        print(use)


print(variables())
# contact interface
# name - "no name"
# age -"10"
# phone_number -"nil" 
 
users ={}

def create_users(name,age,phone_number,):
    return {"name" :name, "age": age, "phone_number": phone_number,} 

def add_user(user, users):
    key = user['name']
    if users.get(key):
        return  None 
    users[key] = user 
    return users 
    
def print_users(users):
    for key, users in users.items(): 
        print(key,users['phone_number']) 

def get_user_info():
    name = input("Name")  
    age = input('Age')  
    phone_number = input('phone numbers: ')         
    return create_users(name,age,phone_number) 

def main(users):
    print('1 - view contacts') 
    print('2 - Add contacts') 
    print('3 - quit')
    response = int(input('>>> ') )
    print(response ==1)
    if response == 1:
        print_users(users) 
        input()
    elif response ==2: 
      users =  add_user(get_user_info(),users)
    elif response ==3:
      exit()          

if __name__ == '__main__':
    while True:
       main(users)    
import json
import os
import random
import asyncio
global authorization
authorization=False

def start_up_menu():
    print('''
Hey there , Welcome to ProjectX
[1] About & Feedback
[2] Tests
[3] View
[4] Entry Editor
[5] View Categories
[6] Exit
    ''')
    return input('Enter your choice ')
def authorization():
    print('''
    [1] Check if user is authorized
    [2] Apply for access
    [3] Login
    ''')
    inx=input('Enter your Choice')
    if inx =="1":
        check_authorization()
    elif inx =="2":
        print('Not available yet')
    elif inx=="3":
        login()
def login():
    print('Enter your username')
    username=input('Username ')
    print('Enter your password')
    password=input('Password ')
    with open('Amura/data.json','r') as f:
        data=json.load(f)
    if username==data['owner']['code'] and password==os.environ['Password']:
        print('Login successful')
        authorization=True
        return True
    else:
        login
        return False
def check_authorization():
    '''Create a function which checks that whether the user is authorized or not on basis of a global variable which is set to False in start of project and if the user is log in then it sets the variable to True'''
    if authorization==True:
        print('You are authorized')
    else:
        print('You are not authorized')
def feedback():
    ''' Ask user to send a rating from 1 to 5 and store it in file'''
    with open('Amura/data.json','r') as f:
        data=json.load(f)
    print('Please rate the project from 1 to 5')
    rating=input('Enter your rating ')
    if rating in ['1','2','3','4','5']:
        data['feedback']=rating
        with open('Amura/data.json','w') as f:
            json.dump(data,f)
        print('Thank you for your feedback')
    else:
        print('Invalid rating')
        feedback()
def exit(choice=1):
    if choice==00:
        ask=input('Are you sure you want to exit? [Y/N] ')
        if ask=='Y':
            print('Exiting...')
            os.system('cls')
            print('[###################] Completed Shutdown')
            os.system('cls') 
            exit()
        else:
            print('Aborted')
            os.system('cls')
    else:
        
        startproject()
     
def tests():
    print('''
    [1] Print all entries
    ''')
    choice=input('Enter your choice ')
    if choice=='1':
        with open('Amura/data.json','r') as f:
            data=json.load(f)
        print(data)
    
                               
    
    
def tell_about_project():
    with open('Amura/data.json','r') as f:
            data=json.load(f)

    print('''
    ProjectX is a project which encryptes certain enteties
    Owner=Pranjal Prakarsh aka Prakarsh17''')
    print('Name : '+data['owner']['name'])
    print('Github : '+data['owner']['github'])
    print('ProjectX Code : '+data['owner']['code'])
    print('Tessarect Discord Bot : '+data['owner']['ad'])
    feedback()
def view_registry():
    print('''
    [1] View all
    [2] View by ID
    [3] View by Name
    [4] View by Class
    ''')
    return input('Enter your choice ')
def view_all():
    with open('Amura/data.json','r') as f:
        data=json.load(f)
    print(data)
    for i in data['entries']:
        print(i,data['entries'][i]['code'],data['entries'][i]['class'])
def view_by_id():
    id=input('Enter ID ')
    with open('Amura/data.json','r') as f:
        data=json.load(f)
    for i in data['entries']:
        if i==id:
            print(i,data['entries'][i]['code'],data['entries'][i]['class'])
def view_by_name():
    name=input('Enter name ')
    with open('Amura/data.json','r') as f:
        data=json.load(f)
    print('Results : ')
    for i in data['entries']:
        if data['entries'][i]['name']==name:
            print(i,data['entries'][i]['code'],data['entries'][i]['class'])
def view_by_class():
    class_=input('Enter class ')
    with open('Amura/data.json','r') as f:
        data=json.load(f)
    for i in data['entries']:
        if data['entries'][i]['class']==class_:
            print(i,data['entries'][i]['code'],data['entries'][i]['class'])
def view_categories():
    with open('Amura/data.json','r') as f:
        data=json.load(f)
    for i in data['categories']:
        print(i,data['categories'][i])
def entryeditor():
    print('''
    [1] Create new entry
    [2] Delete entry
    [3] Edit entry
    [4] Create new Category
    [5] Delete Category
    [6] Edit Category
    [7] Exit
    ''')
    return input('Enter your choice ')
def create_code(name,clas,category):
    code=''
    code+=str(category)  
    for i in name:
        code+=str(ord(i))
    for x in range(2):
        code += str(random.randint(0, 9))    
    code+=str(clas)

    return code

def create_new_entry():
    name=input('Enter name ')  
    clas=input('Enter class ')
    print('Here are available Categories')
    with open('Amura/data.json','r') as f:
        data=json.load(f)
    #print(data['categories'])
    for i in data['categories']:
        print(i,"- ",data['categories'][i])    
    category=input('Enter category ')
    if category in data['categories']:
        finalcategory=category
        encryptedcode=create_code(name,clas,finalcategory)
        data['entries'][encryptedcode]={'name':name,'class':clas,'category':finalcategory}
        if not encryptedcode in data['entries']:
            with open('Amura/data.json','w') as f:
                json.dump(data,f)
            
            print('Successfully Entered, Code is '+encryptedcode)
        else:
            print('Entry already exists with code '+encryptedcode)

    else:
        print('Invalid category')

def delete_entry():
    with open('Amura/data.json','r') as f:
        data=json.load(f)
    print('Here are available entries')
    for i in data['entries']:
        print(i,"- ",data['entries'][i]['name'])
    id=input('Enter ID ')
    if id in data['entries']:
        del data['entries'][id]
        with open('Amura/data.json','w') as f:
            json.dump(data,f)
        print('Successfully Deleted')
    else:
        print('Invalid ID')
def edit_entry():
    with open('Amura/data.json','r') as f:
        data=json.load(f)
    print('Here are available entries')
    for i in data['entries']:
        print(i,"- ",data['entries'][i]['name'])
    id=input('Enter ID ')
    if id in data['entries']:
        name=input('Enter name ')
        clas=input('Enter class ')
        category=input('Enter category ')
        if category in data['categories']:
            finalcategory=category
            encryptedcode=create_code(name,clas,finalcategory)
            data['entries'].pop(id)
            data['entries'][encryptedcode]={'name':name,'class':clas,'category':finalcategory}
            with open('Amura/data.json','w') as f:
                json.dump(data,f)
            print('Successfully Edited')
        else:
            print('Invalid category')
    else:
        print('Invalid ID')
def create_new_category():
    categoryinf=input('Enter category description')
    categoryin=input('Enter category Initials')
    with open('Amura/data.json','r') as f:
        data=json.load(f)
    data['categories'][categoryin]=categoryinf
    with open('Amura/data.json','w') as f:
        json.dump(data,f)
    print('Successfully Created')
def delete_category():
    with open('Amura/data.json','r') as f:
        data=json.load(f)
    print('Here are available Categories')
    for i in data['categories']:
        print(i,"- ",data['categories'][i])
    category=input('Enter category ')
    if category in data['categories']:
        del data['categories'][category]
        with open('Amura/data.json','w') as f:
            json.dump(data,f)
        print('Successfully Deleted')
    else:
        print('Invalid category')
def edit_category():
    with open('Amura/data.json','r') as f:
        data=json.load(f)
    print('Here are available Categories')
    for i in data['categories']:
        print(i,"- ",data['categories'][i])
    category=input('Enter category ')
    if category in data['categories']:
        categoryinf=input('Enter category description')
        categoryin=input('Enter category Initials')
        data['categories'][categoryin]=categoryinf
        with open('Amura/data.json','w') as f:
            json.dump(data,f)
        print('Successfully Edited')
    else:
        print('Invalid category')
def startproject():
    authorization()
    
    if not authorization:
        return "Authorization Failed"
    start=start_up_menu()
    if start=='1':
        tell_about_project()
    elif start=='2':
        tests()
    elif start=='3':
        choice=view_registry()
        if choice=='1':
            view_all()
        elif choice=='2':
            view_by_id()
        elif choice=='3':
            view_by_name()
        elif choice=='4':
            view_by_class()
    elif start=='4':
        choice=entryeditor()
        if choice=='1':
            create_new_entry()
        elif choice=='2':
            delete_entry()
        elif choice=='3':
            edit_entry()
        elif choice=='4':
            create_new_category()
        elif choice=='5':
            delete_category()
        elif choice=='6':
            edit_category()
        elif choice=='7':
            exit()
    elif start=='5':
        view_categories()  
    elif start=="6":
        exit(00)     
while True:
    asyncio.sleep(5)
    startproject()

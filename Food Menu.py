import random
breakfast='paratha and egg' # same for everyday
lunch_dinner=['rotti-bhindi','chat','rice','burger','macroni','alo ka paratha','rotti-ghobi'] #changes everyday
from datetime import datetime
def food_menu():
    print('Welcome to the Food Menu!')
food_menu()
def day():
    day=datetime.today().strftime('%A') # to check day of week
    if day=='Monday':
        return "Today's menu is:" + (breakfast)+ " "+"in Breakfast," ,random.choice(lunch_dinner)+ " "+"in lunch," +random.choice(lunch_dinner)+ " "+"in dinner"
    elif day=='Tuesday':
          return "Today's menu is:" + (breakfast)+ " "+"in Breakfast," ,random.choice(lunch_dinner)+ " "+"in lunch," +random.choice(lunch_dinner)+ " "+"in dinner"
    elif day=='Wednesday':
          return "Today's menu is:" + (breakfast)+ " "+"in Breakfast," ,random.choice(lunch_dinner)+ " "+"in lunch," +random.choice(lunch_dinner)+ " "+"in dinner"
    elif day=='Thursday':
        return "Today's menu is:" + (breakfast)+" "+ "in Breakfast," ,random.choice(lunch_dinner)+ " "+"in lunch," +random.choice(lunch_dinner)+ " "+"in dinner"
    elif day=='Fridayday':
        return "Today's menu is:" + (breakfast)+" "+ "in Breakfast," ,random.choice(lunch_dinner)+ " "+"in lunch," +random.choice(lunch_dinner)+ " "+"in dinner"
    elif day=='Saturday':
        return "Today's menu is:" + (breakfast)+" "+ "in Breakfast," ,random.choice(lunch_dinner)+ " "+"in lunch," +random.choice(lunch_dinner)+ " "+"in dinner"
    elif day=='Sunday':
        return "Today's menu is:" + (breakfast)+" "+ "in Breakfast," ,random.choice(lunch_dinner)+ " "+"in lunch," +random.choice(lunch_dinner)+ " "+"in dinner"
day()

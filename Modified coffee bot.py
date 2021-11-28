def coffee_bot(): # add price in coffee bot according to every selection then sum price and tell customer total price
    print('Welcome to the cafe!')
coffee_bot()
def get_size():
    res=input('What size drink can I get for you \n[a] Small \n[b] Medium \n[c] Large\n')
    if res=='a':
        return 'Small'
    elif res=='b':
          return 'Medium'
    elif res=='c':
          return 'Large'
    else:
        print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    return get_size()
size=get_size()
def get_drink_type():
    res=input('What type of drink would you like?\n[a] Brewed Coffee \n[b] Mocha \n[c] Latte\n')
    if res=='a':
          return 'Brewed coffee'
    elif res=='b':
          return 'Mocha'
    elif res=='c':
          return 'order_latte'
    else:
        print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    return get_drink_type()
drink_type=get_drink_type()
def order_latte():
    res=input('And what kind of milk for your latte?\n[a]2% milk \n[b]Non-fat milk \n[c]Soy milk \n')
    if res=='a':
        return 'latte'
    elif res=='b':
        return 'non-fat latte'
    elif res=='c':
        return 'soy latte'
    else:
        print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    return order_latte()
latte=order_latte()
def cup_type():
    res=input('What kind of cup would you like? \n[a]Plastic cup \n[b]own reuseable cup \n')
    if res=='a':
        return 'plastic cup'
    elif res=='b':
        return 'own reusebale cup'
    else:
        print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    return cup_type()
cup=cup_type()
#for price
size_price={'Small':1,'Medium':2,'Large':3}
drink_price={'Brewed coffee':1,'Mocha':2,'order_latte':3}
latte_price={'latte':1,'non-fat latte':2,'soy latte':3}
cup_price={'plastic cup':3,'own reusebale cup':0}
price=0
for key,val in size_price.items():
    if size==key:
        price+=val
for key,val in drink_price.items():
    if drink_type==key:
        price+=val
for key,val in latte_price.items():
    if latte==key:
        price+=val
for key,val in cup_price.items():
    if cup==key:
        price+=val        
print("Alright, that's a" + " " + (size) + " " + (drink_type) + " " + "with" + " " + (cup) + "!" + "and your bill is" + " " + str(price) + "$")
name=input('Can I get your name please?')
print("Thanks," + " " + (name) + " " + "! Your drink will be ready shortly.")
        

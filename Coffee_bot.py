
def coffee_bot():
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
print("Alright, that's a" + " " + (size) + " " + (drink_type) + " " + "with" + " " + (cup) + "!")
name=input('Can I get your name please?')
print("Thanks," + " " + (name) + " " + "! Your drink will be ready shortly.")


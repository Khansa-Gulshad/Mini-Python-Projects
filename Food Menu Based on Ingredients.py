import random
from collections import Counter

#whatever food menu you can cook and ingredients required for each menu
ingredients = {'rotti-bhindi':["bhindi"],
               'chat':["boiled-chana","boiled-potatoe", 'onion','tomatoe'],
               'Rice':["mix-vege","beef-with-bone"],
               'burger':["kebab","bun",'cheese'],
               'macroni':["mix-vege","macroni"],
              'alo ka paratha':["boiled-potatoe"],
               'rotti-ghobi':["ghobi","potatoe"],
               'dumplings':["dumplings"],
              'fish':["fish"],
               'hot-pot':["beef","mushroom", 'potatoe'],
               'mix-veg roll':["mix-vege"],
              'sweet potatoe':["sweet-potatoe"],
               'beetroot':["beetroot"],
               'order outside':["nothing"],
              'alo cutlets':["boiled-potatoe"]}
ingre=[item for item in input("What are your ingredients: ").split()]
def ing(ingre,ingredients):
    for key, value in ingredients.items():
        for i in range(len(value)):
            if len(value)==len(ingre):
                if value[i]==ingre[i]:
                    print('Hello, this is in menu today')
                    return key
                
ing(ingre,ingredients)

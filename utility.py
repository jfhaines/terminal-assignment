from custom_exceptions import InputError
from randomizer import RandomList

def randomizer_assembler(item, probability = 1):
    return {'item': item, 'probability': probability}

def rand_item(items):
    list_store = []
    for item, probability in items:
        list_store.append(randomizer_assembler(item, probability))
    return RandomList(list_store).get_random()

def rand_unique_items(num, items):
    item_list = items.copy()
    dict_list = []
    selected = []
    for item in item_list:
        dict_list.append(randomizer_assembler(item))
    for i in range(num):
        item = (RandomList(dict_list).get_random())
        selected.append(item)
        dict_list.remove(randomizer_assembler(item))
    return selected[0] if num == 1 else selected



def get_index(prompt, item_list):
    user_input = input(prompt)
    if user_input.isdigit() and int(user_input) >= 0 and int(user_input) < len(item_list):
        return int(user_input)
    else:
        raise InputError(user_input)
from custom_exceptions import InputError
from randomizer import RandomList

def rand_item(items):
    list_store = []
    for item, chance in items:
        details = {item: chance}
        list_store.append(details)
    return RandomList(list_store).get_random()

def get_index(prompt, item_list):
    user_input = input(prompt)
    if user_input.isdigit() and int(user_input) >= 0 and int(user_input) < len(item_list):
        return int(user_input)
    else:
        raise InputError(user_input)
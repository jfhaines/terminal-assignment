from randomizer import RandomList

from custom_exceptions import InputError


def randomizer_assembler(item, probability = 1):
    return {'item': item, 'probability': probability}

def rand_item(items):
    list_store = []
    for item, probability in items:
        list_store.append(randomizer_assembler(item, probability))
    return RandomList(list_store).get_random()

def rand_unique_items(num, items):
    dict_list = []
    selected = []
    for item in items:
        dict_list.append(randomizer_assembler(item))
    while len(selected) < min(num, len(items)):
        item = RandomList(dict_list).get_random()
        if item not in selected:
            selected.append(item)
    return selected[0] if num == 1 else selected


def get_index(prompt, item_list):
    user_input = input(prompt)
    if (user_input.isdigit() and int(user_input) >= 0
        and int(user_input) < len(item_list)):
        return int(user_input)
    else:
        raise InputError(user_input)

def convert_list_to_prompt_str(list_items):
    list_store = list(enumerate(list_items))
    for index, move in list_store:
        list_store[index] = f'{index} = {move}'
    return ', '.join(list_store)

def get_item(prompt, item_list):
    while True:
            try:
                index = get_index(prompt, item_list)
                return item_list[index]
            except InputError as err:
                print(err.user_message)

def should_continue(prompt):
    while True:
        try:
            user_input = input(f'{prompt} (y | n): ')
            if user_input == 'n':
                return False
            elif user_input == 'y':
                return True
            else:
                raise InputError(user_input)
        except InputError as err:
            print(err.user_message)
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    tuple_ = (len(string), string.upper(), string.lower())
    return tuple_


def is_contains(string, list_to_search):
    count_calls()
    new_list_to_search = [x.upper() for x in list_to_search]
    if string.upper() in new_list_to_search:
        return True
    else:
        return False


print(string_info('Cat'))
print(string_info('Banana'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)

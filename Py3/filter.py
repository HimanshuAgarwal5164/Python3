lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

def f(s):
    return 'w' in s

filter_testing = filter(f,lst_check)
print(list(filter_testing))

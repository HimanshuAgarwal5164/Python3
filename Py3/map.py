lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

def double(x):
    return 2*x

greeting_doubled = map(double,lst)

print(list(greeting_doubled))

def entering(any_function):
    def inner_enter(a,b):
        a = list(map(int, input("Enter numbers in a:").strip().split()))[:n]
        b = list(map(lambda x: x * x, a))
        return any_function(a,b)
    return inner_enter
@entering
def add_func(a,b):

    # print("\nList is - ", a)
    #
    # print("\nSquare list is -", b)


    x = list(map(lambda l, m: l + m, a, b))
    return x
print(entering(a,b))
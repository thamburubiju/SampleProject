def divide (x,y):
    try:
        result = x//y
        print("yeah your answer is:",result)
    except ZeroDivisionError:
        print("sorry you are dividing by zero")
divide(3,2)
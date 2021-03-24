a=10
k=0
try:
    k=int(input("enter a number"))
    print(k)
    print(a / k)
except ZeroDivisionError as e:
    print("not possible",e)
except ValueError as e:
    print(e)
except Exception as e:
    print("general exception",e)
finally:print("resource closed")
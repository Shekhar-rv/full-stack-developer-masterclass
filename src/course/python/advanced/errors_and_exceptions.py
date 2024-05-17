def divider(a: int, b: int) -> float:
    try:
        result = a/b
    except ZeroDivisionError:
        print("Please do not divide by zero!")
    else:
        print(f"The result is {result}")
        return result



divider(1, 0) # Please do not divide by zero!
divider(1, 2)  # 0.5

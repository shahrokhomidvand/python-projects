num1 = float(input("عدد اول را وارد کنيد: "))
num2 = float(input("عدد دوم را وارد کنيد: "))
operation = input("عمليات ( + - * / )را انتخاب کنيد: ")


if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 !=0:
        result = num1 / num2
    else:
        result = None
        print("Error:تقسيم بر صفر امکان پذير نيست")
else:
    print("Error:عمليات نامعتبر است")
# Display the result
if result is not None:
    print(f"result: {result}")


        

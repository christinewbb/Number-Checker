def check_number():
    integers = int(input("Lapag ka random number: "))
    
    if integers == 0:
        print("The number you input is zero.")
    elif integers %2 == 0:
        print("The number you input is even number.")
    else:
        print("The number you input is odd number.")
        
check_number() 
largest = None
smallest = None
list_of_numbers = []
while True:
    try :
        num = input("Enter a number: ")
        if num == "done":
            break
        num = int(num)
    except:
        print("Invalid input")
        continue
    if num == "done":
        break
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num
print("Maximum is", largest)
print("Minimus is", smallest)
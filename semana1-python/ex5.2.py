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
    list_of_numbers.append(num)
largest = max(list_of_numbers)
smallest = min(list_of_numbers)
print("Maximum", largest)
print("Minimum", smallest)
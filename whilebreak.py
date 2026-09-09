pin = "0931"
attemps = 0
while attemps < 5:
    enter = input("ENTER PIN: ")
    enter == pin
    if enter == pin:
        print("ACCESS GRANTED")
        break
    print("TRY AGAIN")
    attemps = attemps + 1


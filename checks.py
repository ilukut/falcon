run = 0
while run <3:
    try:


        temp = int(input("Enter the temperature:"))

        def temperature(temp):
            if temp < 32:
                print("cold")
            elif temp == 32:
                print("Normal")
            else:
                print("hot")

        temperature(temp)
        run+=1

    except:
        print("Invalid entry")
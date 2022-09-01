'''Registration form'''

import random
import string

output_list = []
for j in range(0, 1):
    number_list = []

    # Not sign, not numbers only contain Alphabates
    while True:
        item1 = input("Enter the Learner Name: ")
        if item1.isalpha() == True:
            name = True
            print("Hello", item1.capitalize())
            break
        else:
            print("\nPlease enter the correct detail, please try again.\n")

    # Valid Date
    # Date should be today or after the today's date
    import datetime as dt
    def input_validation(item2):
        while True:
            try:
                dt.datetime.strptime(item2, '%Y/%m/%d')
                break
            except ValueError:
                print("\nSorry, this does not appear to be valid date Format, YYYY/MM/DD")
                item2 = input_validation(input("Enter the Joining date that you want to join in format YYYY/MM/DD:"))
                break
        return item2
    item2 = input_validation(input("Enter the Joining date in format YYYY/MM/DD:"))
    print("The date you entered is:", item2)

    # If experienced then how much
    # Store item31 in the number_list 
    while True:
        item3 = input("Are you Fresher or Experienced?")
        if item3 == ("Fresher"):
            print(item1.capitalize() + " " + "is Fresher")
            break
        elif item3 =="Experienced":
            print(item1.capitalize() +" "+ "is Experienced")
            while True:
                # print(item1.capitalize() +" "+ "is Experienced")
                item31 = input("Enter the Experience do you have (in months): ")
                if item31.isdigit() == True:
                    print("You have great Experience!!")
                    break
                else:
                    print("\nPlease enter the correct detail!\n")
                    print("The enter detail should be in months, please try again.")
            break
        else:
            print("please write the Fresher or Experienced Accordingly")

    # Valid Duration time
    while True:
        item4 = input("Enter the Duration of Learning that you want (in months): ")
        if item4.isdigit() == True:
            print("You want to join for", item4, "month. Great!!")
            break
        else:
            print("\nPlease enter the correct detail!\n")
            print("The enter detail should be in months, please try again.")

    # Available Dance Form list
    while True:
        item5 = input("Enter the Type of Dance which you want: ")
        if item5 == "Khatak":
            print("You want to learn the Dance form", item5.capitalize())
            break
        elif item5 == "Hiphop":
            print("You want to learn the Dance form", item5.capitalize())
            break
        elif item5 == "Western":
            print("You want to learn the Dance form", item5.capitalize())
            break
        elif item5 == "Bharatnatyam":
            print("You want to learn the Dance form", item5.capitalize())
            break
        elif item5 == "Kucipudi":
            print("You want to learn the Dance form", item5.capitalize())
            break
        elif item5 == "Freestyle":
            # name = True
            print("You want to learn the Dance form", item5.capitalize())
            break
        elif item5 == "Salsa":
            # name = True
            print("You want to learn the Dance form", item5.capitalize())
            break
        elif item5 == "RajasthaniFolk":
            # name = True
            print("You want to learn the Dance form", item5.capitalize())
            break
        else:
            print("Our Acedmy teaches the dance forms :")
            print("\nKhatak \nHiphop \nWestern \nBharatnatyam ")
            print("Kucipudi \nFreestyle \nSalsa \nRajasthaniFolk")
            print("\nSorry, We don't have the dance form ", item5 )
            print("\nplease Enter the Dance Form from the list: ")

    # Generted Unique Id

    def ran_gen(size, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))
    item6 = ran_gen(8, "ABCDEF1234")
    print ("Your User ID is:" , item6)

    number_list.append(item1)
    number_list.append(item2)
    number_list.append(item3)
    ## number_list.append(item31)
    number_list.append(item4)
    number_list.append(item5)
    number_list.append(item6)

    print(number_list)

    output_list.append(number_list)

# Show entries 

# Store date in file
with open('text.txt', 'a') as fp:
    for item in output_list:
        fp.write("%s\n" % item)

# Show the File Data //Show Entries
while True:
    show_content = input("Are you want to read The content of the file?(please enter Yes or No Accordingly)")
    if show_content == "Yes":
        with open('text.txt') as f:
            file_content = f.read()
            print(file_content)
            break
    elif show_content =="No":
        print("Thanks For Answering")
        break
    else:
        print("\nPlease enter the one Value 'Yes' or 'No'!\n")

# Show Only name or Date Of Join
# def Convert(number_list):
#     res_dct = {number_list[i]: number_list[i + 1] for i in range(0, len(number_list))}
#     return res_dct

# print(Convert(number_list))


# Show Specific Details
# Dictionary
# Key = ID, Value = number_list
# list_Dict ={


# }


# Filter Entries

# type of dance
# Expired entries
# Duration
# Current entries
# New entries
 
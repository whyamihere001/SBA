#26/3/24 started working on this, created the file, did a little bit research
#17/4 research (used AI)
#18/4 research, found some useful libraries (used AI)
#19/4 research, started ACTUALLY coding
#*IMPORTANT* I ONLY USED AI FOR RESEARCH I DID NOT COPY AND PASTE
#25/4 created the menu() fuction, not finished (definetly), but the base of it
#26/4 developing the function add_guest()
#28/4 what the fuck am i doing
#10/5 yk what? json is stupid
#11/5 i am too tired but remember, tmr i would fix the print guest function and make the load_json function

import json

guests = []
def check_name(name):
    while True:
        if name.strip() == "":
            print("name cannot be empty. Please try again, or type 'back' to go back to main menu")
            name = input("pls enter your name again: ")
        elif name.lower() == "back":
                menu()
                return None
        else:
                return name
        
def check_phone(phone_no):
    while True:
        if phone_no.isdigit() == False or len(phone_no) != 8:
            print("invalid phone number. Pls try again, or enter 'back' to go back to menu")
        else:
            return phone_no
        
        print("Please try again, or enter 'back' to return to the main menu.")
        phone_no = input("Enter your phone number again: ").strip()
        if phone_no.lower() == "back":
            menu()
            return None
        
def phone_exists(phone_no):
    for g in guests:
        if g["phone_number"] == phone_no:
            return True
    return False

def print_guest(guest_info):
    for guest_info in guests:
        print("name:", guest_info["name"])
        print("phone number:", guest_info["phone_number"])
        print("seats required:", guest_info["seats_required"])
        print("other guests:", guest_info["other_guests"])                
           
def save(data, file_name):
    file = open(file_name, "w")
    json.dump(data, file)
    file.close()

def load_json()

def add_guest():
    
        name = input("what is your name: ")
        name = check_name(name)
        
        while True:
            phone_no = input("please type in your phone number: ").strip()
            phone_no = check_phone(phone_no)
            if phone_no is None:
                return

            if phone_exists(phone_no) == True:
                print("phone number cannot duplicate. This phone number already registered. Please try again")
                continue

            
            #in case you cant see it, ckc, phone number is the "primary key" for this mini dictionary "database""
                    
            guest_info = {
                        "name": name,
                        "phone_number": phone_no,
                        "seats_required": 1,  
                        "other_guests": []
                    }
            
            guests.append(guest_info)
            print("these are guests info that are currently registered: ")

            print_guest(guest_info)
            
            finished = input("add another guest? type 'done' if you are finished: ")
            if finished.lower() == "done":
                print("exiting...")
                break
            else:
                while True:
                    name = input("pls enter the name: ")
                    name = check_name(name)

                    for g in guests: # yes, i know this part is weird, why do i have to define another dictionary "g"?
                        if g["phone_number"] == phone_no: #this to loop through guests[] until it get to the guy with the specific phone number (loop until find the primary key)
                            g["seats_required"] = g["seats_required"] + 1 #to prevent users from entering invalid stuff, I would count the seats for them
                            g["other_guests"].append(name) #this just to add the name to the other_guest[] under the name of the required main guest in guest_info
                    
                    print("this is the current guest list:")
                    print_guest(guest_info)

                    finished = input("add more guests? type 'done' if finished")
                    if finished.lower() == "done":
                        print("exiting...")
                        menu()
                        return
                    else:
                        continue
        file = open("guests.json", "r") #remember, file must be OPENED before loading the data inside it and printing it
        saved = json.load(file)
        file.close()

        print(saved)

def remove_main_guest():
    while True:
        phone_no = input("pls input the phone number of main guest that you want to remove: ")
        phone_no = check_phone(phone_no)
        if phone_no is None:
            menu()
            return
        elif phone_exists(phone_no) == False:
            print("no guest is registered under this phone number. Pls Try again.")
            continue
        else:
            confirm = input("are you sure you want to remove this main guest? That means removing every other guests under the name of this main guest. (Y/N)").strip()
            if confirm.upper() == "Y":
                guests.remove()
        

def remove_other_guest():
    phone_no = input("pls input the phone number of main guest: ")
    check_phone(phone_no)
    if phone_no is None:
        menu()
        return

def remove_guest():
    while True:
        print("these are the guests that are currently registered: ")
        print_guest(guest_info)
        
        guest_type = input("press 1 if you want to remove main guest(s)\npress 2 if you want to remove other guest(s)\nor enter 'back' to go back to main menu\n")
        if guest_type.lower() == "back":
            menu()
            return
        elif guest_type == "1":
            remove_main_guest()
        elif guest_type == "2":
            remove_other_guest()
        else:
            print("invalid input.")
            continue        

                                                         
def menu(): #IMPORTANT!!!!!!!!!    
    while True:
        print("Welcome to Tl dinner. Please type in the corresponding number to the funcions")
        print("1 -add guests ")
        print("2 -remove guest s")
        print("3 -generate/ read the seating plan: ") 
        print("4 -remove guest by phone number")
        print("5 -exit ")
        guest_input = (input("please type in the number: ")).strip()
        if guest_input.isdigit() == False: #for fxxk's sake......... pls remember isdigit()
            print("please enter an integer")
        else:
            guest_input = int(guest_input)
            if guest_input > 4 or guest_input < 1:
                print("invalid. Please enter a number between 1 and 4")
            elif guest_input == 1:
                add_guest()
            elif guest_input == 2:
                remove_guest()
            elif guest_input == 3:
                print("generate seating plan")
            elif guest_input == 4:
                print("finding guest")
            else:
                print("are you sure you want to leave (Y/N)")
                confirmation = input()
                if confirmation.upper() == "Y":
                    break
    return
menu()

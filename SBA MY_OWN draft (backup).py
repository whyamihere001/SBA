#26/3/24 started working on this, created the file, did a little bit research
#17/4 research (used AI)
#18/4 research, found some useful libraries (used AI)
#19/4 research, started ACTUALLY coding
#*IMPORTANT* I ONLY USED AI FOR RESEARCH I DID NOT COPY AND PASTE
#25/4 created the menu() fuction, not finished (definetly), but the base of it
#26/4 developing the function add_guest()
#28/4 what the hell am i doing
#the long 5 day holiday... Ive actually finished the add_guest function. Really much work to do
#10/5 yk what? json is stupid
#11/5 i am too tired but remember, tmr i would fix the print guest function and make the load_json function
#11/5 I woke up and still have no idea how to fix the print guest function. Might not even need it anymore.
# DUDE I learnt about python dictionary and how to add/delete/append/check data just for this SBA. So yea, CKC, thats why this is more than 200 lines.
#I learnt dictionary by AI, but I did the code myself. Really.
import json #yea i needed to save in json. CSV wouldnt work because it is in text form. Well technically it COULD work but i need to split it and re-format it back into dictionary and lists so its too much work. 
import os

guests = [] #this is the big guest list

#IMPORTANT!! THIS IS THE ONLY PART OF MY CODE THAT DIRECTLY COMES FROM CHATGPT I DECLARE IT HERE (MAY FIX LATER)
def load_json(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            content = f.read().strip()
        if not content:
            # File is empty
            with open(filename, "w") as f:
                f.write("[]")
            return []
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            # File is corrupted or not valid JSON
            with open(filename, "w") as f:
                f.write("[]")
            return []
    else:
        # File does not exist
        with open(filename, "w") as f:
            f.write("[]")
        return []

def save_json(data, file_name):
    file = open(file_name, "w")
    json.dump(data, file) #appearently, json is a library, and its similar to those teached in elective C chapter 7
    file.close()
        
guests = load_json("guests.json")
table = load_json("table.json")
fuck1 = load_json("fuck1.json")

if table is None:
    table = []

if guests is None:
    guests = []

if fuck1 is None:
    fuck1 = []

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
            return None #yea I should have make a True/ False tag here but i am too lazy to change it
        
def phone_exists(phone_no):
    for g in guests:
        if g["phone_number"] == phone_no:
            return True
    return False #else: return False no work. It returns False everytime unless the phone no thats duplicated exists at the last index of the array.


def print_guest(guests):
    for g in guests:
        print("name:", g["name"])
        print("phone number:", g["phone_number"])
        print("graduation year", g["graduation_year"])
        print("seats required:", g["seats_required"])
        print("other guests:", g["other_guests"])
        print("----------------------------")                


#ok load_json and save_json I got the idea from chatgpt. Did not exactly copy and paste, but I learnt how to use it and got the main idea from chatgpt

def save_txt(data, file_name):
    file = open(file_name, "w")
    file.write(str(data) + "\n")
    file.close()

def load_txt(file_name):
    file_exists = os.path.exists(file_name)
    if file_exists == True:
        saved_guest_file = open(file_name, "r")
        saved_guest_file.close()
        
    else:
        print("no guest saved .txt file found. Do you want to register now?")
        return []



def add_guest():
    global guests
    guests = load_json("guests.json")

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

        while True: #too annoying to refactor something that I would only use once. this is not a primary key.
            grad_year = input("what is your graduation year? ").strip()

            if grad_year.isdigit() == False:
                print("invalid input. Graduation year must be a number. ")
                continue
            else:
                grad_year = int(grad_year)
                if grad_year < 1973 or grad_year > 2025:
                    print("the graduation year must be between 1973 and 2025. ")
                    continue
                else:
                    break 


            
        #in case you cant see it, ckc, phone number is the "primary key" for this mini dictionary "database"
                    
        guest_info = {
                    "name": name,
                    "phone_number": phone_no,
                    "graduation_year": grad_year,
                    "seats_required": 1,  
                    "other_guests": []
                }
            
        guests.append(guest_info)
        print("these are guests info that are currently registered: ")

        print_guest(guests)
            
        finished = input("add another guest? type 'done' if you are finished: ")
        if finished.lower() == "done":
            save_json(guests, "guests.json")
            save_txt(guests, "guests.txt")
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
                print_guest(guests)

                finished = input("add more other guests? type 'done' if finished ")
                if finished.lower() == "done":
                    save_json(guests, "guests.json")
                    save_txt(guests, "guests.txt")
                    print("exiting...")
                    menu()
                    return
                else:
                    continue
    save_json(guests, "guests.json")
    save_txt(guests, "guests.txt")


def remove_main_guest():
    while True:
        global guests
        guests = load_json("guests.json")
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
                for g in guests:
                    if phone_no == g["phone_number"]:
                        guests.remove(g)
                save_txt(guests, "guests.txt")
                save_json(guests, "guests.json")
                return
            else:
                continue
        

def remove_other_guest():
    while True:
        global guests
        guests = load_json("guests.json")
        phone_no = input("pls input the phone number of main guest: ")
        check_phone(phone_no)
        if phone_no is None:
            menu()
            return
        elif phone_exists(phone_no) == False:
            print("there is no main guests registered under this phone number. Please Try again. ")
            continue
        else:
            other_guest = input("please enter the name of the other guest you want to remove: ")
            for g in guests:
                if phone_no == g["phone_number"]:
                    if other_guest in g["other_guests"]: #check is other_guest is in other_guest[]
                        g["other_guests"].remove(other_guest)
                    else:
                        print("guest named", other_guest, "doesnt exist, please try again")
                        continue
                    g["seats_required"] = g["seats_required"] - 1
                    print("successfully removed the other guest")
                    print(guests)
                    save_txt(guests, "guests.txt")
                    save_json(guests, "guests.json")
                    menu()


def remove_guest():
    while True:
        print("these are the guests that are currently registered: ")
        guests_registered = load_json("guests.json")
        print(guests_registered)
        guest_type = input("press 1 if you want to remove main guest(s)\npress 2 if you want to remove other guest(s)\nor enter 'back' to go back to main menu\n")
        if guest_type.lower() == "back":
            menu()
            return
        elif guest_type == "1":
            remove_main_guest()
            return
        elif guest_type == "2":
            remove_other_guest()
            return
        else:
            print("invalid input. please enter either 1 or 2.")
            continue        

def seating_plan_generate():
    guests = load_json("guests.json")
    small_table = load_json("small_table.json")
    large_table = load_json("large_table.json")
    group_size = []
    for g in guests:
        group_size.append(g["seats_required"])
        print(group_size)
    small_table = {
        "min_size": 4,
        "max_size": 6,
        "table_guests": []

    }
    large_table = {
        "min_size": 10,
        "max_size": 12,
        "table_guests": []
    }
    for i in range(0, len(group_size)):
        if group_size[i] >= 1:
            large_table["table_guests"].append(guests["main_guest"]) #for testing
            large_table["table_guests"].append(guests["other_guest"])
            save_json("table.json")

        

def menu(): #IMPORTANT!!!!!!!!!    
    while True:
        print("Welcome to Tl dinner. Please type in the corresponding number to the funcions")
        print("1 -add guests ")
        print("2 -remove guest s")
        print("3 -generate/ read the seating plan: ") 
        print("4 -search guest by phone number")
        print("5 -exit ")
        guest_input = (input("please type in the number: ")).strip()
        if guest_input.isdigit() == False: #for fxxk's sake......... pls remember isdigit()
            print("please enter an integer")
            continue
        else:
            guest_input = int(guest_input)
            if guest_input > 4 or guest_input < 1:
                print("invalid. Please enter a number between 1 and 4")
                continue
            elif guest_input == 1:
                add_guest()
            elif guest_input == 2:
                remove_guest()
            elif guest_input == 3:
                seating_plan_generate()
            elif guest_input == 4:
                print("finding guest")
            else:
                print("are you sure you want to leave (Y/N)")
                confirmation = input()
                if confirmation.upper() == "Y":
                    break
    return
menu()

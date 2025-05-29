#26/3/24 started working on this, created the file, did a little bit research
#17/4 research (used AI)
#18/4 research, found some useful libraries (used AI)
#19/4 research, started ACTUALLY coding
#*IMPORTANT* I ONLY USED AI FOR RESEARCH I DID NOT COPY AND PASTE
#25/4 created the menu() fuction, not finished (definetly), but the base of it
#26/4 developing the function add_main_guest()
#28/4 what the hell am i doing
#the long 5 day holiday... Ive actually finished the add_main_guest function. Really much work to do
#10/5 yk what? json is stupid
#11/5 i am too tired but remember, tmr i would fix the print guest function and make the load_json function
#11/5 I woke up and still have no idea how to fix the print guest function. Might not even need it anymore.
# DUDE I learnt about python dictionary and how to add/delete/append/check data just for this SBA. So yea, CKC, thats why this is more than 500 lines.
#I learnt dictionary by AI, but I did the code myself. Really.
import json #yea i needed to save in json. CSV wouldnt work because it is in text form. Well technically it COULD work but i need to split it and re-format it back into dictionary and lists so its too much work. 
import os

venue_cap = 500

#IMPORTANT!! THIS IS THE ONLY PART OF MY CODE THAT DIRECTLY COMES FROM CHATGPT I DECLARE IT HERE (MAY FIX LATER)
def load_json(filename, default=None):
    """Loads JSON from file, if fails returns default (dict or list)."""
    if default is None:
        default = {}  # Default to dict if not specified

    if os.path.exists(filename):
        with open(filename, "r") as f:
            content = f.read().strip()
        if not content:
            # File is empty
            with open(filename, "w") as f:
                f.write(json.dumps(default))
            return default
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            # File is corrupted or not valid JSON
            with open(filename, "w") as f:
                f.write(json.dumps(default))
            return default
    else:
        # File does not exist
        with open(filename, "w") as f:
            f.write(json.dumps(default))
        return default

def save_json(data, file_name):
    file = open(file_name, "w")
    json.dump(data, file) #appearently, json is a library, and its similar to those teached in elective C chapter 7
    file.close()
        
guests = load_json("guests.json", default={})
tables = load_json("tables.json", default=[])

if tables is None:
    tables = []

if guests is None:
    guests = {}

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
    global guests
    if phone_no in guests:
        return True
    else:
        return False
    

def print_guest(guests):
    for phone_no in guests:
        print("name: ", guests[phone_no]["name"])
        print("phone number: ", phone_no)
        print("graduation year: ", guests[phone_no]["graduation_year"])
        print("seats required: ", guests[phone_no]["seats_required"])
        print("other guests: ", guests[phone_no]["other_guests"])
        print("table type: ", guests[phone_no]["table_type"])
        print("table id: ", guests[phone_no]["table_id"])
        print("--------------------------------------------------------------------------")

def print_tables(tables):
    table_id = 1
    for table_id in range(0, len(tables)):
        print("table id: ", table_id)
        print("table_type: ", tables[table_id]["type"]) 
        print("seats occupied: ", tables[table_id]["seats_occupied"])
        print("main guests seated", tables[table_id]["guests_seated"]["main_guests"])
        print("graduation year of main guest: ", tables[table_id]["guests_seated"]["grad_year"])
        print("other guests seated: ", tables[table_id]["guests_seated"]["other_guests"])
        print("--------------------------------------------------------------------------")

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

def count_seats():
    global guests
    current_amount = 0
    guests = load_json("guests.json", default={})
    for phone_no in guests:
        current_amount = current_amount + guests[phone_no]["seats_required"]
    return current_amount

def add_main_guest():
    global guests
    guests = load_json("guests.json", default={})

    name = input("what is your name: ")
    name = check_name(name)
        
    while True:
        if count_seats() > venue_cap:
            print("sorry, the venue is at its maximum")
            menu()
            return
        else:
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
                        
            guest_info = {   #guest_info is a dummy variable for temperary use
                "name": name,
                "graduation_year": grad_year,
                "seats_required": 1,
                "other_guests": [],
                "table_type": None,
                "table_id": None
            }
                
            guests[phone_no] = guest_info
            print("These are the guests currently registered:")
            print_guest(guests)       
                
            finished = input("add another guest? type 'done' if you are finished: ")
            if finished.lower() == "done":
                save_json(guests, "guests.json")
                save_txt(guests, "guests.txt")
                print("exiting...")
                break
            elif count_seats() >= venue_cap:
                save_json(guests, "guests.json")
                save_txt(guests, "guests.txt")
                print("sorry, the venue is at its maximum.")
                menu()
            else:
                add_other_guest()

        save_json(guests, "guests.json")
        save_txt(guests, "guests.txt")

def add_other_guest():
    global guests
    guests = load_json("guests.json", default={})

    while True:
        if count_seats() >= venue_cap:
            save_json(guests, "guests.json")
            save_txt(guests, "guests.txt")
            print("sorry, venue is at its maximum.")
            menu()
            return
        other_guests_name = input("pls enter the name: ")
        other_guests_name = check_name(other_guests_name)
        while True:
            phone_no = input("please input the phone number of the main guest that brings in the other guest")

            if phone_no in guests:
                guests[phone_no]["other_guests"].append(other_guests_name)
                guests[phone_no]["seats_required"] = guests[phone_no]["seats_required"] + 1
                break
            else:
                print("main guest with that phone number does not exist")
        finished = input("add more other guests? type 'done' if finished ")
        if finished.lower() == "done":
            save_json(guests, "guests.json")
            save_txt(guests, "guests.txt")
            print("exiting...")
            menu()
            return
        
        else:                
            continue

def add_guest():
    global guests
    while True:
        print("Enter 1 if you want to add another main guest")
        print("Enter 2 if you want to add another other guest")
        print("Enter 'back' if you want to go back to main menu")
        pick = input("please enter the number: ")
        if pick.lower() == "back":
            print("going back to main menu...")
            menu()
            return
        elif pick == "1":
            add_main_guest()
            return
        elif pick == "2":
            add_other_guest()
            return
        else:
            print("invalid. Please input a valid number")
            continue

def remove_main_guest():
    global guests
    guests = load_json("guests.json", default={})
    while True:
        phone_no = input("pls input the phone number of main guest that you want to remove: ")
        phone_no = check_phone(phone_no)
        if phone_no is None:
            menu()
            return
        elif phone_exists(phone_no) == False:
            print("no guest is registered under this phone number. Please Try again.")
            continue
        else:
            confirm = input("are you sure you want to remove this main guest? That means removing every other guests under the name of this main guest. (Y/N)").strip()
            if confirm.upper() == "Y":
                del guests[phone_no] #deletes the main guest by the phone_no, O(1) (constant) access time
                save_json(guests, "guests.json")
                save_txt(guests, "guests.txt")
            else:
                continue
        

def remove_other_guest():
    global guests
    while True:
        global guests
        guests = load_json("guests.json", default={})
        phone_no = input("pls input the phone number of main guest: ")
        check_phone(phone_no)
        if phone_no is None:
            menu()
            return
        elif phone_exists(phone_no) == False:
            print("there is no main guests registered under this phone number. Please Try again. ")
            continue
        else:
            while True:
                other_guests = input("please enter the name of the other guest you want to remove: ")
                other_guests = check_name(other_guests)
                if phone_no in guests:
                        if other_guests in guests[phone_no]["other_guests"]:
                            guests[phone_no]["other_guests"].remove(other_guests)
                            guests[phone_no]["seats_required"] = guests[phone_no]["seats_required"] - 1
                            save_json(guests, "guests.json")
                            save_txt(guests, "guests.txt")
                            menu()
                            return
                        else:
                            print("the other guest you entered does not exist. Please try again")
                            continue
                            



def remove_guest():
    global guests
    while True:
        print("these are the guests that are currently registered: ")
        guests = load_json("guests.json", default={})
        print_guest(guests)
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
    global guests
    global tables
    table_id = 0
    guests = load_json("guests.json", default={})
    tables = load_json("tables.json", default=[])
    table_id = 0
    remaining = count_seats()
    small_max = 6
    big_max = 12

    guests_group_sizes = []

    for guest in guests:
        guests_group_sizes.append(guests[guest]["seats_required"])
    guests_group_sizes = sorted(guests_group_sizes)
    print(guests_group_sizes)

    guests = dict(sorted(guests.items(), key=lambda x: x[1]["graduation_year"])) #sort the guests{} by graduation year so that I could assign tables for them by graduation year
    save_json(guests, "guests.json")
    for g in guests:
        assigned = 0
        remaining = guests[g]["seats_required"]
        all_guests = [guests[g]["name"]] + guests[g]["other_guests"]
        while remaining > 0:
            if len(all_guests) > big_max:
                current_table = {
                            "table_id": table_id,
                            "type": "big",
                            "max": big_max,
                            "seats_occupied": 0,
                            "guests_seated": {
                                "main_guests": [],
                                "grad_year": [],
                                "other_guests": []
                    }    
                }
                current_table["guests_seated"]["main_guests"].append(all_guests[0])
                current_table["guests_seated"]["grad_year"].append(guests[g]["graduation_year"])
                current_table["seats_occupied"] = current_table["seats_occupied"] + 1
                remaining = remaining - 1
                for i in range(1, min(big_max, len(all_guests))):
                    if i < len(all_guests):
                        current_table["guests_seated"]["other_guests"].append(all_guests[i])
                        current_table["seats_occupied"] = current_table["seats_occupied"] + 1
                        assigned = assigned + 1
                        remaining = remaining - 1
                tables.append(current_table)

                if remaining >= 7: #if remaining cannot fit in small table, give them another big table
                    table_id = table_id + 1
                    current_table = {
                            "table_id": table_id,
                            "type": "big",
                            "max": big_max,
                            "seats_occupied": 0,
                            "guests_seated": {
                                "main_guests": [],
                                "grad_year": [],
                                "other_guests": []
                    }    
                }
                    for i in range(assigned, min(assigned+big_max, len(all_guests))):
                        current_table["guests_seated"]["other_guests"].append(all_guests[i])
                        current_table["seats_occupied"] = current_table["seats_occupied"] + 1
                        remaining = remaining - 1
                    assigned = i + 1
                    tables.append(current_table)

                else: #if remaining can fit in a small table, give them another small table
                    table_id = table_id + 1
                    current_table = {
                            "table_id": table_id,
                            "type": "small",
                            "max": small_max,
                            "seats_occupied": 0,
                            "guests_seated": {
                                "main_guests": [],
                                "grad_year": [],
                                "other_guests": []
                    }    
                }  
                    for i in range(assigned, min(assigned+small_max, len(all_guests))):
                        current_table["guests_seated"]["other_guests"].append(all_guests[i])
                        current_table["seats_occupied"] = current_table["seats_occupied"] + 1
                        remaining = remaining - 1
                    assigned = i + 1
                    tables.append(current_table)

            else:
                    
                current_seated = 0
                if remaining + current_seated > small_max:
                    table_id = table_id + 1
                    current_table = {
                            "table_id": table_id,
                            "type": "small",
                            "max": small_max,
                            "seats_occupied": 0,
                            "guests_seated": {
                                "main_guests": [],
                                "grad_year": [],
                                "other_guests": []
                    }
                }   
                    current_table["guests_seated"]["main_guests"].append(guests[g]["name"])
                    for i in range(0, len(all_guests)):
                        current_table["guests_seated"]["other_guests"].append(all_guests[i])
                        current_table["seats_occupied"] = current_table["seats_occupied"] + 1
                        remaining = remaining - 1
                    tables.append(current_table)

                else:
                    while assigned < len(all_guests):
                        current_table = {
                            "table_id": table_id,
                            "type": "small",
                            "max": small_max,
                            "seats_occupied": 0,
                            "guests_seated": {
                                "main_guests": [],
                                "grad_year": [],
                                "other_guests": []
                            }
                        }
                        current_table["guests_seated"]["main_guests"].append(guests[g]["name"])
                        for i in range(assigned + 1, len(all_guests)):
                            current_table["guests_seated"]["other_guests"].append(all_guests[i])
                            current_table["seats_occupied"] = current_table["seats_occupied"] + 1
                            remaining = remaining - 1
                        assigned = assigned + small_max
                        tables.append(current_table)
    print_tables(tables)
    save_json(tables, "tables.json")
    save_txt(tables, "tables.txt")                                                                               

def search_guest():
    global guests
    guests = load_json("guests.json", default={})
    phone_no = input("please input your phone number")
    phone_no = check_phone(phone_no)
    while True:
        if phone_no in guests:   #O(1) time complexity
            print(guests[phone_no]["name"])
            print(guests[phone_no]["graduation_year"])
            print(guests[phone_no]["seats_required"])
            print(guests[phone_no]["other_guests"])
            phone_no = input("would you like to search for another guest using phone number? input the phone number or enter 'back' to go back to main menu: ")
            if phone_no.lower() == "back":
                menu()
                return
            else:
                phone_no = check_phone(phone_no)
                continue
        else:
            phone_no = input("no guest is registered under this phone number, please enter another phone number or type 'back' to go back to main menu: ")
            if phone_no.lower() == "back":
                menu()
                return
            else:
                phone_no = check_phone(phone_no)
                continue
            

def menu(): #IMPORTANT!!!!!!!!!
    global guests
    global tables
    guests = load_json("guests.json", default={})
    tables = load_json("tables.json", default=[])    
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
            if guest_input > 5 or guest_input < 1:
                print("invalid. Please enter a number between 1 and 4")
                continue
            elif guest_input == 1:
                add_guest()
            elif guest_input == 2:
                remove_guest()
            elif guest_input == 3:
                seating_plan_generate()
            elif guest_input == 4:
                search_guest()
            else:
                print("are you sure you want to leave (Y/N)")
                confirmation = input()
                if confirmation.upper() == "Y":
                    break
    return
menu()

def load_json(file_name):
    file_exists = os.path.exists(file_name)
    if file_exists == True:
        saved_guest_file = open(file_name, "r")
        saved_data = json.load(saved_guest_file)
        saved_guest_file.close()
        return(saved_data)
    elif not saved_guest_file:
        saved_guest_file = open(file_name, "w")
        saved_guest_file.write("[]")
        saved_guest_file.close()
        return []    
    else:
        print("no guests saved file found. Do you want to register now?")
        return []
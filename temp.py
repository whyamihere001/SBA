def seating_plan_generate():
    guests = load_json("guests.json", default={})
    tables = load_json("tables.json", default=[])
    table_id = 0

    for table_id in range(0, 80):

        small_table = {
            "table_id": table_id,
            "type": "small",
            "min": 4,
            "max": 6,
            "seats_occupied": 0,
            "guests_seated": {
                "main_guests": [],
                "other_guests": []
            }    
        }

        tables.append(small_table)
        table_id = table_id + 1

    guests_remaining = count_seats()

    while guests_remaining > 0:
        for g in guests: #g is a key
            for t in tables:      #t is a dict

                if guests[g]["seats_required"] <= t["max"]:
                    t["guests_seated"]["main_guests"].append(g)
                    t["seats_occupied"] = t["seats_occupied"] + 1
                    if guests[g]["seats_required"] > 1:
                        while t["seats_occupied"] < t["max"]:
                            t["guests_seated"]["other_guests"].extend(guests[g]["other_guests"])
                            t["seats_occupied"] = t["seats_occupied"] + guests[g]["seats_required"] - 1
                            
                    else:
                        t["seats_occupied"] = t["seats_occupied"] + 1
                        t = t + 1
                    
                break
            guests_remaining = guests_remaining - t["seats_occupied"]
            break
            
                    

            
    save_json(tables, "tables.json")
    save_txt(tables, "tables.txt")

                if (group_size + tables[table_id]["seats_required"]) <= small_max:
                tables[table_id]["guests_seated"]["main_guests"].append(g)
                tables[table_id]["seats_required"] = tables[table_id]["seats_required"] + 1
                if guests[g]["seats_required"] > 1:
                    tables[table_id]["guests_seated"]["other_guests"].extend(guests[g]["other_guests"])
                    tables[table_id]["seats_required"] = tables[table_id]["seats_required"] + 1
                table_id = table_id + 1
                print(table_id)
                remaining = remaining - guests[g]["seats_required"]
                print(remaining)
                save_json(tables, "tables.json")
                continue
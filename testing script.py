import json
import random

first_names = [
    "Alex", "Jamie", "Taylor", "Jordan", "Morgan", "Casey", "Riley", "Sam", "Drew", "Avery",
    "Chris", "Pat", "Jesse", "Blake", "Robin", "Skyler", "Quinn", "Cameron", "Dana", "Emerson"
]
last_names = [
    "Smith", "Lee", "Brown", "Chen", "Wong", "Chan", "Patel", "Ng", "Lam", "Ho", "Garcia", "Kim",
    "Tran", "Park", "Singh", "Lopez", "Khan", "Li", "Tan", "Wong"
]

def random_name():
    return random.choice(first_names) + " " + random.choice(last_names)

guests = {}
used_phones = set()
total_seats = 0
TARGET_SEATS = 200
guest_index = 1

while total_seats < TARGET_SEATS:
    # Unique phone number
    while True:
        phone = str(random.randint(10000000, 99999999))
        if phone not in used_phones:
            used_phones.add(phone)
            break

    name = random_name()
    grad_year = random.randint(1973, 2025)
    # Choose how many other guests for this main guest
    max_other_guests = min(4, TARGET_SEATS - total_seats - 1)  # -1 for main guest
    num_other_guests = random.randint(0, max_other_guests)
    other_guests = [random_name() for _ in range(num_other_guests)]
    seats_required = 1 + num_other_guests

    guests[phone] = {
        "name": name,
        "graduation_year": grad_year,
        "seats_required": seats_required,
        "other_guests": other_guests
    }

    total_seats += seats_required
    guest_index += 1

print(f"Total seats generated: {total_seats}. Total main guests: {len(guests)}")

with open("guests.json", "w") as f:
    json.dump(guests, f, indent=2)

print("Generated guests.json with total seats exactly 200.")
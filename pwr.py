# Input function
def data():
    global name, appliance, power, hours, day

    name = input("Enter the student's name: ")
    appliance = input("Enter the appliance name: ")
    power = int(input("Enter the power drawn: "))
    hours = int(input("How many hours is it used for: "))
    day = int(input("For how many days: "))


# Total Energy used
def energy(power, hours, day):
    global total_energy
    total_energy = (power * hours * day) / 1000
    print(f"Total Energy used = {total_energy} kWh")


# Total Energy Cost
def price(total_energy):
    global total_cost
    total_cost = total_energy * 25
    print(f"Total Cost = {total_cost} KES")


# Global list to store all users
info = []

# Storage
def store(name, appliance, power, total_energy, total_cost):
    global info
    new_user = {
        "name": name,
        "appliance": appliance,
        "power": power,
        "energy": total_energy,
        "cost": total_cost
    }
    info.append(new_user)


# Terminal table
def table():
    global info
    if not info:
        print("\nError: No user data found!")
        print("Please add at least 1 user via option 1 before viewing results.\n")
        return
    
    # Sort users by cost (highest to lowest)
    sorted_info = sorted(info, key=lambda x: x['cost'], reverse=True)
    
    header = f"| {'Rank':<6} | {'Name':<15} | {'Appliance':<15} | {'Energy (kWh)':<12} | {'Cost (KES)':<12} |"
    print("\n" + header)
    ln_break = len(header)
    print("-" * ln_break)
    
    # Display all users with ranking
    for rank, user in enumerate(sorted_info, start=1):
        row = f"| {rank:<6} | {user['name']:<15} | {user['appliance']:<15} | {user['energy']:<12.2f} | {user['cost']:<12.2f} |"
        print(row)
    
    print("-" * ln_break + "\n")


# Terminal CLI
while True:
    task = input(
        "Power Usage and Cost Calculator \n\n What would you like to do? \n 1. Calculate total energy and cost \n 2. Show all results \n 3. Quit \n\n"
    )

    if task == "1":
        data()  # Call data() first to initialize power, hours, day
        energy(power, hours, day)
        price(total_energy)
        store(name, appliance, power, total_energy, total_cost)
        print("\n")  # Add spacing after calculation

    elif task == "2":
        if info:  # Only break if there's data to show
            table()
            break  # Exit loop after showing results
        else:
            table()  # This will show the error message and continue

    elif task == "3":
        exit("Thanks for using this program!")

    else:
        print("Invalid option.\n")

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


# Storage
def store(name, appliance, total_energy, total_cost):
    new_user = {
        "name": [
            {"appliance": appliance},
            {"power": power},
            {"energy": total_energy},
            {"cost": total_cost},
        ]
    }

    info = []
    info.append(new_user)


# Terminal table
def table(name, appliance, total_energy, total_cost):
    store(name, appliance, total_energy, total_cost)
    header = f"| {'Name':<10} | {'Appliance':<10} | {'Total Power':<7} | {'Total Cost':<12} |"
    print(header)
    ln_break = len(header)
    print("-" * ln_break)


# Terminal CLI
task = input(
    "Power Usage and Cost Calculator \n\n What would you like to do? \n 1. Calculate total energy and cost \n 2. Show all results \n 3. Quit"
)

if task == "1":
    ans = energy(power, hours, day)
    print(ans)

elif task == "2":
    table(name, appliance, total_energy, total_cost)

elif task == "3":
    exit("Thanks for using this program!")

else:
    print("INvalid choice")

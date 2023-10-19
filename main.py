#1

seasons = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Autumn',
    12: 'Winter'
}


month_number = int(input('Enter a month number (1-12): '))

if 1 <= month_number <= 12:
    season = seasons[month_number]
    print(f'The corresponding season for month {month_number} is {season}.')
else:
    print('Invalid month number. Please enter a number between 1 and 12.')


#2

names_set = set()

all_names = []

name = input("Enter a name (or press Enter to quit): ")

while name != "":
    if name in names_set:
        print("Existing name")
    else:
        print("New name")
        names_set.add(name)

    all_names.append(name)
    name = input("Enter a name (or press Enter to quit): ")


print("\nAll names entered:")
for name in all_names:
    print(name)

#3

airport_data = {}

choice = "0"

while choice != "3":
    print("Airport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        icao_code = input("Enter the ICAO code of the airport: ")
        airport_name = input("Enter the name of the airport: ")
        airport_data[icao_code] = airport_name
        print(f"Airport '{airport_name}' with ICAO code '{icao_code}' has been added.")
    elif choice == "2":
        icao_code = input("Enter the ICAO code of the airport to fetch information: ")
        if icao_code in airport_data:
            print(f"The name of the airport with ICAO code '{icao_code}' is '{airport_data[icao_code]}'.")
        else:
            print(f"Airport with ICAO code '{icao_code}' not found.")
    elif choice == "3":
        print("Exiting the program.")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")


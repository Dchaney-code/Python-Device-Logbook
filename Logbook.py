Database = {}

def add_new_device():
    global Database
    print ("\n--- Adding New Device ---")
    device_id = input("Please enter the ID of the device (e.g. defib-001):")
    device_type = input(f"Please enter what type of device {device_id} is (e.g. Defibrillator):")
    device_ward = input(f"Please enter the ward of {device_id} (e.g. A&E):")
    Database[device_id] = {
    'type': device_type,
    'ward': device_ward,
    'maintenance_logs': []
    }
    print (f"\nDevice {device_id} ({device_type}) added to the logbook successfully.")

def maintenance_log_task():
    print("\n--- Accessing maintenance log---")
    device_id = input("Enter the ID of the device you want to log: ")
    if device_id in Database:
        print(f"---logging {device_id} ({Database[device_id]['type']}) ---")
        maintenance_description = input("Please enter the description of the maintenance carried out on the device (e.g., calibrated sensor): ")
        Database[device_id]['maintenance_log'].append(maintenance_description)
        print(f"\n{device_id}s Maintenance has been successfully logged.")
    else:
        print(f"\nInvalid Device ID detected '{device_id}' is not found in the logbook please check for typo's and try again.")
        print("Please Make sure the device has been registered to the database using option 1 from the main menu.")

def main_menu():
    print("\n---Welcome to the Medical Devices Logbook---")
    print ("1. Add new device")
    print ("2. log maintenance task")
    print ("3. view device history")
    print ("4. quit")
    choice = input("please choose an option from (1-4): ")
    return choice

while True:
    user_choice = main_menu()
    if user_choice == '1':
        add_new_device()
    elif user_choice == '2':
        maintenance_log_task()
    elif user_choice == '3':
        print ("View device history WIP")
    elif user_choice == '4':
        print ("Now exiting logbook. Goodbye...")
        break
    else:
        print("Invalid option chosen. Please review your choice and choose from options 1 to 4.")
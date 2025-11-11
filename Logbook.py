Database = {}

def main_menu():
    print("/n---Welcome to the Medical Devices Logbook---")
    print ("1. Add new device")
    print ("2. log maintenance task")
    print ("3. view device history")
    print ("4. quit")
    choice = input("please choose an option from (1-4): ")
    return choice

while True:
    user_choice = main_menu()
    if user_choice == '1':
        print ("Add device WIP")
    elif user_choice == '2':
        print ("Log maintenance task WIP")
    elif user_choice == '3':
        print ("View device history WIP")
    elif user_choice == '4':
        print ("Now exiting logbook. Goodbye...")
        break
    else:
        print("Invalid option chosen. Please review your choice and choose from options 1 to 4.")
import csv


def welcome():
    # Create an entry variable using the input function and multiple line strings format
    entry = int(input("""Welcome to Python Contacts.  
                    >>>Python Contacts commands are: 1,2,3 or 4 <<<
                    >>>What would you like to do?<<<
                    1. List exiting contacts
                    2. Create a new contact
                    3. Check a contact
                    4. Delete an entry
                    5. Exit
                    Enter your entry here(1,2,3 0r 4):  """))

    # Close the function
    return entry

def list_contacts():
    print("Let's list all contacts")
    with open("contacts_raw.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for entry in reader:
            print(f"""
            Given Name": {entry["Given Name"]}, "Family Name": {entry["Family Name"]}, 
            "Initials": {entry["Initials"]}
            "Birthday": {entry["Birthday"]}
            "Notes": {entry["Notes"]}
            "Group Membership" {entry["Group Membership"]}\n
            """)


def create_contact():
    print("Let's add a contact")
    column_names = ["Name", "Given Name", "Additional Name", "Family Name",
            "Yomi Name", "Given Name Yomi", "Additional Name Yomi", "Family Name Yomi",
            "Name Prefix", "Name Suffix", "Initials", "Nickname", "Short Name", "Maiden Name",
            "Birthday", "Gender", "Location", "Billing Information", "Directory Server", "Mileage",
            "Occupation", "Hobby", "Sensitivity", "Priority", "Subject",
            "Notes", "Language", "Photo",
            "Group Membership",
            "E-mail 1 - Type", "E-mail 1 - Value", "E-mail 2 - Type","E-mail 2 - Value",
            "Phone 1 - Type", "Phone 1 - Value", "Phone 2 - Type", "Phone 2 - Value",
            "Organization 1 - Type", "Organization 1 - Name",
            "Organization 1 - Yomi Name", "Organization 1 - Title", "Organization 1 - Department",
            "Organization 1 - Symbol", "Organization 1 - Location", "Organization 1 - Job Description"]

    entry = {"Name": "", "Given Name": "", "Additional Name": "", "Family Name": "",
            "Yomi Name": "", "Given Name Yomi": "", "Additional Name Yomi": "", "Family Name Yomi": "",
            "Name Prefix": "", "Name Suffix": "", "Initials": "",
            "Nickname": "", "Short Name": "", "Maiden Name": "",
            "Birthday": "", "Gender": "", "Location": "",
            "Billing Information": "", "Directory Server": "", "Mileage": "",
            "Occupation": "", "Hobby": "", "Sensitivity": "", "Priority": "", "Subject": "",
            "Notes": "", "Language": "", "Photo": "",
            "Group Membership": "",
            "E-mail 1 - Type": "", "E-mail 1 - Value": "", "E-mail 2 - Type": "","E-mail 2 - Value": "",
            "Phone 1 - Type": "", "Phone 1 - Value": "", "Phone 2 - Type": "", "Phone 2 - Value": "",
            "Organization 1 - Type": "", "Organization 1 - Name": "",
            "Organization 1 - Yomi Name": "", "Organization 1 - Title": "", "Organization 1 - Department": "",
            "Organization 1 - Symbol": "", "Organization 1 - Location": "", "Organization 1 - Job Description": ""}

    print("You may press Enter if you do not wish to input such information")
    entry["Given Name"] = str(input("Please input Given Name:\n"))
    entry["Family Name"] = str(input("Please input Family Name:\n"))
    entry["Initials"] = str(input("Please input Initials:\n"))
    entry["Birthday"] = str(input("""Please input Birthday in XXXX-XX-XX format.
    If you do not wish to input year of birth, you may enter "-" as the year
    eg. --12-02\n"""))
    entry["Notes"] = str(input("Please input Notes:\n"))
    entry["Group Membership"] = str(input("""Please input tag(s) of the entry.
    Please separate each tag by " ::: "
    eg. Friend ::: Xccelerate ::: FTDS2023NOV\n"""))

    with open("contacts_raw.csv", "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_names)
        writer.writerow(entry)
        csvfile.close()


def check_contact():
    print("Let's print all contacts start with a Phrase as Given Name")
    print("If there is no matching result, we will return to start page")
    phrase = str(input("Please input Phrase:\n"))
    with open("contacts_raw.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for entry in reader:
            if entry["Given Name"].startswith(phrase):
                print(f"""
                Given Name": {entry["Given Name"]}, "Family Name": {entry["Family Name"]}, 
                "Initials": {entry["Initials"]}
                "Birthday": {entry["Birthday"]}
                "Notes": {entry["Notes"]}
                "Group Membership" {entry["Group Membership"]}\n
                """)

def delete_contact():
    # Prompting the user for the first value in the row to be deleted
    value_to_delete = str(input("Enter Given Name of the contact to be deleted: "))

    file_path = "contacts_raw.csv"

    # Creating a temporary file to store the updated data
    temp_file_path = "contacts_temp.csv"

    try:
        # Opening the input file in read mode and the temporary file in write mode
        with open("contacts_raw.csv", 'r') as input_file, open(temp_file_path, 'w', newline='') as temp_file:
            # Creating a CSV reader and writer objects
            reader = csv.reader(input_file)
            writer = csv.writer(temp_file)

            entry_deleted = False

            # Iterating over each row in the input file
            for entry in reader:

                # Checking if the first value in the row matches the value to be deleted
                if entry[1] == value_to_delete:
                    entry_deleted = True
                    continue
                # Writing the row to the temporary file
                writer.writerow(entry)

            # Checking if the row was found and deleted
            if entry_deleted:
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")

        # Replacing the input file with the temporary file
        import os
        os.replace(temp_file_path, file_path)


    except FileNotFoundError:
        raise FileNotFoundError("Specified file does not exist.")


def phonebook():
    # initiate a while loop to continuously run the phonebook program
    while True:
        # call welcome function.
        # Set entry variable to welcome function
        entry = welcome()

        # Create conditions for decision-making for any option entered by the user
        if entry == 1:
            list_contacts()

        # Decision For the 2nd entry
        elif entry == 2:
            create_contact()

        # Create a decision for the third entry
        elif entry == 3:
            check_contact()

        # Create a decision for entry 4
        elif entry == 4:
            delete_contact()

        elif entry == 5:
            print("Thanks for using Python Contacts")
            break
        # Error Message
        else:
            print("Incorrect Entry. Please try again")

# End of Program


# Run Program
phonebook()





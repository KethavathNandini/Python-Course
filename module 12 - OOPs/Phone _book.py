class PhoneBook:
    phone_directory = []


    def __init__(self , name, phone_number):
        self.name = name
        self.phone = phone_number
        PhoneBook.phone_directory.append(self)

    def show_contact(self):
        return f"Name: {self.name}, contanct number: {self.phone}"

    @classmethod
    def show_all_contancts(cls):
        if len(cls.phone_directory) == 0:
            print("no contacts found in the directory")
        else:
            for contacts in cls.phone_directory:
                print(contacts.show_contact())

    @classmethod
    def search_contact(cls,search_name):
        for contact_del in cls.phone_directory:
            if contact_del.name.upper() == search_name.upper():
                return contact_del.phone

        return f"No contact found for {search_name}"


    @staticmethod
    def validate_phonne_number(number):
        if len(number) >=8 and number.isdigit():
            return True
        else:
            return False


n_contacts = int(input("enter how many contacts do you want to add?: "))

for i in range(n_contacts):
    name = input("Enter the name of contact: ")
    phone_number = input("Enter the phone number ")
    if PhoneBook.validate_phonne_number(phone_number):
        PhoneBook(name , phone_number)



PhoneBook.show_all_contancts()
# c1 = PhoneBook("john" , 927094792)
# c2 =PhoneBook("carol", 78739270)
# print(PhoneBook.phone_directory)
# # print(c1.show_contact())
# PhoneBook.show_all_contancts()
# print(PhoneBook.search_contact("john"))
# print(PhoneBook.search_contact("Carol"))
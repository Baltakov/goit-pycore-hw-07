from models import AddressBook, Record
from utils import input_error

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Phone number updated."
    else:
        return "Contact not found."

@input_error
def show_phones(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        return f"Phones for {name}: " + ", ".join(phone.value for phone in record.phones)
    else:
        return "Contact not found."

@input_error
def show_all(book: AddressBook):
    return "\n".join(str(record) for record in book.values()) or "No contacts in the address book."

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        return "Contact not found."

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"Birthday for {name}: {record.birthday.value.strftime('%d.%m.%Y')}"
    else:
        return "Contact or birthday not found."

def birthdays(book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if upcoming:
        return "\n".join(str(record) for record in upcoming)
    else:
        return "No upcoming birthdays."

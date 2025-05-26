# Script to test the various functions in the contactDAO

from contactDAO import contactDAO

dao = contactDAO() # create an instance

# GET all contacts
print("GET all contacts:")
all_contacts = get_all_contacts()
print(all_contacts, "\n")

# CREATE a new contact
print("CREATE new contact:")
new_contact_data = {
    "first_name": "DAO",
    "last_name": "Tester",
    "email": "dao.tester@example.com",
    "phone": "555-0100",
    "health_score": 75,
    "account_id": 14  # Make sure this account ID exists in your DB
}
new_contact_id = create_contact(new_contact_data)
print(f"Created contact with ID: {new_contact_id}\n")

# GET the new contact by ID
print(f"GET contact by ID {new_contact_id}:")
contact = get_contact_by_id(new_contact_id)
print(contact, "\n")

# UPDATE the contact
print(f"UPDATE contact with ID {new_contact_id}:")
updated_data = {
    "first_name": "UpdatedDAO",
    "last_name": "Tester",
    "email": "updated.dao@example.com",
    "phone": "555-0200",
    "health_score": 85,
    "account_id": 14
}
update_success = update_contact(new_contact_id, updated_data)
print("Update success:", update_success)
print(get_contact_by_id(new_contact_id), "\n")

# DELETE the contact
print(f"DELETE contact with ID {new_contact_id}:")
delete_success = delete_contact(new_contact_id)
print("Delete success:", delete_success)

# Confirm deletion
print(f"GET deleted contact ID {new_contact_id} (should be None):")
deleted_contact = get_contact_by_id(new_contact_id)
print(deleted_contact)
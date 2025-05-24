# Script to test the various functions in the DAO

from account_DAO import accountDAO

dao = accountDAO() # create an instance

# Get all accounts
print("Testing all accounts function:")
print(dao.getAllAccounts())

# Create a new account
print("\nTesting account creation function:")
new_account = {"account_name": "Test Corp", "website": "testcorp.com"}
new_id = dao.createAccount(new_account)
print("Created account with ID:", new_id)

# Find by ID
print("\nTesting find account by ID function:")
print(dao.findAccountByID(new_id))

# Update the account
print("\nTesting update account by ID function:")
dao.updateAccount({"id": new_id, "account_name": "Updated Corp", "website": "updatedcorp.com"})
print("Updated account with ID:", new_id)
print(dao.findAccountByID(new_id))

# Delete the account
print("Testing account deletion by ID function:")
dao.deleteAccount(new_id)
deleted = dao.findAccountByID(new_id)
print("Should return None (if deleted):", deleted)

# FInal check
print("\nFinal account list:")
print(dao.getAllAccounts())
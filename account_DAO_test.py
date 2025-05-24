# Script to test the various functions in the DAO

from account_DAO import accountDAO

# Get all accounts
print("Testing all accounts function:")
print(accountDAO.getAllAccounts())

# Create a new account
print("Testing account creation function:")
new_account = {"account_name": "Test Corp", "website": "testcorp.com"}
new_id = accountDAO.createAccount(new_account)
print("Created account with ID:", new_id)

# Find by ID
print("Testing find account by ID function:")
print(accountDAO.findAccountByID(new_id))

# Update the account
print("Testing update account by ID function:")
accountDAO.update({"id": new_id, "account_name": "Updated Corp", "website": "updatedcorp.com"})
print("Updated account with ID:", new_id)

# Delete the account
print("Testing account deletion by ID function:")
accountDAO.delete(new_id)
print(accountDAO.findAccountByID(new_id))
print(accountDAO.getAllAccounts())
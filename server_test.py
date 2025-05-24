# Script to test flask app server functions

import requests

BASE_URL = "https://fdennehy.pythonanywhere.com/accounts"

# 1. Get all accounts
print("\nGET all accounts:")
response = requests.get(BASE_URL)
print(response.json())

# 2. Create new account
print("\nCreate new account (POST):")
new_account = {"account_name": "Server Test Corp", "website": "http://servertest.com"}
response = requests.post(BASE_URL, json=new_account)
created = response.json()
print(created)

# 3. Get account by ID
account_id = created["account_id"]
print(f"\nGET account by ID {account_id}:")
response = requests.get(f"{BASE_URL}/{account_id}")
print(response.json())

# 4. Update account
print(f"\nUpdate account (PUT) with ID {account_id}:")
updated_data = {"account_name": "Updated Server Corp", "website": "http://updatedserver.com"}
response = requests.put(f"{BASE_URL}/{account_id}", json=updated_data)
print("Status code:", response.status_code) # debug
print("Respnse content:", repr(response.text)) # debug

if response.status_code in (200, 201):
    print(response.json())
else:
    print("Update faied, no JSON returned")

# 5. Delete account
print(f"\nDELETE account {account_id}:")
response = requests.delete(f"{BASE_URL}/{account_id}")
print(response.json())

# 6. Verify deletion
print(f"\nGET deleted account {account_id}:")
response = requests.get(f"{BASE_URL}/{account_id}")
print("Expected 404 or error message:", response.text)
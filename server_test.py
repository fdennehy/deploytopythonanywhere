# Script to test flask app server functions

import requests

BASE_URL = "https://fdennehy.pythonanywhere.com/accounts"

# 1. Get all accounts: curl https://fdennehy.pythonanywhere.com/accounts
print("\n GET all accounts: \n")
response = requests.get(BASE_URL)
print(response.json())

# 2. Create new account
# curl -i -H "Content-Type: application/json" -X POST -d '{"name": "Server Test Corp", "website": "http://servertest.com", "revenue": "0", "region":"Africa"}' https://fdennehy.pythonanywhere.com/accounts
print("\n Create new account (POST): \n")
new_account = {
    "name": "Server Test Corp", 
    "website": "http://servertest.com", 
    "revenue":"0", 
    "region":"Africa"
}
response = requests.post(BASE_URL, json=new_account)
created = response.json()
print("\n Created account: \n", created)

new_id = created.get("id") 
if not new_id:
    print("\n Failed to create account. Exiting test. \n")
    exit(1)

# 3. Get an account by id: curl https://fdennehy.pythonanywhere.com/accounts/{new_id}"
print(f"\n GET account by ID {new_id}: \n")
response = requests.get(f"{BASE_URL}/{new_id}")
print(response.json())

# 4. Update account
# curl -i -H "Content-Type: application/json" -X PUT -d '{"name": "Updated Server Corp", "website": "http://updatedserver.com", "revenue": "0", "region":"Antarctica"}' https://fdennehy.pythonanywhere.com/accounts/id
print(f"\n Update account (PUT) with ID {new_id}:")
updated_data = {
    "name": "Updated Server Corp", 
    "website": "http://updatedserver.com", 
    "revenue":"0", 
    "region":"Antarctica"
}
response = requests.put(f"{BASE_URL}/{new_id}", json=updated_data)
print("\n Status code:", response.status_code) # debug
print("\n Response content:", repr(response.text)) # debug

if response.status_code in (200, 201):
    print(response.json())
else:
    print("\n Update failed, no JSON returned")

# 5. Delete an account by id: curl -X DELETE https://fdennehy.pythonanywhere.com/accounts/{new_id}
print(f"\n DELETE account {new_id}: \n")
response = requests.delete(f"{BASE_URL}/{new_id}")
print(response.json())

# 6. Verify deletion: curl -i https://fdennehy.pythonanywhere.com/accounts/{new_id}
print(f"\n GET deleted account {new_id}: \n")
response = requests.get(f"{BASE_URL}/{new_id}")
print("Expected 404 or error message:", response.text)

# 7. Delete all accounts: curl -X DELETE https://fdennehy.pythonanywhere.com/accounts/wipe
print(f"\n DELETE all accounts \n")
response = requests.delete(f"{BASE_URL}/wipe")
print(response.json())

# 8. Verify all accounts have been deleted: curl https://fdennehy.pythonanywhere.com/accounts
print("\n Confirming all accounts have been deleted: \n")
response = requests.get(BASE_URL)
print(response.json())

# 9. Insert dummy accounts: curl -X DELETE curl -X POST https://fdennehy.pythonanywhere.com/accounts/dummy
print("\n Rehydrating database with dummy data: \n")
response = requests.post(f"{BASE_URL}/dummy")
if response.status_code == 201:
    dummy_data = response.json()
    print("Dummy insert success:", dummy_data.get("message"))
else:
    print("Dummy data insert failed:", response.text)

# 10. Verify dummy account have been created: curl https://fdennehy.pythonanywhere.com/accounts
print("\n Confirming dummy accounts have been created: \n")
response = requests.get(BASE_URL)
print(response.json())
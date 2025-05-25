# Import required modules
from flask import Flask, jsonify, request, abort, render_template
from flask_cors import CORS, cross_origin
from account_DAO import accountDAOInstance

app = Flask(__name__, static_url_path='', static_folder='static') # serve static files from static/, but make them accessible at the root URL.
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

# Serve html file to root url /
@app.route('/')
@cross_origin()
def account_viewer():
    return render_template("account_viewer.html")

# Get all accounts: curl https://fdennehy.pythonanywhere.com/accounts
@app.route('/accounts')
@cross_origin()
def getAllAccounts():
    results = accountDAOInstance.getAllAccounts()
    return jsonify(results)

# Get an account by id: curl https://fdennehy.pythonanywhere.com/accounts/id"
@app.route('/accounts/<int:id>')
@cross_origin()
def getAccountById(id):
    account = accountDAOInstance.findAccountByID(id)
    if account:
        return jsonify(account)
    else:
        return jsonify({"error": "Account not found"}), 404

# Create new account: 
# curl -i -H "Content-Type: application/json" -X POST -d '{"name": "Server Test Corp", "website": "http://servertest.com", "revenue": "0", "region":"Africa"}' https://fdennehy.pythonanywhere.com/accounts
@app.route('/accounts', methods=['POST'])
@cross_origin()
def createAccount():
    account = request.get_json()
    if not account:
        abort(400, description="Invalid Input")
    new_account = accountDAOInstance.createAccount(account)
    if new_account:
        return jsonify(new_account), 201
    else:
        return jsonify({"error": "Account creation failed"}), 500

# Update account by ID
# curl -i -H "Content-Type: application/json" -X PUT -d '{"name": "Updated Server Corp", "website": "http://updatedserver.com", "revenue": "0", "region":"Antarctica"}' https://fdennehy.pythonanywhere.com/accounts/id
@app.route('/accounts/<int:id>', methods=['PUT'])
@cross_origin()
def updateAccount(id):
    account = request.get_json()
    if not account:
        abort(400, description="Invalid input")
    updated = accountDAOInstance.updateAccount(id, account)
    if updated:
        return jsonify(updated)
    else:
        return jsonify({'error': 'Account update failed'}), 500
        
# Delete an account by id: curl -X DELETE https://fdennehy.pythonanywhere.com/accounts/id
@app.route('/accounts/<int:id>' , methods=['DELETE'])
@cross_origin()
def deleteAccount(id):
    result = accountDAOInstance.deleteAccount(id)
    if result:
        return jsonify({"success":True, "message":"Account deleted successfully"}),200
    else:
        return jsonify({"error":"Account deletion failed"}), 404

# Delete all account data: curl -X DELETE https://fdennehy.pythonanywhere.com/accounts/wipe
@app.route('/accounts/wipe', methods=['DELETE'])
@cross_origin()
def wipeAllAccounts():
    result = accountDAOInstance.deleteAllAccounts()
    if result:
        return jsonify({"success":True, "message":"All accounts deleted successfully."}), 200
    else:
        return jsonify({"error":"Failed to delete accounts or no accounts found"}), 500

# Generate dummy data: curl -X POST https://fdennehy.pythonanywhere.com/accounts/dummy
@app.route('/accounts/dummy', methods=['POST'])
@cross_origin()
def insertDummyAccounts():
    result = accountDAOInstance.dummyDataInsert()
    if result:
        return jsonify({"success": True, "message": "Dummy data inserted successfully.", "accounts": result}), 201
    else:
        return jsonify({"error": "Failed to insert dummy data."}), 500

if __name__ == '__main__' :
    app.run(debug= True)
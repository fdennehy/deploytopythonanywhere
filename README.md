# Simple Customer Success Management (CSM) Tool

## Overview
This project is a lightweight web-based dashboard for managing Accounts and Contacts, built with:
- **Flask** for the backend
- **MySQL** as the database
- **HTML, JavaScript, jQuery, Chart.js, and Bootstrap** on the frontend

Key functionality includes CRUD operations on Accounts and Contacts, and real-time visualization of average contact health scores by account.

---

## Features

✅ Manage Accounts:  
- Create, Read, Update, Delete  
- Real-time validation  

✅ Manage Contacts:  
- Create, Read, Update, Delete  
- Health score tracking  
- Optional generation of dummy contacts using RandomUser API

✅ Insights:  
- **Bar Chart** of average contact health scores per account (auto-refreshes after data changes)  

✅ UX Improvements:  
- Dynamic content areas  
- Collapsible side menus  
- Responsive chart display  

---

## Folder Structure

```
project/
│
├── templates/
│   └── dashboards.html      # Main HTML page with embedded JavaScript
│
├── accountDAO.py            # DAO logic for accounts table
├── contactDAO.py            # DAO logic for contacts table
├── server.py                # Flask backend server
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---

## Setup Instructions

1. **Clone the repository**

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up the MySQL database**
   - Ensure your database is running
   - Create tables: `account`, `contact`
   - Update your connection credentials in the DAO files if needed

5. **Run the Flask server**
```bash
python server.py
```

6. **Open the Dashboard**
   Navigate to `http://127.0.0.1:5000/` in your browser

---
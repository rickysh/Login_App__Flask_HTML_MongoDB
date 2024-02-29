from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient


template_dir = "../frontend/templates"

app = Flask(__name__, template_folder=template_dir)

# MongoDB connection
client = MongoClient('mongodb+srv://<username>:<password>@cluster0.kuewrfz.mongodb.net/')
db = client['full_stack_db']  # Replace 'your_database_name' with your actual database name
collection = db['full_stack_col_1']  # Replace 'your_collection_name' with your actual collection name

@app.route('/', methods=['GET', 'POST'])
def login():
    err_msg = ""
    if request.method == 'POST':
        user = request.form['user']
        password = int(request.form['password'])

        user_data = collection.find_one({'user': user, 'password': password})

        if user_data:
            return redirect(url_for('welcome', user=user))
        else:
            err_msg = "Invalid username or password"
            return render_template('index.html', err_msg=err_msg)  # Render the form template
    return render_template('index.html', err_msg=err_msg)  # Render the form template

@app.route('/<user>')
def welcome(user):
    curr_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render_template('login_success.html', user=user, curr_time=curr_time)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

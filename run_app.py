# import libray 
from flask import Flask, render_template, redirect, url_for, session, flash, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from flask_mysqldb import MySQL

# inheret flask properties
app = Flask(__name__)

# create database connection
app.config['MYSQL_HOST'] = 'localhost'  # Correct key for MySQL host
app.config['MYSQL_USER'] = 'root'  # Correct key for MySQL user
app.config['MYSQL_PASSWORD'] = 'kali7'  # Correct key for MySQL password
app.config['MYSQL_DB'] = 'web_database'  # Correct key for MySQL database name
app.config['MYSQL_PORT'] = 3306  # Default MySQL port, explicitly set it
app.secret_key = 'your_secret_key_here'

mysql = MySQL(app)
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=20)])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=1, max=100)])  # Adjust range as needed
    gender = SelectField("Gender", choices=[('', 'Select your gender'), ('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[DataRequired()])
    profession = SelectField("Profession",choices=[('', 'Select your profession'),('student', 'Student'), ('employee', 'Employee')], validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])  # Password min length added
    submit = SubmitField("Sign Up")

    def validate_name(self, field):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user_detail WHERE name = %s", (field.data,))
        user = cursor.fetchone()
        cursor.close()
        if user:
            raise ValidationError("Name already exists. Please choose a different name.")
        
class LoginForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

#create route (connection between html file and flask file)
@app.route("/")
def home():

    if 'name' in session:  # Check if user is logged in
        # If logged in, display home page with username
        name = session['name']
        return render_template("homepage.html", name=name)  # Pass the name to the template
    else:
        # If not logged in, display home page with register button
        return render_template("homepage.html", register=True)  # Use the register flag for UI logic

    return render_template("homepage.html")

@app.route("/register", methods= ["GET", "POST"])
def register():

    # create form
    form = RegisterForm()
    
    # validate form
    if form.validate_on_submit():

        # Collect input values
        name = form.name.data
        age  = form.age.data
        gender = form.gender.data
        profession = form.profession.data
        password = form.password.data

        # Insert data into the database
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO user_detail(name, age, gender, profession, password) VALUES (%s, %s, %s, %s, %s)",(name, age, gender, profession, password))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for("login"))
    
    return render_template("register.html", form = form)


@app.route("/login", methods=["GET", "POST"])
def login():

    # create form
    form = LoginForm()

    # validate form
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user_detail WHERE name = %s AND password = %s", (name, password))
        user = cursor.fetchone()
        cursor.close()

        # redirect to user dashboard
        if user:
            session['name'] = name
            return redirect(url_for("user_dashboard"))
        else:
            flash("Invalid username or password. Please try again.")
            return redirect(url_for("login"))

    return render_template("login.html", form = form)

@app.route("/user_dashboard")
def user_dashboard():

    # check if user is logged in
    if 'username' not in session:
        name = session['name']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user_detail WHERE name = %s", (name,))
        user = cursor.fetchone()
        cursor.close()

        # render user dashboard
        if user:
            return render_template("user_dashboard.html", user=user)

        # redirect to login page
        return redirect(url_for("login"))

@app.route('/logout', methods=['POST'])
def logout():
    # Logic to log out the user
    session.clear()  # Clear user session
    return redirect('/')

@app.route("/cousres")
def cousres():
    return render_template("course.html")


@app.route('/quiz/<topic>', methods=['GET', 'POST'])
def quiz(topic):

    import test

    quiz_data = test.test().quiz_data


    if topic not in quiz_data:
        return "Quiz topic not found", 404
    
    questions = quiz_data[topic]
    
    if request.method == 'POST':
        answers = request.json.get('answers')
        score = 0
        for question, answer in zip(questions, answers):
            if answer == question['correct']:
                score += 1
        return jsonify({"score": score, "total": len(questions)})
    
    return render_template('quiz.html', topic=topic, questions=questions)

@app.route('/about')
def about():    
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


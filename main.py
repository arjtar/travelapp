from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/login')
def login():
	return render_template('login.html')

	@app.route('/doLogin',methods=['POST'])
	def doLogin();
		email = request.form['email']
		email = request.form['psw']

		return render_template('home.html',result={"email":email}
app.run()

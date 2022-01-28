from flask import Flask , render_template , request
app=Flask(__name__,template_folder='templates')

def home():
 return render_template("home.html")

def about():
 return render_template("about.html")

def contact():
 return render_template("contact.html")

def service():
 return render_template("service.html")

def register():
 if request.method=="GET":
  return render_template("register.html",msg="")
 else:
  #print(request.form)
  name=request.form['name']
  username=request.form['username']
  password=request.form['password']
  address=request.form['address']
  city=request.form['city']
  gender=request.form['gender']
  print(name+"<------>"+gender)	 
  return render_template("register.html",msg="form submitted")	

def login():
 return render_template("login.html")

app.add_url_rule("/","home",home)
app.add_url_rule("/about","about",about)
app.add_url_rule("/contact","contact",contact)
app.add_url_rule("/service","service",service)
app.add_url_rule("/register","register",register,methods=["GET","POST"])
app.add_url_rule("/login","login",login)

if __name__== '__main__':
 app.run(debug=True,port=5001)
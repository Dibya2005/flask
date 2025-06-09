
# from flask import Flask, request


# app=Flask(__name__) # ye flask ko batayega jois file par ham kam kr rha ha ye hamari flask ki main file ha
# @app.route("/") # root decorator koi ye flask ko ye batayega ki jabbhi  home page visit karega apko iske niche wala code chalana ha
# def home():
#   return "hello userr  This is my first flsk app"
# @app.route("/about")
# def about():
#   return "this is about page"
# @app.route("/contact")
# def contact():
#   return "this is a contact page"
# @app.route("/submit",methods=["GET","POST"])
# def submit():
#   if request.method=='POST':
#    return "you sent data"
#   else:
#     return "you only viewing the form"
from flask import Flask,request,redirect,url_for,session,Response
app=Flask(__name__)
app.secret_key="supersecret" # for work with session in flask reuired in flask so that we can securely session ka use kr pao koi aur dusra insan usko use krke modify na krde
# lets make a home page 
@app.route("/",methods=["GET","POST"])
def login():
  if request.method=="POST":
    username=request.form.get("username")
    password=request.form.get("password")
    if username=="admin" and password=="123":
      session["user"]=username #store in session
      return redirect(url_for("welcome"))
    else:
      return Response("invalid credential, trry again !",mimetype="text/plain") #mime type what typee of contant you will return  for html return donot have to initialize the return type
    #ham if me return karega kya return karega ek html ka form
  return '''
           <h2> login page</h2>
           <form method="POST">
           Username:<input type="text" name="username"> <br>
           Password:<input type="text" name="password"><br>
           <input type="submit" value="Login">
           </form>
'''
#welcome page after login
@app.route("/welcome")
def welcome():
  if "user" in session:
    return f'''
       <h2>welcome ,{session["user"]}!</h2>
       <a hred={url_for('logout')}>logout</a>

  '''
  return redirect(url_for("login")) #logout click krli arun login page t redirect hbo
#logout route
@app.route("/logout")
def logout():
  session.pop("user",None) #sesiion r pora user tu remove krbo
  return redirect(url_for("login"))
#none pass krsu jdi user amr session t nai error hoa r pora basoi

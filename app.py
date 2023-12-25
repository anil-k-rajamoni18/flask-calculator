from flask import Flask , render_template ,request

app = Flask(__name__) #__main___

@app.route("/")
def index():
  return "<h1 style = 'color:red'><center>Hello World Flask....</center></h1>"



@app.route("/home")
def home():
  return render_template("home.html")


@app.route("/hello")
def hello():
  return "<h1><center>Greetings....</center></h1>"

@app.route("/calculator",methods=["GET","POST"])
def calculator():
  if request.method == "POST":
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    op = request.form["op"]
    result = 0
    if op=="+":
      result = num1 + num2
    elif op=="-":
      result = num1 - num2
    elif op=="*":
      result = num1 * num2
    elif op=="/":
      result = num1 / num2
    
    elif op=="//":
      result = num1 // num2

    elif op=="**":
      result = num1 ** num2
    
    elif op=="%":
      result = num1 % num2

    else:
      result = f"invalid symbol {op}"

    result = f"{num1} {op} {num2} = {result}"

    return render_template("result.html",response = result)




@app.route("/user/<name>")
def user(name):
  return f"<h2>hello .... {name}</h2>"


@app.route("/contact")
def contact():
  return "<h3> contact us page</h3>"


if __name__ == '__main__':
  app.run()
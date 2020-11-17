from  flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def DTC():
  return render_template("first.html")

"""@app.route('/result', method=['POST'])
def row():
  return render_template("")"""

if __name__== "__main__":
  app.run()

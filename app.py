from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/<name>')
def index1(name):
    return '<h1> Hello {}'.format(name)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods = ['POST','GET'])
def result():
    output = request.form.to_dict()
    name = output["name"]
    return render_template("DisplayResult.html",name = name)



'''
@app.route('/')
def home():
    return "Hello, add /Yourname in url and see the wonder"
'''
if __name__ == "__main__":
    app.run(debug=True)
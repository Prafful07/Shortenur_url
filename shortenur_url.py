from flask import Flask, render_template,request,redirect

import string
import random
 
# initializing size of string
N = 5
 
# using random.choices()
# generating random strings
def getrand():
    return ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=N))

app = Flask(__name__)

redirect_data = {}
@app.route('/', methods=["GET","POST"])
def home():
    url = request.form.get("url")
    if url!=None and len(url)!=0:
        rval = getrand()
        redirect_data[rval] = url
        
        return render_template('shortenurl.html',data={"url":f'http://127.0.0.1:5000/{rval}'}) 
    return render_template('index.html')

@app.route('/<id>')
def shortner(id):
    return redirect(redirect_data[id])  
    
 
 

 
app.run(debug=True)
from flask import Flask, render_template, redirect

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/amazon')
def amazon():
    return redirect("https://www.amazon.in/Secret-History-Donna-Tartt/dp/0140167773")
     

app.run(debug=True)
from flask import Flask,request

app = Flask(__name__)

@app.route('/komi')

def salma():
    user  = request.args.get('user', 'guest')
    return f"<h1>Heellll {user}</h1>"

if __name__ == "__main__":
    app.run()
 
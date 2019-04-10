from flask import Flask, request
from caesar import encrypt



app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!Doctype html>
<html>
    <head>

        <style>
            
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px san-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
        <body>

            <form action = "/" method = 'POST'>
                <label> <strong>Rotate by</strong>: </label>
                <input name = "rot" type = "text" value = 0>
                <textarea name = "text"> {0} </textarea>
                <input type = "submit" value = " Submit Query"/>
            </form>

        </body>
</html>
"""
@app.route("/")
def index():
    return form.format('')

@app.route("/", methods = ['POST'])
def encryption():
    rots = int(request.form['rot'])
    msg = request.form ['text']
    return form.format (encrypt(msg,rots))

app.run()
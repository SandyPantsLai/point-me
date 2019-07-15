from flask import Flask
app = Flask( __name__ )

@app.route('/')
def main():
    return 'Hello World!'

@app.route('/blue')
def blue():
    return 'Blue!'

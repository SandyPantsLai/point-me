from flask import Flask
app = Flask( __name__ )

@app.route('/')
def main():
    return 'Redirected to Blue from /!'

@app.route('/blue')
def blue():
    return 'Blue!'

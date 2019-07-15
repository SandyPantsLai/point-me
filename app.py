from flask import Flask
app = Flask( __name__ )

@app.route('/blue/')
def main():
    return 'Blue!'

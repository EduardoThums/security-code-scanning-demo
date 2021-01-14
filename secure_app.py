from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def health_check():
    return 'Everything is working just fine!'        

if __name__ == '__main__':
    app.run(debug=True)

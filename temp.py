from flask import Flask

app = Flask(__name__)

@app.route('/testing_api')
def hello_world():
    return 'Hello, World!'

#add content here








#do not go beyond here
if __name__ == '__main__':
    app.run(debug=True)
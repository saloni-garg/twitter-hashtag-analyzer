from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
# def hello():
#     return "Hello World!"
def main():
	print("Hello")
	return render_template('index.html')


@app.route('/', methods=['POST'])
def handle_data():
    text = request.form['inputText']
    print(text)
    return text

if __name__ == '__main__':
	app.debug = True
	app.run()


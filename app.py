from flask import Flask, render_template, request
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
#import nltk
#nltk.download('stopwords')

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
	text = text.lower()
#	dd="The LNM Institute of Information Technology, is a deemed university located in Jaipur, India, on an 100-acre campus. The institute is a public-private partnership venture between the LNM foundation and the Government of Rajasthan and operates as an autonomous non-profit organization"    
	words_all = word_tokenize(text)
	#imp_words=[]
	imp_words = set()
	string_to_print= "Important words extracted are:  "
	stop_words = set(stopwords.words("english"))

	for w in words_all:
		if w not in stop_words:
			imp_words.add(w)
		
	for unique_Words in imp_words:
		string_to_print = string_to_print + "  |  " + unique_Words

	print(imp_words)
	return string_to_print

if __name__ == '__main__':
	app.debug = True
	app.run()


# import the Flask class from the flask module
from flask import Flask, render_template, request
from gensim.models import KeyedVectors
# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/handle_data', methods=['POST'])
def handle_data():
	word = request.form['projectFilepath']
	filename = 'C:/Users/Shritam/Desktop/Address Data/Siraj/word_vectors_game_of_thrones-LIVE-master/GoogleNews-vectors-negative300.bin'
	# load the google word2vec model

	model = KeyedVectors.load_word2vec_format(filename, binary=True, limit=100000)
	result = model.most_similar(word, topn=10)

	
	return render_template("result.html",result = result)
	# return a response


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
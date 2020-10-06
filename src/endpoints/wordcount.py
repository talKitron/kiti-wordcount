import requests
import operator
import re
import nltk
from flask import Blueprint, jsonify, request, render_template
from flask import current_app as app
from bs4 import BeautifulSoup
from collections import Counter
from src.stop_words import stops
from src.models import Result

wordcount = Blueprint(name='wordcount', import_name='__name__')

@wordcount.route('/test', methods=['GET'])
def home():
    output = {"msg": "You've reached the test endpoint from wordcount"}
    return jsonify(output)


@wordcount.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == 'POST':
        # get user submitted url
        try:
            url = request.form['url']
            r = requests.get(url)
            print(r.text)
        except Exception as e:
            errors.append(
                "Unable to get URL. Please make sure it's a valid URL and try again."
            )
            return render_template('index.html', errors=errors, results=results)
        if r:
            # text processing
            raw = BeautifulSoup(r.text.lower(), 'html.parser').get_text()
            nltk.data.path.append('./src/nltk_data/')
            tokens = nltk.word_tokenize(raw)
            text = nltk.Text(tokens)
            # remove punctuation and count raw words
            nonPunct = re.compile('.*[A-Za-z].*')
            raw_words = [w for w in text if nonPunct.match(w)]
            raw_word_count = Counter(raw_words)
            # stop words
            no_stop_words = [w for w in raw_words if w.lower() not in stops]
            no_stop_words_count = Counter(no_stop_words)
            # save the results
            results = sorted(
                no_stop_words_count.items(),
                key = operator.itemgetter(1),
                reverse = True
            )[:10]
            try:
                result = Result(
                    url = url,
                    result_all = raw_word_count,
                    result_no_stop_words = no_stop_words_count
                )
                result.save()
            except Exception as e:
                # errors.append(str(e))
                errors.append('Unable to add item to database.')
    return render_template('index.html', errors=errors, results=results)

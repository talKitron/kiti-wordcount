from flask import Blueprint, jsonify, request, render_template

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
        except:
            errors.append(
                "Unable to get URL. Please make sure it's a valid URL and try again."
            )
    return render_template('index.html', errors=errors, results=results)

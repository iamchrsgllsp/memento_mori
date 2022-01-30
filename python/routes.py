from __main__ import app, render_template, url_for


@app.route('/test', methods=['GET'])
def test():
    return render_template('home.html')

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

app.run(debug=True)
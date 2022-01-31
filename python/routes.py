from __main__ import app, render_template, url_for


@app.route('/test', methods=['GET'])
def test():
    return render_template('home.html')

@app.route('/', methods=['GET'])
def home():
    user = "dave"
    data = ["hello","world","this is another test"]
    return render_template('home.html',user=user,data=data)

app.run(debug=True)
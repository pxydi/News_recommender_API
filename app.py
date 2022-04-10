from flask import Flask, render_template, g, request, jsonify
import sqlite3
import recommender

app = Flask(__name__)
app.config['SECRET_KEY'] = "Thisisasecret!"

def connect_db():
    sql = sqlite3.connect('/Users/xydi/Documents/python_work/Random/FlaskIntroduction/Udemy/recommender_app/documents.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/document', methods = ['GET', 'POST'])
def document():

    db = get_db()

    if request.method == 'POST':

        category = str(request.form['category'])
        title = str(request.form['title'])
        doc_text = str(request.form['doc_text'])

        db.execute('insert into documents (category, title, doc_text) values (?,?,?)', \
                   [category, title, doc_text])
        db.commit()

    cur = db.execute('select id, category, title, doc_text from documents')
    results = cur.fetchall()

    return render_template('add_document.html',results=results)

@app.route('/similar', methods = ['GET', 'POST'])

def similar():
    if request.method == 'POST':

        sample_text = str(request.form['sample_text'])
        k = request.form['k']
        sample_categories = request.form['sample_categories']


        res = recommender.recommender(sample_text, sample_categories, k)
        return jsonify(res)

    return render_template('find_similar_docs.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, Response, render_template, request, jsonify

from wtforms import TextField, Form, StringField
from model.generate_trigrams import generate_n_text_from_seed
import pickle



app = Flask(__name__)

with open('./model/chains/trump.p', 'rb') as f:
    don_chain=pickle.load(f)

with open('./model/chains/nietzsche.p', 'rb') as f:
    fred_chain=pickle.load(f)

with open('./model/chains/george.p', 'rb') as f:
    george_chain=pickle.load(f)

chain_dict = {'the_donald':don_chain,
              'fred':fred_chain,
              'george':george_chain}

class SearchForm(Form):
    autocomp = StringField('Search', id='nietzsche_autocomplete')




@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    id = request.args.get('char')
    if search and id:

        print(str(id))

        results = generate_n_text_from_seed(chain=chain_dict[id], in_text=str(search),max_char=100)
        return jsonify(matching_results=results)
    else:
        return jsonify(note='use the query string to call the auto complete. For an example paste the example query into the query string after `http://<hostname>/autocomplete` in the url above',
                       example='?q=what+a&char=the_donald')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    print(form)
    return render_template("search.html", form=form)

if __name__ == '__main__':
    app.run(debug=False)

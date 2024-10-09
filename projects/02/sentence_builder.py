from flask import Flask, render_template, request, redirect, url_for
import utils

app = Flask(__name__)

skeleton = {
    "D_0": "",
    "Adj_0": "",
    "N_0": "",
    "Adv": "",
    "V": "",
    "D_1": "",
    "Adj_1": "",
    "N_1": "",
    "TENSE": ""
}

english_words = utils.get_all_words()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_page = request.form.get('opt')
        if selected_page == 'noun':
            return redirect(url_for('noun'))
        elif selected_page == 'pronoun':
            return redirect(url_for('pronoun'))
    return render_template('index.html')


@app.route('/noun', methods=['GET', 'POST'])
def noun():
    if request.method == 'POST':
        selected_page = request.form.get('opt')
        if selected_page == 'with_adjective':
            return redirect(url_for('with_adjective'))
        elif selected_page == 'no_adjective':
            return redirect(url_for('no_adjective'))
    return render_template('noun.html')

@app.route('/with_adjective', methods=['GET', 'POST'])
def with_adjective():
    adjectives = [e[0] for e in english_words['adjectives']]
    form = None
    nouns = []
    if request.method == 'POST':
        form = request.form.get('noun_form')
        if form == 'singular':
            nouns = [e[1] for e in english_words['nouns']]
        elif form == 'plural':
            nouns = [e[2] for e in english_words['nouns']]
        skeleton['N_0'] = request.form.get('noun')
        skeleton['Adj_0'] = request.form.get('adjective')
        if skeleton['Adj_0'] is not None and skeleton['N_0'] is not None:
            return redirect(url_for('adders'))
    return render_template('with_adjective.html', available_nouns=nouns,
                           noun_form=form, available_adjectives=adjectives)


@app.route('/no_adjective', methods=['GET', 'POST'])
def no_adjective():
    form = None
    nouns = []
    if request.method == 'POST':
        form = request.form.get('noun_form')
        if form == 'singular':
            nouns = [e[1] for e in english_words['nouns']]
        elif form == 'plural':
            nouns = [e[2] for e in english_words['nouns']]
        skeleton['N_0'] = request.form.get('noun')
        if skeleton['N_0'] is not None:
            return redirect(url_for('adders'))
    return render_template('no_adjective.html', available_nouns=nouns, noun_form=form)


@app.route('/pronoun', methods=['GET', 'POST'])
def pronoun():
    if request.method == 'POST':
        skeleton['N_0'] = request.form.get('opt')
        return redirect(url_for('adders'))
    return render_template('pronoun.html', words=english_words)


@app.route('/verb', methods=['GET', 'POST'])
def verb():
    noun_or_pronoun = skeleton['N_0']
    nouns_with_s_verb = ['it', 'she', 'he'] + [noun[1] for noun in english_words['nouns']]
    tense = None
    word = None
    verbs = []
    if request.method == 'POST':
        tense = request.form.get('verb_tense')
        if tense == 'past':
            verbs = [e[3] for e in english_words['verbs']]
        elif tense == 'present':
            if noun_or_pronoun not in nouns_with_s_verb:
                verbs = [e[2] for e in english_words['verbs']]
            else:
                verbs = [e[4] for e in english_words['verbs']]
        elif tense == 'future':
            verbs = [e[5] for e in english_words['verbs']]
        skeleton['V'] = request.form.get('verb')
        word = request.form.get('verb')
        if word is not None:
            return redirect(url_for('add_more'))
    return render_template('verb.html', verb_tense=tense, available_verbs=verbs)


@app.route('/adders', methods=['GET', 'POST'])
def adders():
    if request.method == 'POST':
        selected_page = request.form.get('adder')
        if selected_page == 'adverb':
            return redirect(url_for('adverb'))
        elif selected_page == 'no_adjective':
            return redirect(url_for('determiner'))
        elif selected_page == 'nothing':
            return redirect(url_for('verb'))
    return render_template('adders.html')


@app.route('/adverb', methods=['GET', 'POST'])
def adverb():
    if request.method == 'POST':
        skeleton['Adv'] = request.form.get('opt')
        return redirect(url_for('verb'))
    return render_template('adverb.html', words=english_words)


@app.route('/determiner', methods=['GET', 'POST'])
def determiner():
    return render_template('determiner.html')

@app.route('/add_more', methods=['GET', 'POST'])
def add_more():
    if request.method == 'POST':
        selected_page = request.form.get('opt')
        if selected_page == 'yes':
            return redirect(url_for('noun_v2'))
        elif selected_page == 'no':
            return redirect(url_for('sentence'))
    return render_template('add_more.html')


@app.route('/noun_v2', methods=['GET', 'POST'])
def noun_v2():
    if request.method == 'POST':
        selected_page = request.form.get('opt')
        if selected_page == 'with_adjective':
            return redirect(url_for('with_adjective_v2'))
        elif selected_page == 'no_adjective':
            return redirect(url_for('no_adjective_v2'))
    return render_template('noun.html')

@app.route('/with_adjective_v2', methods=['GET', 'POST'])
def with_adjective_v2():
    adjectives = [e[0] for e in english_words['adjectives']]
    form = None
    nouns = []
    if request.method == 'POST':
        form = request.form.get('noun_form')
        if form == 'singular':
            nouns = [e[1] for e in english_words['nouns']]
        elif form == 'plural':
            nouns = [e[2] for e in english_words['nouns']]
        skeleton['N_1'] = request.form.get('noun')
        skeleton['Adj_1'] = request.form.get('adjective')
        if skeleton['Adj_1'] is not None and skeleton['N_1'] is not None:
            return redirect(url_for('sentence'))
    return render_template('with_adjective.html', available_nouns=nouns,
                           noun_form=form, available_adjectives=adjectives)


@app.route('/no_adjective_v2', methods=['GET', 'POST'])
def no_adjective_v2():
    form = None
    nouns = []
    if request.method == 'POST':
        form = request.form.get('noun_form')
        if form == 'singular':
            nouns = [e[1] for e in english_words['nouns']]
        elif form == 'plural':
            nouns = [e[2] for e in english_words['nouns']]
        skeleton['N_1'] = request.form.get('noun')
        if skeleton['N_1'] is not None:
            return redirect(url_for('sentence'))
    return render_template('no_adjective.html', available_nouns=nouns, noun_form=form)

@app.route('/pronoun_v2', methods=['GET', 'POST'])
def pronoun_v2():
    if request.method == 'POST':
        skeleton['N_1'] = request.form.get('opt')
        return redirect(url_for('sentence'))
    return render_template('pronoun.html', words=english_words)

@app.route('/sentence', methods=['GET', 'POST'])
def sentence():
    builded_sentence = ' '.join([skeleton[e] for e in skeleton.keys()])
    return render_template('sentence.html', sentence=builded_sentence)



if __name__ == '__main__':
    app.run(debug=True)
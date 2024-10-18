from flask import Flask, render_template, request, redirect, url_for
import utils

app = Flask(__name__, static_folder='static')

skeleton = {
    "Q": "",
    "D": "",
    "Adj_0": "",
    "N_0": "",
    "V": "",
    "P": "",
    "Adj_1": "",
    "N_1": "",
    "Adv": "",
    "TEMP": ""
}

english_words = utils.get_all_words()


@app.route('/', methods=['GET', 'POST'])
def index():
    for k in skeleton.keys():
        skeleton[k] = ""
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
        return redirect(url_for('adders_no_determiner'))
    return render_template('pronoun.html', words=english_words)


@app.route('/verb', methods=['GET', 'POST'])
def verb():
    noun_or_pronoun = skeleton['N_0']
    nouns_with_s_verb = ['it', 'she', 'he'] + [noun[1] for noun in english_words['nouns']]
    nouns_with_was_verb = ['I', 'it', 'she', 'he'] + [noun[1] for noun in english_words['nouns']]
    tense = None
    mode = None
    word = None
    verbs = []
    if request.method == 'POST':
        tense = request.form.get('verb_tense')
        mode = request.form.get('verb_mode')
        if mode == 'indicative':
            if tense == 'past simple':
                verbs = [e[3] for e in english_words['verbs']]
            elif tense == 'past continuous':
                if noun_or_pronoun not in nouns_with_was_verb:
                    verbs = ['were ' + e[6] for e in english_words['verbs']]
                else:
                    verbs = ['was ' + e[6] for e in english_words['verbs']]
            elif tense == 'past perfect':
                verbs = ['had ' + e[7] for e in english_words['verbs']]
            elif tense == 'past perfect continuous':
                verbs = ['had been ' + e[6] for e in english_words['verbs']]
            elif tense == 'present simple':
                if noun_or_pronoun not in nouns_with_s_verb:
                    verbs = [e[2] for e in english_words['verbs']]
                else:
                    verbs = [e[4] for e in english_words['verbs']]
            elif tense == 'present continuous':
                if noun_or_pronoun == 'I':
                    verbs = ['am ' + e[6] for e in english_words['verbs']]
                elif noun_or_pronoun in nouns_with_s_verb:
                    verbs = ['is ' + e[6] for e in english_words['verbs']]
                else:
                    verbs = ['are ' + e[6] for e in english_words['verbs']]
            elif tense == 'present perfect':
                if noun_or_pronoun not in nouns_with_s_verb:
                    verbs = ['have ' + e[7] for e in english_words['verbs']]
                else:
                    verbs = ['has ' + e[7] for e in english_words['verbs']]
            elif tense == 'present perfect continuous':
                if noun_or_pronoun not in nouns_with_s_verb:
                    verbs = ['have been ' + e[6] for e in english_words['verbs']]
                else:
                    verbs = ['has been ' + e[6] for e in english_words['verbs']]
            elif tense == 'future simple':
                verbs = [e[5] for e in english_words['verbs']]
            elif tense == 'future continuous':
                verbs = ['will be ' + e[6] for e in english_words['verbs']]
            elif tense == 'future perfect':
                verbs = ['will have ' + e[7] for e in english_words['verbs']]
            elif tense == 'future perfect continuous':
                verbs = ['will have been ' + e[6] for e in english_words['verbs']]
        elif mode == 'negation':
            if tense == 'past simple':
                verbs = ["didn't " + e[2] for e in english_words['verbs']]
            elif tense == 'past continuous':
                if noun_or_pronoun not in nouns_with_was_verb:
                    verbs = ["weren't " + e[6] for e in english_words['verbs']]
                else:
                    verbs = ["wasn't " + e[6] for e in english_words['verbs']]
            elif tense == 'past perfect':
                verbs = ["hadn't " + e[7] for e in english_words['verbs']]
            elif tense == 'past perfect continuous':
                verbs = ["hadn't been " + e[6] for e in english_words['verbs']]
            elif tense == 'present simple':
                if noun_or_pronoun not in nouns_with_s_verb:
                    verbs = ["don't " + e[2] for e in english_words['verbs']]
                else:
                    verbs = ["doesn't" + e[2] for e in english_words['verbs']]
            elif tense == 'present continuous':
                if noun_or_pronoun == 'I':
                    verbs = ['am not ' + e[6] for e in english_words['verbs']]
                elif noun_or_pronoun in nouns_with_s_verb:
                    verbs = ["isn't " + e[6] for e in english_words['verbs']]
                else:
                    verbs = ["aren't " + e[6] for e in english_words['verbs']]
            elif tense == 'present perfect':
                if noun_or_pronoun not in nouns_with_s_verb:
                    verbs = ["haven't " + e[7] for e in english_words['verbs']]
                else:
                    verbs = ["hasn't " + e[7] for e in english_words['verbs']]
            elif tense == 'present perfect continuous':
                if noun_or_pronoun not in nouns_with_s_verb:
                    verbs = ["haven't been " + e[6] for e in english_words['verbs']]
                else:
                    verbs = ["hasn't been " + e[6] for e in english_words['verbs']]
            elif tense == 'future simple':
                verbs = ["won't " + e[2] for e in english_words['verbs']]
            elif tense == 'future continuous':
                verbs = ["won't be " + e[6] for e in english_words['verbs']]
            elif tense == 'future perfect':
                verbs = ["won't have " + e[7] for e in english_words['verbs']]
            elif tense == 'future perfect continuous':
                verbs = ["won't have been " + e[6] for e in english_words['verbs']]
        elif mode == 'question':
            if tense == 'past simple':
                verbs = [e[2] for e in english_words['verbs']]
                skeleton['Q'] = 'did'
            elif tense == 'past continuous':
                verbs = [e[6] for e in english_words['verbs']]
                if noun_or_pronoun not in nouns_with_was_verb:
                    skeleton['Q'] = 'were'
                else:
                    skeleton['Q'] = 'was'
            elif tense == 'past perfect':
                verbs = [e[7] for e in english_words['verbs']]
                skeleton['Q'] = 'had'
            elif tense == 'past perfect continuous':
                verbs = ['been ' + e[6] for e in english_words['verbs']]
                skeleton['Q'] = 'had'
            elif tense == 'present simple':
                verbs = [e[2] for e in english_words['verbs']]
                if noun_or_pronoun not in nouns_with_s_verb:
                    skeleton['Q'] = 'do'
                else:
                    skeleton['Q'] = 'does'
            elif tense == 'present continuous':
                verbs = [e[6] for e in english_words['verbs']]
                if noun_or_pronoun == 'I':
                    skeleton['Q'] = 'am'
                elif noun_or_pronoun in nouns_with_s_verb:
                    skeleton['Q'] = 'is'
                else:
                    skeleton['Q'] = 'are'
            elif tense == 'present perfect':
                verbs = [e[7] for e in english_words['verbs']]
                if noun_or_pronoun not in nouns_with_s_verb:
                    skeleton['Q'] = 'have'
                else:
                    skeleton['Q'] = 'has'
            elif tense == 'present perfect continuous':
                verbs = ['been ' + e[6] for e in english_words['verbs']]
                if noun_or_pronoun not in nouns_with_s_verb:
                    skeleton['Q'] = 'have'
                else:
                    skeleton['Q'] = 'has'
            elif tense == 'future simple':
                verbs = [e[2] for e in english_words['verbs']]
                skeleton['Q'] = 'will'
            elif tense == 'future continuous':
                verbs = ['be ' + e[6] for e in english_words['verbs']]
                skeleton['Q'] = 'will'
            elif tense == 'future perfect':
                verbs = ['have ' + e[7] for e in english_words['verbs']]
                skeleton['Q'] = 'will'
            elif tense == 'future perfect continuous':
                verbs = ['have been ' + e[6] for e in english_words['verbs']]
                skeleton['Q'] = 'will'
        skeleton['V'] = request.form.get('verb')
        word = request.form.get('verb')
        if word is not None:
            return redirect(url_for('add_more'))
    return render_template('verb.html', verb_tense=tense, verb_mode=mode, available_verbs=verbs)


@app.route('/adders', methods=['GET', 'POST'])
def adders():
    if request.method == 'POST':
        selected_page = request.form.get('adder')
        if selected_page == 'adverb':
            return redirect(url_for('adverb'))
        elif selected_page in ['article', 'demonstrative', 'possessive', 'quantifier', 'number']:
            skeleton['TEMP'] = selected_page
            return redirect(url_for('determiner'))
        elif selected_page == 'preposition':
            return redirect(url_for('preposition'))
        elif selected_page == 'nothing':
            return redirect(url_for('verb'))
    return render_template('adders.html')


@app.route('/adders_no_determiner', methods=['GET', 'POST'])
def adders_no_determiner():
    if request.method == 'POST':
        selected_page = request.form.get('adder')
        if selected_page == 'adverb':
            return redirect(url_for('adverb'))
        elif selected_page == 'preposition':
            return redirect(url_for('preposition'))
        elif selected_page == 'nothing':
            return redirect(url_for('verb'))
    return render_template('adders_no_determiner.html')


@app.route('/adverb', methods=['GET', 'POST'])
def adverb():
    if request.method == 'POST':
        skeleton['Adv'] = request.form.get('opt')
        if skeleton['N_0'] in [e[0] for e in english_words['pronouns']]:
            return redirect(url_for('adders_no_determiner'))
        else:
            return redirect(url_for('adders'))
    return render_template('adverb.html', words=english_words)


@app.route('/determiner', methods=['GET', 'POST'])
def determiner():
    type = skeleton['TEMP']
    skeleton['TEMP'] = ""
    determiners = [e[1] for e in english_words['determiners'] if e[2] == type]
    if skeleton['N_0'] in [e[2] for e in english_words['nouns']]:
        if type == 'article':
            determiners = ['the']
        elif type == 'demonstrative':
            determiners = ['these', 'those']
        elif type == 'number':
            determiners = [d for d in determiners if d != 'one']
    else:
        if type == 'demonstrative':
            determiners = ['this', 'that']
        elif type == 'number':
            determiners = ['one']
    if request.method == 'POST':
        skeleton['D'] = request.form.get('opt')
        if skeleton['N_0'] in [e[0] for e in english_words['pronouns']]:
            return redirect(url_for('adders_no_determiner'))
        else:
            return redirect(url_for('adders'))
    return render_template('determiner.html', words=determiners)


@app.route('/add_more', methods=['GET', 'POST'])
def add_more():
    if request.method == 'POST':
        selected_page = request.form.get('opt')
        if selected_page == 'yes':
            return redirect(url_for('noun_v2'))
        elif selected_page == 'no':
            return redirect(url_for('sentence'))
    return render_template('add_more.html')


@app.route('/preposition', methods=['GET', 'POST'])
def preposition():
    prepositions = [e[0] for e in english_words['prepositions']]
    if request.method == 'POST':
        skeleton['P'] = request.form.get('opt')
        if skeleton['N_0'] in [e[0] for e in english_words['pronouns']]:
            return redirect(url_for('adders_no_determiner'))
        else:
            return redirect(url_for('adders'))
    return render_template('preposition.html', words=prepositions)


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
    builded_sentence = ' '.join([skeleton[e] for e in skeleton.keys() if skeleton[e] != ""]).capitalize()
    if skeleton['Q'] == "":
        builded_sentence += "."
    else:
        builded_sentence += "?"
    builded_sentence = builded_sentence.replace(' i ', ' I ')
    return render_template('sentence.html', sentence=builded_sentence)


if __name__ == '__main__':
    app.run(debug=True)

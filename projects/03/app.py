from pprint import pprint
import re
import sqlite3

INIT_MSG = """
Welcome to the App!
You can use the following commands:

- Evaluate logical expressions with two operands and operators: AND, OR, XOR
- Assign the result of an expression to a variable, e.g.: `x := finire AND compare`
- View all user-defined variables: `--list`
- Print the value of a specific variable: `-print <variable>`
- Exit the application: `-exit`
- Clear all data: `-clear`

Enter your command below:

"""
PATTERN = r'([a-zA-Z]+ := )?([a-zA-Z]+(\s)*)((AND|OR)(\s)+[a-zA-Z]+)?'
DATABASE = 'db.sql'
variables = dict()
SQL_QUERY = """
select verbs.verb from verbs
join associations on associations.verb = verbs.verb
join lemmas on associations.lemma = lemmas.lemma
join nouns on nouns.lemma = lemmas.lemma
where nouns.noun = '{}'
limit 10;
"""


def handle_sql(noun):
    conn = sqlite3.connect('db.sql')
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY.format(noun))
    x = {_[0] for _ in cursor.fetchall()}
    cursor.close()
    conn.close()
    return x


def get_variable(variable):
    try:
        p = variables[variable]
    except KeyError:
        p = handle_sql(variable)

    return p


def evaluate(x):
    x = x.split()
    if len(x) == 2:
        print("incomplete input")
        return
    elif len(x) == 1:
        return get_variable(x[0])
    if x[1] not in ("AND", "OR", "XOR"):
        print("not a valid logic operator")
        return
    p = get_variable(x[0])
    q = get_variable(x[2])

    if "AND" == x[1]:
        return p.intersection(q)
    elif "OR" == x[1]:
        return p.union(q)
    elif "XOR" == x[1]:
        return p.symmetric_difference(q)
    return NotImplemented


print(INIT_MSG)
while True:
    user_input = input("> ")
    if "-" == user_input[0]:
        if "-exit" == user_input:
            break
        elif "-clear" == user_input:
            variables.clear()
            print("variables cleared")
        elif "-list" == user_input:
            pprint(variables.keys())
        elif len(x := user_input.split(" ")) == 2:
            try:
                pprint(variables[x[1]])
            except KeyError as e:
                print(f"no such variable: {x[1]}")
        elif len(x) == 1:
            print("no variable provided")
        else:
            print("not a valid command")
    else:
        if re.match(PATTERN, user_input) is None:
            print("invalid input")
            continue
        xx = user_input.split(' := ')[::-1]
        rr = evaluate(xx[0])
        if rr is None:
            continue
        if len(xx) == 2:
            variables[xx[1]] = rr
        else:
            pprint(rr)

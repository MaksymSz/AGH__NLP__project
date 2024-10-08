import sqlite3


# (D_0) (Adj_0) N_0 (Adv) V (D_1) (Adj_1) N_1
def get_words(limit=1):
    conn = sqlite3.connect('words.sql')
    cursor = conn.cursor()

    # determiners 0
    cursor.execute(f"select word from determiners order by random() limit {limit};")
    D_0 = cursor.fetchall()

    # adjectives 0
    cursor.execute(f"select word from adjectives order by random() limit {limit};")
    Adj_0 = cursor.fetchall()

    # nouns 0
    cursor.execute(f"select word from nouns order by random() limit {limit};")
    N_0 = cursor.fetchall()

    # adverbs
    cursor.execute(f"select word from adverbs order by random() limit {limit};")
    Adv = cursor.fetchall()

    # verbs
    cursor.execute(f"select * from verbs order by random() limit {limit};")
    V = cursor.fetchall()

    # determiners 1
    cursor.execute(f"select word from determiners order by random() limit {limit};")
    D_1 = cursor.fetchall()

    # adjectives 1
    cursor.execute(f"select word from adjectives order by random() limit {limit};")
    Adj_1 = cursor.fetchall()

    # nouns 1
    cursor.execute(f"select word from nouns order by random() limit {limit};")
    N_1 = cursor.fetchall()
    # # prepositional 1
    # cursor.execute(f"select word from propositional order by random() limit {limit};")
    # P_1 = cursor.fetchall()

    cursor.close()
    conn.close()
    result = zip(D_0, Adj_0, N_0, Adv, V, D_1, Adj_1, N_1)
    #
    # for x in (D_0, Adj_0, N_0, Adv, V, D_1, Adj_1, N_1):
    #     print(x)

    return result

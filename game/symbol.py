import random
def make_symbols(pairs):
    letters = []
    for i in range(pairs):
        letters.append(chr(ord('A') + i))
    symbols = letters * 2
    random.shuffle(symbols)
    return symbols
import pandas

data = pandas.read_csv("day26/nato_phonetic_alphabet.csv", index_col=False)


data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


while True:
    text = input("Enter a word: ").upper().strip()

    if text != "EXIT":
        text_list = [l for l in text]
        for letter in text:
            if letter in data_dict.keys():
                print(f"{letter}: {data_dict[letter]}, ", end="")
        print()
        continue
    break

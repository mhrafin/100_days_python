import pandas

data = pandas.read_csv("day26/nato_phonetic_alphabet.csv", index_col=False)


data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(data_dict)


while True:
    text = input("Enter a word: ").upper().strip()

    if text != "EXIT":
        for letter in text:
            if letter in data_dict.keys():
                print(f"{letter}: {data_dict[letter]}, ", end="")
        print()
        continue
    break

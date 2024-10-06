# TODO: Create a letter using starting_letter.txt

# for each name in invited_names.txt
with open(
    "day24/mail_merge_project/Input/Names/invited_names.txt"
) as invited_name_file:
    names = invited_name_file.readlines()
    # invited_names = []
    for i, name in enumerate(names):
        names[i] = name.replace("\n", "")


print(names)
# print(invited_names)
# Replace the [name] placeholder with the actual name.
with open("day24/mail_merge_project/Input/Letters/starting_letter.txt") as temp:
    template = temp.read()
    template = template.strip()
    print(template)
    # template = template.replace("[name]", "")
    
# Save the letters in the folder "ReadyToSend".
for name in names:
    with open(f"day24/mail_merge_project/Output/ReadyToSend/{name + '.txt'}", mode="w") as current:
        t = template.replace("[name]", name)
        current.write(t)
            

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

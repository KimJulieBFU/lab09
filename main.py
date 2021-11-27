def sort_sentence(sentence):
    new_list = ""

    sentence = sentence.lower()
    stroke = sentence.split(" ")

    stroke.sort(key=len)
    stroke[0] = stroke[0].capitalize()

    for i in range(0, len(stroke)):
        new_list += stroke[i] + " "

    return new_list

import os


def word_to_delete():
    file = open('Zygmunt Berling.txt', "r").read()
    file_split = file.split(' ')

    words_table = ["Podkarpackie", "baseball", "się", "i", "oraz", "nigdy", "dlaczego"]
    for word in range (len(file_split),0,-1):
        if file_split[word-1] in words_table:
            file_split.remove(file_split[word-1])
    print(file_split)


def word_to_replace():
    file = open('Zygmunt Noskowski.txt', "r").read()
    file_split = file.split(' ')
    
    words_table = {'Podkarpackie' : 'Góry', 'i': 'oraz', 'oraz': 'i', 'nigdy': 'prawie nigdy', 'dlaczego': 'czemu'}
    for word in range(len(file_split)):
        if file_split[word - 1] in words_table.keys():
            file_split[word - 1] = words_table.get(file_split[word - 1], word)
    print(file_split)



if __name__ == '__main__':
    word_to_delete()
    #word_to_replace()
# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
print(sum(letter in 'ауоыиэяюёе' for letter in word.lower()))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' '))) # но тут нужно утонять, не все одинокие буквы могут быть словами


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in sentence.split():
    print(i[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
lengths = [ len(token) for token in sentence.split()]
print(sum(lengths)/len(lengths))
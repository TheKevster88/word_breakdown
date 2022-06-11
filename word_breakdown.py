#program that finds the number of vowels and consonants in a word

def get_word():
    while True:
        input_word = input("Please type in your word: ")
        if input_word == '':
            print("input empty. Please enter valid word")
        else:
            break
    word_decipher(input_word)

def word_decipher(input_word):
    word_breakdown = list(input_word)
    #print(word_breakdown)
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    vowels = 0
    number = ['1','2','3','4','5','6','7','8','9','0']
    numbers = 0
    space = [' ']
    spaces = 0
    other = 0
    for letter in word_breakdown:
        if letter in vowel:
            vowels+=1
        elif letter in number:
            numbers+=1
        elif letter in space:
            spaces+=1
        else:
            other+=1
    
    if vowels > 0:
        if vowels == 1:
            print("The word '" + input_word + "' has " + str(vowels) + " vowel.")
        if vowels > 1:
            print("The word '" + input_word + "' has " + str(vowels) + " vowels.")
    else:
        print("The word '" + input_word + "' has no vowels.")
    
    if numbers > 0 :
        if numbers == 1:
            print("The word '" + input_word + "' has " + str(numbers) + " number.")
        if numbers > 1:
            print("The word '" + input_word + "' has " + str(numbers) + " numbers.")
    else:
        print("The word '" + input_word + "' has no numbers.")
    
    if spaces > 0:
        if spaces == 1:
            print("The word '" + input_word + "' has " + str(spaces) + " space.")
        if spaces > 1:
            print("The word '" + input_word + "' has " + str(spaces) + " spaces.")
    else:
        print("The word '" + input_word + "' has no spaces.")
    
    if other > 0:
        if other == 1:
            print("the word '" + input_word + "' has " + str(other) + " other character entry.")
        if other > 1:
            print("the word '" + input_word + "' has " + str(other) + " other character entries.")
    else:
        print("the word '" + input_word + "' has no other character entries.")
        
if __name__ == '__main__':
    get_word()

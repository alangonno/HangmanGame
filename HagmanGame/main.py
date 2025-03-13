import requests 

def findw():
    responsew = requests.get("https://random-word-api.herokuapp.com/word")
    if responsew.status_code == 200:
        return responsew.json()[0]
    else:
        return 'Não foi possivel escolher uma palavra'

def titles(msg):
    print('+=' * 20)
    print(msg.upper().center(40))
    print('+=' * 20)

def hangman():

    word = findw()
    if not word:
        return
    
    wordtry = list(len(word) * '_')
    attempt = 6
    fail = []

    titles('Hangman Game')

    while attempt > 0:
        
        print(f'Word:', ' '.join(wordtry))
        print(f'You have {attempt} attempts yet!')
        print('Letters already tried:', ', '.join(fail))
        print('+=' * 20)

        letter = input('\nWrite a letter:').lower()

        if letter in fail:
            titles('You already tried this letter. Choose another one.')
            continue

        elif letter in word:
            for c in range(0, len(word)):
                if letter == word[c]:
                    wordtry[c] = letter
        
        else:
            titles(f'Do not exist {letter} in word!')
            attempt -= 1
        
        fail.append(letter)

        if ''.join(wordtry) == word:
            titles('Congratulations! You got the word right!')
            titles(f'{word} is the word')
            return     

    titles('You have lost, No more attempts!')
    titles(f'{word} is the word')
    return
        
hangman()
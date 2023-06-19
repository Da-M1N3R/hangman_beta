def reset(secret_word, correct):
    secret_word = list(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct:
            continue
        elif secret_word[i].isalpha():
             secret_word[i] = '_'
        else:
            continue
    secret_word = ''.join(secret_word)
    return secret_word

def check(sw, correct, wrong, guess):
    guess = guess[0]
    if guess in sw and guess not in correct:
        correct.append(guess)
        reset(sw, correct)
    elif guess in correct:
        print('Entered Correctly Already... New Letter Please.')
        pass
    elif guess in wrong:
        print('Recorded Wrong Already... New Letter Please.')
        pass
    else:
        wrong.append(guess)
        reset(sw, correct)
    print(f'Correct characters: {correct}')
    print(f'Wrong characters: {wrong}')


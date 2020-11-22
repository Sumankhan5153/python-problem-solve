print('please input your word:')
word = input()
word = word.casefold()
reversed_word = word[::-1]

if word == reversed_word:
    print('great! it palli')
else:
    print('lol! its not')
import random
rnd_num = random.randint(1,100)

print('Enter any number to guess the computer-generated number.')

num_list = [0]
count = 0

while True:
    try:
# First try
        if count == 0:
            guess_num = int(input('Enter any number from 1 to 100: '))
            num_list.append(guess_num)
            count += 1
            if guess_num <= 100 and guess_num > 0:
                if guess_num == rnd_num:
                    print('CONGRATULATIONS, YOU WON!')
                    print(f'It took you {count} guesses to get it right')
                elif abs(guess_num - rnd_num) <= 10:
                    print('WARM')
                elif abs(guess_num - rnd_num) > 10:
                    print('COLD')
            else:
                print('OUT OF BOUNDS')
# Subsequent tries
        else:
            if count > 0:
                guess_num = int(input('Enter any number from 1 to 100: '))
                num_list.append(guess_num)
                count += 1
                if guess_num <= 100 and guess_num > 0:
                    if guess_num == rnd_num:
                        print('CONGRATULATIONS, YOU WON!')
                        print(f'It took you {count} guesses to get it right')
                        break
                    elif abs(guess_num - rnd_num) < abs(num_list[-2] - rnd_num):
                        print('WARMER')
                    elif abs(guess_num - rnd_num) > abs(num_list[-2] - rnd_num):
                            print('COLDER')
                else:
                    print('OUT OF BOUNDS')
    except:
        print('INVALID INPUT')

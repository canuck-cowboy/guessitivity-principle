import time


def initialize():
    while True:
        try:
            low = int(input('\t- Enter the lower bound of the game (eg. 1): '))
            high = int(input('\t- Enter the higher bound of the game (eg. 100): '))
            # if low > high: swap them
            if low > high:
                low, high = high, low

            print(f'\nAwesome! Now think of a number between [{low}-{high}].')
            break

        except ValueError:
            print('Enter a whole number only')

    print("\nThe AI will try to guess your number. Let's see how many steps it takes!")
    print('-------------------------------------------------------------------------')

    return list(range(low, high+1))


def compute(array):
    count = 0
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:
        try:
            middle_index = (right_index - left_index) // 2 + left_index
            guess = array[middle_index]
            print(f'AI Guess: {guess}')

            count += 1

            feedback = None
            while feedback not in ['h', 'high', 'l', 'low', 'c', 'correct']:
                feedback = input('Is the guess too (H)igh, (L)ow or (C)orrect: ').lower()

            if feedback in ['h', 'high']:
                right_index = middle_index - 1

            elif feedback in ['l', 'low']:
                left_index = middle_index + 1

            elif feedback in ['c', 'correct']:
                return count

        except IndexError:
            print('Inconsistent input')
            break


def main():
    print('Welcome to the Guessitivity Principle Game!')
    print('You will need to set a range for the game first.')
    while True:
        array = initialize()
        start = time.time()
        count = compute(array)
        if count is not None:
            end = time.time()
            elapsed = round(end - start)
            print('-----------------------------------------------------------------------')
            print(f'AI guessed your secret number in {count} attempts, and {elapsed} sec!')
            print('-----------------------------------------------------------------------')

        else:
            print("AI is ready to play, but only if you're honest! Let's keep it fair and fun...")

        print()
        play_again = input('Play again? (y/n): ').lower()
        if play_again not in ['y', 'yes', 'yep', 'yeah', 'ok', 'okay', 'sure']:
            print('Goodbye.')
            break
        print('\n')


if __name__ == '__main__':
    main()
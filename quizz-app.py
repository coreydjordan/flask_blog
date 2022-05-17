def quiz():
    options = """
    1 - blah blah blah
    2 - bleh bleh bleh
    """
    print(options)
    correct = 0
    user_choice = int(input('which option is a lie, select 1 or 2 '))
    if user_choice == 1:
        correct += 5
        print(f'that is correct you have {correct} points')
    elif user_choice == 2:
        correct -= 5
        print(f'sorry, try again. you have {correct} points')
    else:
        print('please make a valid selection!')
    if correct >= 5:
        print('you got a perfect score.')
    elif correct < 5:
        print('you did not get a perfect score.')

quiz()
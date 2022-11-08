import numpy as np

def random_predict(number:int=1) -> int:
    """Guessing a number using the binary method

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Number of attempts
    """

    count = 0
    bottom_limit = 1    
    upper_limit = 101   
    predict_number = (bottom_limit+upper_limit) // 2   # estimated number

    while True:
        count += 1
                
        if number == predict_number:
            break # exit from the loop if guessed right
        if number > predict_number:
            bottom_limit = predict_number
            predict_number = (bottom_limit+upper_limit) // 2
        if number < predict_number:
            upper_limit = predict_number
            predict_number = (bottom_limit+upper_limit) // 2    
    return(count)

#print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """For how many attempts on average out of 1000 approaches our algorithm guesses

    Args:
        random_predict ([type]): guess function

    Returns:
        int: average number of tries
    """

    count_ls = [] # list to save the number of attempts
    np.random.seed(1) # fix seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) # made a list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # find the average number of attempts

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)
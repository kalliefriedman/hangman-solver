import requests


def make_guess(game_id, guess):
    """Takes in a game_id and guess as params and returns python dict containing response"""
    response = requests.post("http://int-sys.usr.space/hangman/games/"+game_id+"/guesses", data={'char': guess})
    return response.json()


def start_game(email):
    """Takes in an email as a string and returns python dict containing response"""
    response = requests.post('http://int-sys.usr.space/hangman/games', data={'email': email})
    return response.json()


def play_game(email):
    decoded_response = start_game(email)

    # setting inital variables from response
    game_id = decoded_response["gameId"]
    word = decoded_response["word"]
    guesses_left = decoded_response["guessesLeft"]

    # letters in alphabet in order from most to least frequently occuring
    letters_to_guess = "EARIOTNSLCUDPMHGBFYWKVXZJQ"

    # creating counter to loop through letters_to_guess string by index
    counter = 0
    msg = ""

    # guessing and resetting variables with response from API
    while guesses_left > 0 and msg is not "Congrats! You have solved this hangman!":
        decoded_guess_response = make_guess(game_id, letters_to_guess[counter])
        msg = decoded_guess_response["msg"]
        counter += 1
        guesses_left = decoded_guess_response["guessesLeft"]
        word = decoded_guess_response["word"]
        print word

    if msg is not "Congrats! You have solved this hangman!":
        print msg
        print "The word was " + word
    else:
        print msg

# starting game
email = raw_input("Enter your email to play: ")
play_game(email)

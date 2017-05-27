import requests
from sys import argv
from pprint import pprint
import json


def get_status(game_id):
    """ """
    response = requests.get("http://int-sys.usr.space/hangman/games/" + game_id)
    return response.json()

def make_guess(game_id, guess):
    """ """
    response = requests.post("http://int-sys.usr.space/hangman/games/"+game_id+"/guesses", data={'char': guess})
    return response.json()


def play_game(email):
    response = requests.post('http://int-sys.usr.space/hangman/games', data={'email': email})
    decoded_response = response.json()
    game_id = decoded_response["gameId"]
    word = decoded_response["word"]
    guesses_left = decoded_response["guessesLeft"]
    letters_to_guess = "EARIOTNSLCUDPMHGBFYWKVXZJQ"
    counter = 0
    while guesses_left > 0 and "_" in word:
        decoded_guess_response = make_guess(game_id, letters_to_guess[counter])
        counter += 1
        decoded_status_response = get_status(game_id)
        word = decoded_status_response["word"]
        guesses_left = decoded_guess_response["guessesLeft"]
        print word

    if guesses_left:
        print "You Won!"
        print "The word was " + word
    else:
        print "Nice try, you didn't guess it. Here's how far you got."
        print "The word was " + word

email = raw_input("Enter your email to play: ")
play_game(email)

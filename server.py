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
    msg = ""
    while guesses_left > 0 and msg is not "Congrats! You have solved this hangman!":
        decoded_guess_response = make_guess(game_id, letters_to_guess[counter])
        print decoded_guess_response
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

email = raw_input("Enter your email to play: ")
play_game(email)

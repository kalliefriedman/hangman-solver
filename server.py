import requests
from sys import argv
from pprint import pprint
import json

def start_game(email):
    """ """
    return response
    # game_id = response["game_id"]
    # word = response["gameId"]
    # guesses_left = response["guessesLeft"]


def get_status(game_id):
    """ """
    response = requests.get("http://int-sys.usr.space/hangman/games/" + game_id)
    # word = response["word"]
    # guesses_left = response["guessesLeft"]
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
    while guesses_remaining > 0 and WORD DOESN"T CONTAIN "_":
        decoded_guess_response = make_guess(game_id, letters_to_guess[counter])
        counter += 1
        decoded_status_response = get_status(game_id)
        word = decoded_status_response["word"]
        guesses_left = decoded_guess_response["GuessesLeft"]

    # if guesses remaining then print "YOU WON, the word is ""
    # if no guesses remining print "here's what you got so far. Good try"

email = raw_input("Enter your email to play: ")
play_game(email)

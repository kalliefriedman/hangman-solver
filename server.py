import requests

EARIOTNSLCUDPMHGBFYWKVXZJQ

def start_game(email):
    """ """
    response = requests.post('http://int-sys.usr.space/hangman/games', data={'email': email})
    game_id = response["game_id"]
    word = response["gameId"]
    guesses_left = response["guessesLeft"]


def get_status(game_id):
    """ """
    response = requests.get("http://int-sys.usr.space/hangman/games/" + game_id)
    game_id = response["gameId"]
    word = response["word"]
    guesses_left = response["guessesLeft"]
    active = response["active"]


def make_guess(game_id, guess):
    """ """
    response = requests.post("http://int-sys.usr.space/hangman/games/"+game_id+"/guesses", data={'char': guess})
    guesses_left = response["GuessesLeft"]
    active = response["active"]
    msg = response["msg"]
import os
import random
from flask import Flask, jsonify
from dotenv import load_dotenv

# load env file for the user name
load_dotenv()

app = Flask(__name__)


@app.route('/api')
def get_recipe():
    #get user_name from file, if it doesn't use "Guest" as fallback
    user_name = os.getenv("USER_NAME", "Guest")

    # Read the inventory file
    try:
        with open("inventory.txt", "r") as file:
            # split the file by lines, into an ingredient list
            ingredients = [line.strip() for line in file.readlines() if line.strip()]
    #if file does not exist create an empty list as fallback
    except FileNotFoundError:
        ingredients = []

    #logic for recipe, if you have no ingredients, prompt to go buy some
    if not ingredients:
        suggestion = "Your fridge is empty. go to the supermarket!"
    #if we do have ingredients, choose by random and suggest making using the chosen ingredient
    else:
        chosen_ingredient = random.choice(ingredients)
        suggestion = f"How about making something delicious with {chosen_ingredient}?"

    #return reply in JSON format
    return jsonify({
        "greeting": f"Hello {user_name}!",
        "inventory": ingredients,
        "suggestion": suggestion
    })


if __name__ == '__main__':
    # run server on port 5000, listen to any oncoming requests
    #use host = '0.0.0.0' to make sure we listen to all devices
    app.run(host='0.0.0.0', port=5000)
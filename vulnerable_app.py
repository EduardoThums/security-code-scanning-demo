from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/catch', methods=['POST'])
def catch_pokemon():
    pokemon = request.get_json()['pokemon']

    with open('pokedex.txt', 'a') as pokedex:
        pokedex.write(f'{pokemon}\n')

    return jsonify({'message': f'Congratulations, you have added the {pokemon} pokemon into your pokedex!'})


@app.route('/pokedex')
def view_pokedex():
    pokemons = []
    
    with open('pokedex.txt') as pokedex:
        for pokemon in pokedex.readlines():
            pokemon = pokemon.replace('\n', '')

            pokemons.append(pokemon)

    return jsonify({'pokemons': pokemons})


if __name__ == '__main__':
    app.run()

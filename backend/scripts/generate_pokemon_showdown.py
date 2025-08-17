from pokemendel_core.data.gen3 import PokemonGen3
from pokemendel_core.data import fetch_pokemon
from pokemendel_core.utils.definitions.genders import Genders
from scripts.showdown_movesets import MOVESETS
from typing import List
import random



def choose_gender(pokemon) -> str:
    if Genders.GENDERLESS in pokemon.supported_genders:
        return ""

    selected_gender = (
        pokemon.supported_genders[0]
        if len(pokemon.supported_genders) == 1
        else random.choice(pokemon.supported_genders)
    )
    return "(M)" if selected_gender == Genders.MALE else "(F)"


def get_moveset(gen: int, pokemon_name: str) -> List[str]:
    assert gen in MOVESETS, "Generation was not supported in movesets"
    gen_movesets = MOVESETS[gen]
    assert pokemon_name, f"Pokemon {pokemon_name} is not in gen {gen} moveset"
    pokemon_moves = gen_movesets[pokemon_name]
    assert 1 <= len(pokemon_moves) <= 4, f"Pokemon {pokemon_name} in gen {gen} is not between 1 and 4"
    return pokemon_moves


def generate_showdown_format(gen, name, nickname=None, item=None, set_gender=True):
    moves = get_moveset(gen, name)

    pokemon = fetch_pokemon(name, gen)

    # Format the Pokémon name and optional nickname
    header = f"{name} ({nickname})" if nickname else name

    # Default values (can be expanded based on user input)
    item = f"@ {item}" if item else ""
    gender = choose_gender(pokemon)
    ability = ""  # "Ability: Unknown"
    level = "Level: 5"  # Default level
    evs = "EVs: 0 HP / 0 Atk / 0 Def / 0 SpA / 0 SpD / 1 Spe"
    nature = ""  # "Adamant Nature"
    happiness = "Friendship: 50"

    # Format moves
    move_list = "\n".join(f"- {move}" for move in moves)
    details = "\n".join(filter(None, [ability, level, happiness, evs, nature]))

    # Assemble the final format
    showdown_export = f"""
{header} {gender} {item}
{details}   
{move_list}  
""".strip()

    return showdown_export


if __name__ == "__main__":
    output = generate_showdown_format(
        gen=2,
        name=PokemonGen3.ARTICUNO,
        nickname="Steve",
        # item="Leaf Stone",
    )
    print(output)

from pokemendel_core.data.gen3 import PokemonGen3
from pokemendel_core.data import fetch_pokemon
from pokemendel_core.utils.definitions.genders import Genders
import random

LATEST_GEN = 3


def choose_gender(pokemon) -> str:
    if Genders.GENDERLESS in pokemon.supported_genders:
        return ""

    selected_gender = (
        pokemon.supported_genders[0]
        if len(pokemon.supported_genders) == 1
        else random.choice(pokemon.supported_genders)
    )
    return "(M)" if selected_gender == Genders.MALE else "(F)"


def generate_showdown_format(name, moves, nickname=None, item=None, set_gender=True):
    if not (1 <= len(moves) <= 4):
        raise ValueError("A Pokémon must have between 1 and 4 moves.")

    pokemon = fetch_pokemon(name, LATEST_GEN)

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
        name=PokemonGen3.AERODACTYL,
        nickname="Monica",
        item="Moon Stone",
        moves=[
            "Wing Attack",
            # "Tail Whip",
            # "Encore",
        ],
    )
    print(output)

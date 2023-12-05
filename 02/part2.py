def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read().split("\n")


def fn_prep_data(p_puzzle_data: list) -> dict:
    dt_data = {}
    for ligne in p_puzzle_data:
        dt_game = {}  # Une game
        game, cubes = ligne.split(":")
        # Extraire le game ID, en str
        game_id = ""
        for num in game:
            if num.isdigit():
                game_id += num
        # Extraire les cubes, par tour
        for num_tour, tour in enumerate(cubes.split(";")):
            dt_tour = {"red": 0, "green": 0, "blue": 0}
            for cube in tour.split(","):
                nb_cubes = ""
                couleur_cubes = ""
                for car in cube:
                    if car.isdigit():
                        nb_cubes += car
                    else:
                        couleur_cubes += car
                dt_tour.update({couleur_cubes.strip(): int(nb_cubes.strip())})
            dt_game.update({f"{num_tour + 1}": dt_tour})
        dt_data.update({game_id: dt_game})
    return dt_data


def do_solution_2() -> int:
    puzzle_data = fn_lire_data("puzzle")
    dt_games = fn_prep_data(puzzle_data)
    # Valider only 12 red cubes, 13 green cubes, and 14 blue cubes, par tour
    somme = 0
    for game_id, tours in dt_games.items():
        # Trouver le plus de cubes rouge, vert et bleu dans une game
        max_red = 0
        max_green = 0
        max_blue = 0
        for num_tour, tour in tours.items():
            if tour.get("red") > max_red:
                max_red = tour.get("red")
            if tour.get("green") > max_green:
                max_green = tour.get("green")
            if tour.get("blue") > max_blue:
                max_blue = tour.get("blue")
        somme += max_red * max_green * max_blue

    # The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
    # The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively.
    # Adding up these five powers produces the sum 2286.
    return somme


if __name__ == "__main__":
    print(do_solution_2())

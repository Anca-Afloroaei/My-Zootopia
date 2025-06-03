import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')


def print_animals_info(data):
    """
    Print selected information about each animal.
    """
    for animal in data:
        if "name" in animal:
            print(f"Name: {animal["name"]}")

        if "characteristics" in animal and animal["characteristics"]:
            characteristics = animal["characteristics"]
        else:
            characteristics = {}

        if "diet" in characteristics:
            print(f"Diet: {characteristics['diet']}")

        if "locations" in animal and len(animal["locations"]) > 0:
            print(f"Location: {animal['locations'][0]}")

        if "type" in characteristics:
            print(f"Type: {characteristics['type']}")

        print("\n")

def main():
    """
    Main function to load animal data and print animal info.
    """
    animals_data = load_data('animals_data.json')
    print_animals_info(animals_data)

if __name__ == "__main__":
    main()




# def print_animal_details(animals):
#     """Prints key details for each animal."""
#     for animal in animals:
#         name = animal.get("name")
#         diet = animal.get("characteristics", {}).get("diet")
#         locations = animal.get("locations", [])
#         type_ = animal.get("characteristics", {}).get("type")
#
#         if name:
#             print(f"Name: {name}")
#         if diet:
#             print(f"Diet: {diet}")
#         if locations:
#             print(f"Location: {locations[0]}")
#         if type_:
#             print(f"Type: {type_}")
#         print()  # Blank line between animals
#
# def main():
#     """Main execution function."""
#     animals_data = load_data("animals_data.json")
#     print_animal_summary(animals_data)
#
# if __name__ == "__main__":
#     main()

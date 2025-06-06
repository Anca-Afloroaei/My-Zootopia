import json


def load_data(file_path):
    """Loads data from the JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def load_template(file_path):
    """Loads HTML template content from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def serialize_animal(animal):
    """
    Convert a single animal object into a formatted HTML <li> block.
    """
    output = '<li class="cards__item">\n'

    if "name" in animal:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    if "characteristics" in animal:
        characteristics = animal["characteristics"]
        if "diet" in characteristics:
            output += f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'
        if "type" in characteristics:
            output += f'    <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    if "locations" in animal and animal["locations"]:
        output += f'    <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'

    return output


def generate_animals_info_string(data):
    """
    Generate an HTML-formatted string containing all animals' information.
    """
    output = ""
    for animal in data:
        output += serialize_animal(animal)
    return output


def build_html_page(output_string, template_string, output_file):
    """
    Replace the placeholder in the template with the output string
    and write to a new HTML file.
    """
    html_content = template_string.replace("__REPLACE_ANIMALS_INFO__", output_string)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)


def main():
    animals_data = load_data("animals_data.json")
    template = load_template("animals_template.html")
    animals_info_str = generate_animals_info_string(animals_data)
    build_html_page(animals_info_str, template, "animals.html")


if __name__ == "__main__":
    main()









# import json
#
#
# def load_data(file_path):
#     """ Loads data from the JSON file """
#     with open(file_path, "r", encoding="utf-8") as handle:
#         return json.load(handle)
#
#
# def load_template(file_path):
#     """
#     Load HTML template content from a file.
#     """
#     with open(file_path, "r", encoding="utf-8") as file:
#         return file.read()
#
#
# def generate_animals_info_string(data):
#     """
#     Generate an HTML-formatted string containing the required animals' information,
#     with full semantic structure.
#     """
#     output = ""
#     for animal in data:
#         name = animal["name"] if "name" in animal else "Unknown"
#         characteristics = animal["characteristics"] if "characteristics" in animal else {}
#         diet = characteristics["diet"] if "diet" in characteristics else "Unknown"
#         location = animal["locations"][0] if "locations" in animal and animal["locations"] else "Unknown"
#         animal_type = characteristics["type"] if "type" in characteristics else "Unknown"
#
#         output += '<li class="cards__item">\n'
#         output += f'  <div class="card__title">{name}</div>\n'
#         output += '  <p class="card__text">\n'
#         output += f'    <strong>Diet:</strong> {diet}<br/>\n'
#         output += f'    <strong>Location:</strong> {location}<br/>\n'
#         output += f'    <strong>Type:</strong> {animal_type}<br/>\n'
#         output += '  </p>\n'
#         output += '</li>\n'
#
#     return output
#
#
#
# # def generate_animals_info_string(data):
# #     """
# #     Generate an HTML-formatted string containing the required animals' information.
# #     """
# #     output = ""
# #     for animal in data:
# #         output += '<li class="cards__item">\n'
# #
# #         # Name
# #         if "name" in animal:
# #             output += f"Name: {animal['name']}<br/>\n"
# #
# #         # Extract characteristics - dictionary
# #         characteristics = animal["characteristics"] if "characteristics" in animal else {}
# #
# #         # Add Diet -if it exists
# #         if "diet" in characteristics:
# #             output += f"Diet: {characteristics['diet']}<br/>\n"
# #
# #         # Add first Location - if it exists
# #         if "locations" in animal and len(animal["locations"]) > 0:
# #             output += f"Location: {animal['locations'][0]}<br/>\n"
# #
# #         # Add Type - if it exists
# #         if "type" in characteristics:
# #             output += f"Type: {characteristics['type']}<br/>\n"
# #
# #         output += "</li>\n"
# #     return output
#
#
#
#
# # def generate_animals_info_string(data):
# #     """
# #     Generate a formatted string containing the required animals' information.
# #     """
# #     output = ""
# #     for animal_data in data:
# #         # Add Name
# #         if "name" in animal_data:
# #             output += f"Name: {animal_data['name']}\n"
# #
# #         # Extract characteristics - dictionary
# #         if "characteristics" in animal_data and animal_data["characteristics"]:
# #             characteristics = animal_data["characteristics"]
# #         else:
# #             characteristics = {}
# #
# #         # Add Diet -if it exists
# #         if "diet" in characteristics:
# #             output += f"Diet: {characteristics['diet']}\n"
# #
# #         # Add first Location - if it exists
# #         if "locations" in animal_data and len(animal_data["locations"]) > 0:
# #             output += f"Location: {animal_data['locations'][0]}\n"
# #
# #         # Add Type - if it exists
# #         if "type" in characteristics:
# #             output += f"Type: {characteristics['type']}\n"
# #
# #         # adding an extra line between animals for better readability
# #         output += "\n"
# #     return output
#
# def build_html_page(output_string, template_string, output_file):
#     """
#     Replace the placeholder in the template with the output string
#     and write to a new HTML file.
#     """
#     html_content = template_string.replace("__REPLACE_ANIMALS_INFO__", output_string)
#     with open(output_file, "w", encoding="utf-8") as file:
#         file.write(html_content)
#
# def main():
#     animals_data = load_data("animals_data.json")
#     template = load_template("animals_template.html")
#     animals_info_str = generate_animals_info_string(animals_data)
#     build_html_page(animals_info_str, template, "animals.html")
#
# if __name__ == "__main__":
#     main()
#
#
#
#
#
# # animals_data = load_data('animals_data.json')
# #
# #
# # def print_animals_info(data):
# #     """
# #     Print selected information about each animal.
# #     """
# #     for animal in data:
# #         if "name" in animal:
# #             print(f"Name: {animal["name"]}")
# #
# #         if "characteristics" in animal and animal["characteristics"]:
# #             characteristics = animal["characteristics"]
# #         else:
# #             characteristics = {}
# #
# #         if "diet" in characteristics:
# #             print(f"Diet: {characteristics['diet']}")
# #
# #         if "locations" in animal and len(animal["locations"]) > 0:
# #             print(f"Location: {animal['locations'][0]}")
# #
# #         if "type" in characteristics:
# #             print(f"Type: {characteristics['type']}")
# #
# #         print("\n")
# #
# # def main():
# #     """
# #     Main function to load animal data and print animal info.
# #     """
# #     animals_data = load_data('animals_data.json')
# #     print_animals_info(animals_data)
# #
# # if __name__ == "__main__":
# #     main()
#
#
#
#
# # def print_animal_details(animals):
# #     """Prints key details for each animal."""
# #     for animal in animals:
# #         name = animal.get("name")
# #         diet = animal.get("characteristics", {}).get("diet")
# #         locations = animal.get("locations", [])
# #         type_ = animal.get("characteristics", {}).get("type")
# #
# #         if name:
# #             print(f"Name: {name}")
# #         if diet:
# #             print(f"Diet: {diet}")
# #         if locations:
# #             print(f"Location: {locations[0]}")
# #         if type_:
# #             print(f"Type: {type_}")
# #         print()  # Blank line between animals
# #
# # def main():
# #     """Main execution function."""
# #     animals_data = load_data("animals_data.json")
# #     print_animal_summary(animals_data)
# #
# # if __name__ == "__main__":
# #     main()

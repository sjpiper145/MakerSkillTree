#!/bin/env python

import argparse
import os
import yaml


def load_yaml(file_path):
    with open(file_path) as file:
        return yaml.safe_load(file)


def load_svg_template(file_path):
    with open(file_path) as file:
        return file.read()


def make_text_multiline(text: list, length1: int = 18, length2: int = 25) -> str:
    """Split long one-line strings into multiple-lines strings with a maximum length."""

    # To follow the shape of the hexagon the first line should
    # be smaller, maybe to 18 characters.

    desired_l = length1  # for line 1
    processed_str_len = 0

    space_indexes = [i for i, char in enumerate(text) if char == " "]
    for i in range(1, len(space_indexes)):
        if space_indexes[i] < desired_l + processed_str_len:
            # substring fit in the line, keep searching
            pass
        else:
            # substring is greater than permissible length
            text[space_indexes[i - 1]] = "&#10;"  # break line on previous space
            desired_l = length2  # for lines 2, 3, 4, ...
            processed_str_len += space_indexes[i - 1] - 1

    return "".join(text)


def process_svg(template, data):
    # Replace title and footer
    processed = template.replace("{{ title }}", data["title"])
    processed = processed.replace("{{ footer }}", data["footer"])

    displacement = (0, 9, 19, 29, 39, 49, 59, 69)
    for i in range(10):
        for j in range(7):
            if i < 9:
                box_number = i + displacement[j]
            elif i == 9:
                box_number = i + displacement[j + 1]
                if j >= 5:
                    continue
            value = data["row"][i][j]
            splitted_string = make_text_multiline(list(value))
            placeholder = f"{{{{ box_{box_number:03d} }}}}"
            processed = processed.replace(placeholder, splitted_string)

    return processed


def save_processed_svg(content, output_path):
    with open(output_path, "w") as file:
        file.write(content)


def main():
    script_path = os.path.dirname(os.path.abspath(__file__))
    svg_template_path = os.path.join(script_path, "skill_tree_template.svg.j2")

    parser = argparse.ArgumentParser(description="Process SVG template with YAML data.")
    parser.add_argument("input_yaml", help="Path to input YAML file")
    parser.add_argument("output_svg", help="Path to output processed SVG file")
    args = parser.parse_args()

    # Load YAML data
    yaml_data = load_yaml(args.input_yaml)

    # Load SVG template
    svg_template = load_svg_template(svg_template_path)

    # Process SVG
    processed_svg = process_svg(svg_template, yaml_data)

    # Save processed SVG
    save_processed_svg(processed_svg, args.output_svg)

    print(f"Processed SVG saved to {args.output_svg}")


if __name__ == "__main__":
    main()

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


def process_svg(template, data):
    # Replace title and author
    processed = template.replace("{{ title }}", data["title"])
    processed = processed.replace("{{ author }}", data["author"])

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
            placeholder = f"{{{{ box_{box_number:03d} }}}}"
            processed = processed.replace(placeholder, str(value))

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

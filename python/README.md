# Skill Tree SVG Generator

## Overview
This Python script generates SVG skill trees from YAML input files using a predefined SVG template. It is part of the MakerSkillTree project, which creates interactive skill tracking visualizations.

## Files in this Directory
- `create_skill_tree_svg.py`: Main Python script for generating SVG skill trees
- `skill_tree_template.svg.j2`: Jinja2-style SVG template used as the base for skill tree generation
- `input.yml`: Example input YAML file demonstrating the required data structure
- `requirements.txt`: Lists Python package dependencies

## Requirements
- Python 3.x
- PyYAML library

## Installation
1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
```bash
python create_skill_tree_svg.py input.yml output.svg
```

### Parameters
- `input.yml`: Path to the YAML file containing skill tree data
- `output.svg`: Path where the generated SVG will be saved

## YAML Input Format
The input YAML file should contain:
- `title`: The title of the skill tree
- `footer`: Footer text for the SVG
- `row`: A 2D list representing the skill tree content, with 10 rows and 7 columns

## Example YAML
```yaml
title: My Skill Tree
footer: © 2023 My Organization
row:
  0: ['Skill 1', 'Skill 2', 'Skill 3', '', '', '', '']
  1: ['Skill 4', 'Skill 5', 'Skill 6', '', '', '', '']
  # ... more rows following the same pattern
```

## Dependencies
- argparse (Python standard library)
- os (Python standard library)
- PyYAML

## Template
The script uses a Jinja2-style SVG template (`skill_tree_template.svg.j2`) with placeholders for dynamically inserting skill tree content.

## License
Part of the MakerSkillTree project. See the main repository for licensing details.

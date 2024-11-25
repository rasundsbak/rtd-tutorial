import os
import re

def collect_notes(source_dir, output_file):
    note_pattern = re.compile(r'\.\. note::\n\n((?:[ \t]+.+\n)+)')
    all_notes = []

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.rst'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as rst_file:
                    content = rst_file.read()
                    notes = note_pattern.findall(content)
                    all_notes.extend(notes)

    with open(output_file, 'w') as out_file:
        for note in all_notes:
            out_file.write(".. note::\n\n")
            out_file.write(note)
            out_file.write("\n")

if __name__ == "__main__":
    source_directory = "./docs"  # Adjust this to your source directory
    output_filename = "./docs/note_collection.rst"  # Adjust this to your desired output file
    collect_notes(source_directory, output_filename)


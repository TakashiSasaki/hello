# Filename: convert_webp_to_ico.py

import sys
from PIL import Image
import os

def convert_webp_to_ico(input_file):
    # Change the extension of the input file to .ico
    base = os.path.splitext(input_file)[0]
    output_file = f"{base}.ico"

    # Open the WebP image
    img = Image.open(input_file)

    # Convert and save the image as ICO
    # The sizes argument specifies the sizes to include in the ICO file
    img.save(output_file, format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])

    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    # Check if the input file was provided
    if len(sys.argv) != 2:
        print("Usage: python convert_webp_to_ico.py <input_file.webp>")
        sys.exit(1)

    # Get the input file from the command line arguments
    input_file = sys.argv[1]

    # Convert the WebP file to ICO
    convert_webp_to_ico(input_file)

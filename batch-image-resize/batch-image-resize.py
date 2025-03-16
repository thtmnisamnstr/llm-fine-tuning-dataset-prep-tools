import os
from PIL import Image
import argparse

def resize_and_save_image(input_path, output_path, shortest_side_length):
    """
    Resize an image proportionally so that its shortest side equals shortest_side_length.
    
    :param input_path: Path to the input image file.
    :param output_path: Desired path for saving the resized image in .png format.
    :param shortest_side_length: Length of the shortest side after resizing.
    """
    with Image.open(input_path) as img:
        # Calculate new dimensions maintaining aspect ratio
        original_width, original_height = img.size
        if original_width > original_height:
            new_height = shortest_side_length
            new_width = int(new_height * (original_width / original_height))
        else:
            new_width = shortest_side_length
            new_height = int(new_width * (original_height / original_width))
        
        # Resize the image
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        
        # Save the resized image in .png format
        resized_img.save(output_path, 'PNG')

def process_directory(input_dir, output_dir, shortest_side_length):
    """
    Process all .tif, .png, and .jpg files within input_dir and its subdirectories,
    resizing them and saving to output_dir.
    
    :param input_dir: Directory from which to read images.
    :param output_dir: Directory where resized images will be saved.
    :param shortest_side_length: Length of the shortest side after resizing.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Walk through all directories and files in input_dir
    image_count = 0
    total_images = 0
    
    # First pass to count total images
    for root, dirs, files in os.walk(input_dir):
        # Exclude hidden directories (names starting with a period)
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            # Exclude hidden files (names starting with a period)
            if file.startswith('.'):
                continue
            if file.lower().endswith(('.tif', '.png', '.jpg')):
                total_images += 1
    
    # Second pass to process and resize images
    for root, dirs, files in os.walk(input_dir):
        # Exclude hidden directories (names starting with a period)
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            # Exclude hidden files (names starting with a period)
            if file.startswith('.'):
                continue
            if file.lower().endswith(('.tif', '.png', '.jpg')):
                image_count += 1
                input_path = os.path.join(root, file)
                
                # Construct the output path
                relative_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, relative_path)
                if not os.path.exists(output_subdir):
                    os.makedirs(output_subdir)
                output_file_name = os.path.splitext(file)[0] + '.png'
                output_path = os.path.join(output_subdir, output_file_name)
                
                # Print the current image being processed
                print(f"Processing image {image_count}/{total_images}: {input_path}")
                
                # Resize and save the image
                resize_and_save_image(input_path, output_path, shortest_side_length)

def main():
    parser = argparse.ArgumentParser(description="Resize images in a directory to a specified shortest side length.")
    parser.add_argument("input_dir", help="Input directory containing images")
    parser.add_argument("output_dir", help="Output directory for resized images")
    parser.add_argument("shortest_side_length", type=int, help="Length of the shortest side after resizing")

    args = parser.parse_args()

    input_directory = args.input_dir
    output_directory = args.output_dir
    target_shortest_side = args.shortest_side_length

    process_directory(input_directory, output_directory, target_shortest_side)

if __name__ == "__main__":
    main()
import os
import glob
import re

def remove_headmatter_and_images(mdx_content):
    """
    Remove YAML front matter and image references from MDX content.
    
    Args:
        mdx_content (str): The input MDX content as a string.
        
    Returns:
        str: The cleaned content with head matter, images, HTML tags, and excessive newlines removed.
    """
    # Regular expression to match YAML front matter (headmatter)
    headmatter_pattern = re.compile(r'^---\s*.*?\s*---\s*', re.DOTALL | re.MULTILINE)
    # Remove headmatter from the content
    content_without_headmatter = headmatter_pattern.sub('', mdx_content).strip()
    
    # Remove the bolded first line each if it exists
    lines = content_without_headmatter.splitlines()
    if lines and lines[0].startswith('**') and lines[0].endswith('**'):
        lines.pop(0)  # Remove the first line if it's bold
    
    # Join lines back into a single string
    clean_content = '\n'.join(lines)
    
    # Remove all image references
    image_reference_pattern = re.compile(r'!\[.*?\]\(.*?\)')
    clean_content = image_reference_pattern.sub('', clean_content).strip()
    
    # Replace <br> tags with Markdown line breaks
    br_tag_pattern = re.compile(r'<br\s*/?>')
    clean_content = br_tag_pattern.sub('  \n', clean_content).strip()
    
    # Remove all HTML tags from the content
    html_tag_pattern = re.compile(r'<[^>]+>')
    clean_content = html_tag_pattern.sub('', clean_content).strip()
    
    # Normalize multiple successive newlines: reduce sequences of 3 or more to exactly two newlines
    normalize_newlines_pattern = re.compile(r'\n{3,}')
    normalized_content = normalize_newlines_pattern.sub('\n\n', clean_content.strip())
    
    return normalized_content

def process_blog_posts(source_directory, output_directory):
    """
    Process all MDX files in a source directory by removing head matter and images,
    then save the cleaned content to an output directory as Markdown files.
    
    Args:
        source_directory (str): The path to the directory containing .mdx files.
        output_directory (str): The path to the directory where cleaned .md files will be saved.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Get all .mdx files in the source directory
    mdx_files = glob.glob(os.path.join(source_directory, '*.mdx'))
    
    # Iterate through each .mdx file
    for file_path in mdx_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            mdx_content = file.read()
        
        # Clean the content by removing head matter and images
        clean_content = remove_headmatter_and_images(mdx_content)
        
        # Construct the output file path: replace .mdx extension with .md
        base_name = os.path.basename(file_path)
        output_file_path = os.path.join(output_directory, os.path.splitext(base_name)[0] + '.md')
        
        # Write the cleaned content to the output file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(clean_content)

if __name__ == "__main__":
    """
    Main entry point of the script. Specifies source and output directories,
    then processes all MDX files in the source directory.
    """
    # Specify the source directory containing .mdx files
    source_directory = './data'
    
    # Specify the output directory for cleaned .md files
    output_directory = './cleaned-data'
    
    # Process the blog posts and save them to the output directory
    process_blog_posts(source_directory, output_directory)
    
    # Print a completion message
    print("Processing complete. Files have been saved in", output_directory)
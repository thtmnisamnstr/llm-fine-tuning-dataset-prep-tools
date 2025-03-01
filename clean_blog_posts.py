import os
import glob
import re

def remove_headmatter_and_images(mdx_content):
    # Regular expression to match YAML front matter (headmatter)
    headmatter_pattern = re.compile(r'^---\s*.*?\s*---\s*', re.DOTALL | re.MULTILINE)
    # Remove headmatter
    content_without_headmatter = headmatter_pattern.sub('', mdx_content)

    # Check if the first line is bolded and remove it
    lines = content_without_headmatter.splitlines()
    if lines and lines[0].startswith('**') and lines[0].endswith('**'):
        lines.pop(0)
    
    # Join lines back into a single string
    clean_content = '\n'.join(lines)

    # Regular expression to match image references (Markdown images)
    image_reference_pattern = re.compile(r'!\[.*?\]\(.*?\)')
    # Remove image references
    clean_content = image_reference_pattern.sub('', clean_content)

    # Replace <br> tags with Markdown line breaks
    br_tag_pattern = re.compile(r'<br\s*/?>')
    clean_content = br_tag_pattern.sub('  \n', clean_content)

    # Remove all HTML tags
    html_tag_pattern = re.compile(r'<[^>]+>')
    clean_content = html_tag_pattern.sub('', clean_content)

    # Normalize multiple successive newlines: reduce sequences of 3 or more newlines to exactly two newlines
    normalize_newlines_pattern = re.compile(r'\n{3,}')
    normalized_content = normalize_newlines_pattern.sub('\n\n', clean_content.strip())

    return normalized_content

def process_blog_posts(source_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Get all .mdx files in the source directory
    mdx_files = glob.glob(os.path.join(source_directory, '*.mdx'))
    
    for file_path in mdx_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            mdx_content = file.read()
        
        clean_content = remove_headmatter_and_images(mdx_content)
        
        # Construct the output file path
        base_name = os.path.basename(file_path)
        output_file_path = os.path.join(output_directory, os.path.splitext(base_name)[0] + '.md')
        
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(clean_content)

if __name__ == "__main__":
    # Specify the source directory containing .mdx files
    source_directory = './data'
    
    # Specify the output directory for .md files
    output_directory = './cleaned-data'
    
    process_blog_posts(source_directory, output_directory)
    print("Processing complete. Files have been saved in", output_directory)
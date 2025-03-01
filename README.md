# llm-fine-tuning-prepare-dataset-from-md

## clean_blog_posts.py
Python script that will iterate through all of blog posts (in `mdx` format) in the `data` directory, remove all headmatter, remove all image references, remove all html, remove all extraneous whitespace, and save each (in `md` format) in the `cleaned-data` directory.

Run with `python clean_blog_posts.py`.

## md_to_alpaca.py
Python script that will iterate through all of blog posts (in `md` format) in the `cleaned-data` directory and save them to a single Alpaca-formatted json file named `data.json`. The `instruction` values will be blank. The `input` values will be blank. The `output` values will be the contents of the `md` files.

Run with `python md_to_alpaca.py`.
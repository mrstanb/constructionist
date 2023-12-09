import sys
import markdown
import os
import glob

def main():
    if not os.path.exists('public'):
        os.mkdir('public')

    for f in glob.iglob('content/*.md'):
        with open(f, 'r') as file:
            md_content = file.read()
            html_content = markdown.markdown(md_content)

        html_filename = os.path.basename(f)
        html_file_destination = os.path.join('public', os.path.splitext(html_filename)[0] + '.html')

        with open(html_file_destination, 'w') as file:
            file.write(r'''<!DOCTYPE html>
                <html>
                    <head>
                        <meta charset="utf-8" />
                        <title>My First Construction!</title>
                    </head>
                    <body>
            ''')

            file.write(html_content)
            file.write(r'''
                    </body>
                </html>
            ''')

if __name__ == '__main__':
    main()
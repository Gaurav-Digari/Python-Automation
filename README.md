# File Organizer

## What is this project?

This is a simple Python file organizer that automatically sorts files in a directory into different folders based on their file extensions.
For now it will work only on linux later i will make it for windows also.

For example:
- Images (.jpg, .png, .gif, etc.) -> Images
- Videos (.mp4, .mkv, etc.) -> Videos
- Audio (.mp3, .flac, etc.) -> Audio
- Documents (.txt, .pdf, .docx, etc.) -> Documents
- Other file types -> Others

## What problem does it solve?

When a folder contains many different types of files, it can become difficult to keep everything organized.

This script saves time by automatically creating category folders and moving files into the appropriate folder.

## How I created it

I created this project using Python and the built-in `os` and `sys` modules.

The script:
1. Takes a directory/path from the command line.
2. Checks whether the directory is valid.
3. Creates folders for different file categories.
4. Checks the extensions of the files.
5. Moves each file to the appropriate folder.

## How to run

Run the script from the terminal and provide the directory path:

python organizer.py <directory-path>

Example:

python organizer.py Downloads

## File Categories

Images:
.jpg, .png, .webp, .gif, .svg, .jpeg

Videos:
.mp4, .mkv, .avi, .webm, .wmv

Audio:
.mp3, .m4a, .aac, .ogg, .flac

Documents:
.txt, .docx, .pdf, .odt, .pptx, .ppt, .csv

Everything else:
Others

## Note

This is a learning project created to practice Python file handling, command-line arguments, directories, environment variables, and automation.

from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU-269"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents of the console
print(file_contents)
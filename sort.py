# Function to sort the contents of a file
def sort_file_contents(file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            lines = file.readlines()

        # Sort the lines
        lines.sort()

        # Open the file in write mode to save the sorted lines
        with open(file_name, 'w') as file:
            file.writelines(lines)

        print("File contents sorted successfully.")

    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File name
file_name = 'example.txt'

# Calling the function to sort the file contents
sort_file_contents(file_name)

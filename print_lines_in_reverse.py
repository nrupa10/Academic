# Function to read a file and print each line in reverse order
def print_lines_in_reverse(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip()[::-1])
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File name
file_name = 'example.txt'

# Calling the function
print_lines_in_reverse(file_name)

import random
import sys
import os
import tempfile
import subprocess
import time

def read_names_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            names = [line.strip() for line in file]
        return names
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def create_temp_file():
    temp_file_path = tempfile.mktemp()
    print(f"Creating a temporary file at {temp_file_path}.", end=' ')
    return temp_file_path

def open_temp_file_in_vi(temp_file_path, timer_duration):
    print(f"Opening this file now in {timer_duration} seconds for you in vi editor to enter the names")
    for remaining in range(timer_duration, 0, -1):
        print(f"{remaining} ", end='', flush=True)
        time.sleep(1)
    print()  # Move to the next line after the countdown
    subprocess.run(['vi', temp_file_path])

def shuffle_and_assign(names):
    shuffled_names = random.sample(names, len(names))
    pairs = list(zip(names, shuffled_names))
    return pairs

def display_pairs(pairs):
    for pair in pairs:
        print(f'{pair[0]} -> {pair[1]}')

def main():
    choice = input("Do you want to pass the file path (1) or create a temporary file (2) for the list of names?\nEnter 1 or 2: ")

    if choice == '1':
        temp_file_path = create_temp_file()
        open_temp_file_in_vi(temp_file_path, 10)  # Open the file in vi after 10 seconds
        names = read_names_from_file(temp_file_path)
    elif choice == '2':
        input_file_path = input("Enter the complete path of the file with names: ")
        if not os.path.exists(input_file_path):
            print(f"The path you provided does not exist and hence, creating a temporary file '{input_file_path}' for you.", end=' ')
            time.sleep(10)
            temp_file_path = create_temp_file()
            open_temp_file_in_vi(temp_file_path, 10)  # Open the file in vi after 10 seconds
            names = read_names_from_file(temp_file_path)
        else:
            names = read_names_from_file(input_file_path)
    else:
        print("Invalid choice. Please enter 1 or 2.")
        sys.exit(1)

    pairs = shuffle_and_assign(names)

    print("Secret Santa pairs have been shuffled and assigned:")
    display_pairs(pairs)

if __name__ == "__main__":
    main()


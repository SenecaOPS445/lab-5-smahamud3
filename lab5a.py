#!/usr/bin/env python3
# Author ID: 113561229

def read_file_string(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def read_file_list(file_name):
    with open(file_name, 'r') as file:
        return [line.strip('\n') for line in file]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name).strip())
    print(read_file_list(file_name))
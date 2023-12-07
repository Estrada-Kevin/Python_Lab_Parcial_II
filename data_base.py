import json

#saves a file
#param: path where to save, content to save
def save_file(path,content):
    try:
        with open(path,"a") as file:
            file.write(content + '\n')
        print(f"{path} was created successfully.")
    except OSError:
        print(f"Error: Error in saving file.")

#reads a file
#param: path to read
def read_file(path):
    try:
        with open(path,"r") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: Specified file was not found.")


#capitalize words
#param: text to capitalize
#return: capitalized word
def capitalize_words(text):
        words = text.split(' ')
        capitalized_text = [word.capitalize() for word in words]
        return ' '.join(capitalized_text)

#open a json path
#param: path
#return: json data
def open_json(path):
    with open(path,'r') as file:
        config_data = json.load(file)
    return config_data
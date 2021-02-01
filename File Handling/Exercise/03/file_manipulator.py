import os

def manage_file(file_path, mode, content=None):
    with open(file_path, mode) as file:
        if content:
            file.write(content+'\n')
            return
        file.write('')


def create_file(file_path):
    manage_file(file_path, 'w')

def add_content(file_path, content):
    manage_file(file_path, 'a', content)
    # with open(file_path, 'a') as file:
    #     file.write(content+'\n')

def replace_content_file(file_path, content, replace_with):
    try:
        with open(file_path, 'r+') as file:
            text = ''.join(file.readlines())
            replace_content = text.replace(content, replace_with)
            file.seek(0)
            file.writelines(replace_content) # if i use replace_content.split() concatenate  everything
    except FileNotFoundError:
        return 'An error occured'

def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        return 'An error occurred'

actioner= {
        'Create': create_file,
        'Add': add_content,
        'Replace': replace_content_file,
        'Delete': delete_file
}

def start_engine():
    command_data = input().split('-')
    while not command_data[0] == 'End':
        command, command_arg = command_data[0], command_data[1:]
        actioner[command](*command_arg)
        command_data = input().split('-')



start_engine()
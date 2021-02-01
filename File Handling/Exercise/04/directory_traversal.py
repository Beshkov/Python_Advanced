import os


def extract_files(direct):
    return [el for el in direct if '.' in el]


def get_report_for_file_extension(files):
    report = {}
    for file in files:
        name, extension = file.split('.')
        if extension not in report:
            report[extension] = []
        report[extension].append(name)
    return report


dir_content = os.listdir()

files = extract_files(dir_content)
report = get_report_for_file_extension(files)

result_str = ''

for extension, file_name in sorted(report.items(), key=lambda x: x[0]):
    result_str += f'.{extension}\n'
    for name in file_name:
        result_str += f'- - - {name}.{extension}\n'

path = os.path.join(os.environ['userprofile'], 'Desktop', 'report.txt')

with open(path, 'w') as file:
    file.writelines(result_str)

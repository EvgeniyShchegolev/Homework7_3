import os


PATH_DIR = os.getcwd()
list_all_files = os.listdir(PATH_DIR)
list_files_txt = list(file for file in list_all_files if '.txt' in file)


def count_lines_files(file):
    path_to_file = os.path.join(PATH_DIR, file)
    with open(path_to_file, 'r', encoding='utf-8') as f:
        n_lines = sum(1 for _ in f)
        count_lines[file] = n_lines


def create_result_file(dict_files, file_res):
    count_lines_sorted = dict(sorted(dict_files.items(), key=lambda x: x[1]))
    path_to_file_result = os.path.join(PATH_DIR, file_res)
    with open(path_to_file_result, 'w', encoding='utf-8') as file_result:
        for name_file, n_lines in count_lines_sorted.items():
            path_to_file = os.path.join(PATH_DIR, name_file)
            file_result.write(f'{name_file}\n')
            file_result.write(f'{n_lines}\n')
            with open(path_to_file, 'r', encoding='utf-8') as file:
                for i in range(n_lines):
                    file_result.write(file.readline().strip('\n') + '\n')
    print(f'Файл "{file_res}" создан')


count_lines = {}
for file_txt in list_files_txt:
    count_lines_files(file_txt)

create_result_file(count_lines, 'result_file.txt')

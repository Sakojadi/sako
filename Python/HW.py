import os
def find_files(folder_name, target_word):
    text = f'{target_word}\n'
    for file in os.listdir(folder_name):
        try:
            file_path = os.path.join(folder_name, file)
            file1 = open(file_path)
            lines = file1.readlines()
            for i,line in enumerate(lines):
                if target_word in line:
                    text+=f"{i+1}: {file} -> {line}"
            file1.close()
        except:
            pass
    return text
# print(find_files('E:\\projects\\VS code\\Python', 'def'))

def count_files(folder_name):
    l = len(os.listdir(folder_name))
    return f"in {folder_name} there are {l} files\n"
# print(count_files('E:\\projects'))

def max_lenght_word(file_name):
    wl = 0
    fn = open(file_name)
    for line in fn:
        words = line.split()
        for w in words:
            if len(w)>wl:
                wl = len(w)
                w2 = w
    return f'{w2}: {wl}'
# print(max_lenght_word('text.txt'))
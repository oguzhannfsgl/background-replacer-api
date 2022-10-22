import os

def clear_file(output_path):
    filepaths = [os.path.join(output_path, file_) for file_ in os.listdir(output_path)]
    for filepath in filepaths:
        os.remove(filepath)

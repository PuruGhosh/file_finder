import os
from typing import Dict


def count_keyword_in_file(file_path: str, keyword: str) -> dict[str, int | bool] | dict[str, int | bool]:
    """
    Count occurrences of a keyword in a file.

    :param file_path: Path to the file (absolute or relative).
    :param keyword: The keyword to search for in the file's content.
    :return: The count of occurrences of the keyword.
    :raises FileNotFoundError: If the file does not exist.
    :raises IsADirectoryError: If the provided path is a directory.
    """
    # Validate the file path
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file path '{file_path}' does not exist.")
    if os.path.isdir(file_path):
        raise IsADirectoryError(f"The path '{file_path}' is a directory, not a file.")

    # Count keyword occurrences
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                count += line.count(keyword)
    except Exception as e:
        raise RuntimeError(f"Error reading the file: {e}")

    if count>0:
        return {"is_present": True, "count": count}
    else:
        return {"is_present": False, "count": count}



# Example usage
if __name__ == "__main__":
    file_path = "D:\\Develpment\\Projects\\Python\\file_finder\\data\\directory"
    keyword = "abc"
    try:
        count = count_keyword_in_file(file_path, keyword)
        print(f"The keyword '{keyword}' appears {count} times in the file '{file_path}'.")
    except Exception as e:
        print(f"Error: {e}")

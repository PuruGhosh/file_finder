import argparse
import os


def find_keyword_in_files(path: str, keyword: str) -> dict:
    # Validate the path
    valid_path = False
    INVALID_PATH_RESPONSE = {"error": "Invalid path provided."}
    if os.path.exists(path) and not valid_path:
        valid_path = True

    if os.path.exists(f"./{path}") and not valid_path:
        valid_path = True
        path = f"./{path}"
    if os.path.isdir(path) and not valid_path:
        valid_path = True
    if os.path.isdir(f"./{path}") and not valid_path:
        valid_path = True
        path = f"./{path}"

    if(not valid_path):
        return INVALID_PATH_RESPONSE

    # Initialize result dictionary
    result = {
        "keyword": keyword,
        "is_present": False,
        "file_count": 0,
        "files": []
    }

    # Traverse the directory and search for files containing the keyword
    for root, _, files in os.walk(path):
        for file in files:
            # print(file)
            if keyword in file:
                result["files"].append(file)
                result["is_present"] = True

        # Update file count in the result
    result["file_count"] = len(result["files"])

    return result


# Example usage
if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Find files with a keyword in their name.")
    parser.add_argument("--path", required=True, help="The directory path to search.")
    parser.add_argument("--keyword", required=True, help="The keyword to search in file names.")

    args = parser.parse_args()

    # Call the function with provided arguments
    result = find_keyword_in_files(args.path, args.keyword)

    # Print the result
    print(result)

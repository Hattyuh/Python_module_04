import sys
import typing

def print_content(content: str) -> None:
    print(
        "---\n\n"
        f"{content}\n"
        "---"
    )


def proccess_file(args: list[str]) -> int:
    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return 1
    print("=== Cyber Archives Recovery & Preservation ===")
    file: str = args[1]
    print(f"Accesing file {file}'")
    try:
        fd: typing.IO[str] = open(file, "r")
        content: str = fd.read()
        print_content(content)
        fd.close()
        print(f"File '{file}' closed")
    except (FileNotFoundError, PermissionError) as error:
        print(f"Error opening file '{file}': {error}")
    print("Transform data:")
    content: = content.replace("\n", "#\n")
    if content.endswith("\n") == False:
        content += "#"
    print_content(content)
    file = input("Enter new file name (or empty): ")
    if file == "":
        print("Not saving data.")
        return 0
    print(f"Saving data to '{file}'")
    try:
        fd: typing.IO[str] = open(new_file, "w")
        fd.write(content)
        print_content(content)
        fd.close()
        print(f"File '{file}' closed")
    except (FileNotFoundError, PermissionError) as error:
        print(f"Error opening file '{file}': {error}")
    print(f"Data saved to '{file}'")
    return 0


if __name__ == "__main__":
    print(proccess_file(sys.argv)))

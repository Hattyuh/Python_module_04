import sys
import typing


def print_content(content: str) -> None:
    print(
        "---\n\n"
        f"{content}\n"
        "---"
    )


def get_data(args: list[str]) -> str | None:
    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return None
    print("=== Cyber Archives Recovery & Preservation ===")
    file: str = args[1]
    print(f"Accesing file {file}'")
    try:
        fd: typing.IO[str] = open(file, "r")
        content: str = fd.read()
        print_content(content)
        fd.close()
        print(f"File '{file}' closed")
        return content
    except (FileNotFoundError, PermissionError) as error:
        print(f"Error opening file '{file}': {error}")
        return None


def transform_data(data: str) -> str:
    print("Transform data:")
    if len(data) == 0:
        print_content(data)
        return data
    new_data: str = data.replace("\n", "#\n")
    if new_data.endswith("\n") is False:
        new_data += "#"
    print_content(new_data)
    return new_data


def save_data(data: str) -> None:
    file: str = input("Enter new file name (or empty): ")
    if file == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{file}'")
    try:
        fd: typing.IO[str] = open(file, "w")
        fd.write(data)
        print_content(data)
        fd.close()
        print(f"File '{file}' closed")
        print(f"Data saved to '{file}'")
    except (NotADirectoryError, FileNotFoundError, PermissionError) as error:
        print(f"Error saving file '{file}': {error}")


if __name__ == "__main__":
    data: str | None = get_data(sys.argv)
    if data is not None:
        data = transform_data(data)
        save_data(data)

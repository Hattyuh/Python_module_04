import sys
import typing


def print_content(content: str) -> None:
    print(f"---\n\n{content}\n---")


def get_data(args: list[str]) -> str | None:
    if len(args) != 2:
        print("Usage: ft_archieve_creation.py <file>")
        return None
    print("=== Cyber Archives Recovery & Preservation ===")
    file: str = args[1]
    print(f"Accesing file {file}'")
    try:
        fd: typing.IO[str] = open(file, "r")
        try:
            content: str = fd.read()
            print_content(content)
        finally:
            fd.close()
            print(f"File '{file}' closed")
        return content
    except (OSError) as error:
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
        try:
            fd.write(data)
            print_content(data)
        finally:
            fd.close()
        print(f"Data saved to '{file}'")
        print(f"File '{file}' closed")
    except (OSError) as error:
        print(f"Error saving file '{file}': {error}")


if __name__ == "__main__":
    data: str | None = get_data(sys.argv)
    if data is not None:
        data = transform_data(data)
        save_data(data)

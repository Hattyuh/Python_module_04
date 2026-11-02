import sys
import typing


def read_file(args: list[str]) -> None:
    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    file: str = args[1]
    print(f"Accesing file {file}'")
    try:
        fd: typing.IO[str] = open(file, "r")
        try:
            content: str = fd.read()
            print(f"---\n\n{content}\n---")
        finally:
            fd.close()
            print(f"File '{file}' closed")
    except (OSError) as error:
        print(f"Error opening file '{file}': {error}")


if __name__ == "__main__":
    read_file(sys.argv)

def secure_archive(
        file: str,
        action:  str = "r",
        content: str = ""
) -> tuple[bool, str]:
    if action != "r" and action != "w":
        return (
            False,
            f"Wrong action value {action}: use 'r' to read or 'w' to write"
        )
    try:
        with open(file, action) as fd:
            if action == "r":
                result: str = fd.read()
            else:
                fd.write(content)
                result = f"Content succesfully written to '{file}'"
        return (True, result)
    except (OSError) as error:
        return (False, f"{error}")


if __name__ == "__main__":
    print("=== Cyber Archieves Security ===")
    print("\nUsing 'secure_archieve' to read from nonexistent file:")
    print(secure_archive("nonexistent.txt", "r", ""))
    print("\nUsing 'secure_archieve' to read from inaccessible file:")
    print(secure_archive("inaccessible.txt", "r", ""))
    print("\nUsing 'secure_archieve' to write something to inaccessible file:")
    print(secure_archive("inaccessible.txt", "w", "Yoo"))
    print("\nUsing 'secure_archieve' to read from a regular file:")
    result: tuple[bool, str] = secure_archive("file", "r", "")
    print(result)
    print("\nUsing 'secure_archieve' to write previous content to a new file:")
    print(secure_archive("new_file", "w", result[1]))

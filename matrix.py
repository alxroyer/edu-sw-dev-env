def parse_line(line: str) -> str:
    raise SyntaxError(f"Invalid syntax {line!r}")


def main():
    # REQ-UI-010: Interactive command line interface
    print("Matrix command line. Type 'exit' to quit.")
    while True:
        try:
            # REQ-UI-015: Prompt
            # REQ-UI-020: Left and right arrows
            # REQ-UI-030: HOME and END keys
            # REQ-UI-040: BACKSPACE and DELETE keys
            # REQ-UI-050: ENTER key
            _line: str = input("matrix> ").strip().replace("\t", "")
            if _line.lower() == 'exit':
                break
            # REQ-SYN-000: Empty and blank lines
            if _line:
                _result = parse_line(_line)
                # REQ-UI-060: Result messages
                print(_result)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

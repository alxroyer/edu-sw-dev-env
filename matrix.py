import json
import re
try:
    import yaml
except ImportError:
    print("Warning: Please install PyYAML to read and write from YAML files.")


VAR_NAME_RGX: str = r"[a-zA-Z_][a-zA-Z_0-9]*"


variables = {}


class Matrix:
    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return repr(self.data)

    # REQ-SYN-100: Stdout matrix output
    def __str__(self) -> str:
        return '\n'.join([' '.join(map(lambda x: f"{x:>5}", row)) for row in self.data])

    # REQ-SYN-040: `+` operator
    def __add__(self, other: 'Matrix') -> 'Matrix':
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions for addition.")
        return Matrix([
            [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ])

    # REQ-SYN-050: `-` operator
    def __sub__(self, other: 'Matrix') -> 'Matrix':
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        return Matrix([
            [self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ])

    # REQ-SYN-060: `*` operator
    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if len(self.data[0]) != len(other.data):
            raise ValueError("Number of columns in the first matrix must equal number of rows in the second matrix for multiplication.")
        return Matrix([[
            sum(a * b for a, b in zip(self_row, other_col))
            for other_col in zip(*other.data)
        ] for self_row in self.data])

    @classmethod
    def from_json(cls, json_data: str) -> 'Matrix':
        data = json.loads(json_data)
        return cls(data)

    # REQ-SYN-022: File matrix input
    @classmethod
    def from_file(cls, file_path: str) -> 'Matrix':
        with open(file_path, 'r') as file:
            if file_path.endswith('.json'):
                data = json.load(file)
            elif file_path.endswith(('.yaml', '.yml')):
                data = yaml.safe_load(file)
            else:
                raise ValueError("Unsupported file format.")
        return cls(data)

    # REQ-SYN-110: File matrix output
    def to_file(self, file_path: str):
        with open(file_path, 'w') as file:
            if file_path.endswith('.json'):
                json.dump(self.data, file)
            elif file_path.endswith(('.yaml', '.yml')):
                yaml.safe_dump(self.data, file)
            else:
                raise ValueError("Unsupported file format.")


def parse_line(line: str) -> str:
    _match: re.Match[str]

    # REQ-SYN-010: Variable assignment
    _match = re.match(rf"^({VAR_NAME_RGX}) *= *(.*)$", line)
    if _match:
        _var_name = _match.group(1)
        _expr = _match.group(2)
        variables[_var_name] = parse_matrix_value(_expr)
        return f"Assigned {_var_name} = {variables[_var_name]!r}"

    # REQ-SYN-100: Stdout matrix output
    _match = re.match(r"^print\((.*)\)$", line)
    if _match:
        _expr = _match.group(1)
        _matrix = parse_matrix_value(_expr)
        return str(_matrix)

    # REQ-SYN-110: File matrix output
    _match = re.match(r"^write\( *(.*) *, *\"([^\"]*)\" *\)$", line)
    if _match:
        _expr = _match.group(1)
        _file_path = _match.group(2)
        _matrix = parse_matrix_value(_expr)
        _matrix.to_file(_file_path)
        return f"{_file_path!r} written with {_matrix!r}"

    raise SyntaxError(f"Invalid syntax {line!r}")


# REQ-SYN-020: Matrix value
def parse_matrix_value(expr: str) -> Matrix:
    _match: re.Match[str]
    _tmp_var_name: str

    # REQ-SYN-023: Variable value
    if expr in variables:
        return variables[expr]

    # REQ-SYN-022: File matrix input
    _match = re.match(r"^(.*)read\( *\"([^\"]*)\" *\)(.*)$", expr)
    if _match:
        file_path = _match.group(2)
        _tmp_var_name = f"__tmp{len(variables)}"
        try:
            variables[_tmp_var_name] = Matrix.from_file(file_path)
            return parse_matrix_value(_match.group(1) + _tmp_var_name + _match.group(3))
        finally:
            del variables[_tmp_var_name]

    # REQ-SYN-040: `+` operator
    # REQ-SYN-050: `-` operator
    _match = re.match(r"^(.*)([+-])(.*)$", expr)
    if _match:
        _m1 = parse_matrix_value(_match.group(1).strip())
        _m2 = parse_matrix_value(_match.group(3).strip())
        if _match.group(2) == "+":
            return _m1 + _m2
        else:
            return _m1 - _m2

    # REQ-SYN-060: `*` operator
    _match = re.match(r"^(.*)(\*)(.*)$", expr)
    if _match:
        _m1 = parse_matrix_value(_match.group(1).strip())
        _m2 = parse_matrix_value(_match.group(3).strip())
        return _m1 * _m2

    # REQ-SYN-021: JSON matrix input
    if expr.startswith("[") and expr.endswith("]"):
        try:
            return Matrix.from_json(expr)
        except json.JSONDecodeError:
            raise ValueError(f"Invalid matrix value: {expr!r}")

    raise SyntaxError(f"Invalid syntax {repr!r}")


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

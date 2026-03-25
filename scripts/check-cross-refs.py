#!/usr/bin/env python

import argparse
import logging
import pathlib
import re
import sys
import typing


INPUT_PATH: str = ""
TOC_LINKS: typing.Dict[str, typing.Tuple[int, str]] = {}  # {anchor => (line, title)}
CROSS_REFS: typing.List[typing.Tuple[int, str, str]] = []  # [(line, text, anchor)]


def parse_args() -> None:
    global INPUT_PATH

    _parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Check cross references in a TOC enabled .md file.",
        add_help=False,
    )
    _parser.add_argument("--help", action="help", help="Show this help message and exit.")
    _parser.add_argument("--debug", action="store_true", default=False, help="Activate debugging.")
    _parser.add_argument("input", action="store", help="TOC enabled input .md file.")
    _args: typing.Any = _parser.parse_args(sys.argv[1:])

    logging.basicConfig(level=logging.DEBUG if _args.debug else logging.INFO)
    INPUT_PATH = _args.input
    logging.debug(f"INPUT_PATH={INPUT_PATH!r}")


def read_input_file() -> None:
    _toc_mode: bool = False

    for _index, _line in enumerate(pathlib.Path(INPUT_PATH).read_text().splitlines()):  # type: int, str
        if _line == "<!-- TOC -->":
            _toc_mode = True
            logging.debug(f"{INPUT_PATH}:{_index + 1}: _toc_mode={_toc_mode!r}")
        elif _line == "<!-- /TOC -->":
            _toc_mode = False
            logging.debug(f"{INPUT_PATH}:{_index + 1}: _toc_mode={_toc_mode!r}")
        else:
            _match: typing.Match[str] = re.search(r"\[([^\]]*)\]\((#[^)]*)\)", _line)
            if _match:
                if _toc_mode:
                    TOC_LINKS[_match.group(2)] = (_index + 1, _match.group(1))
                else:
                    CROSS_REFS.append((_index + 1, _match.group(1), _match.group(2)))
                logging.log(
                    logging.DEBUG if _toc_mode else logging.INFO,
                    f"{INPUT_PATH}:{_index + 1}: {'TOC' if _toc_mode else 'Cross'} reference {_match.group(1)!r} -> {_match.group(2)!r}",
                )

def check_cross_refs() -> None:
    for _line, _text, _cross_ref in CROSS_REFS:  # type: int, str, str
        if _cross_ref not in TOC_LINKS:
            logging.error(f"{INPUT_PATH}:{_line}: No such cross reference {_text!r} -> {_cross_ref!r}")
        elif not _cross_ref.startswith(_text.replace("§", "#").replace(".", "")):
            logging.error(f"{INPUT_PATH}:{_line}: {_text!r} does not match with {_cross_ref!r}")


if __name__ == "__main__":
    parse_args()
    read_input_file()
    check_cross_refs()

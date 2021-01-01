"""
    based on: Bryce93 answer in https://stackoverflow.com/questions/38543709/count-lines-of-code-in-directory-using-python

    how to enter data when execute script:

    dir_path -> enter the full directory path that contains the project
    directory path: /home/user/directory/path

    file_extensions -> enter one or more file extensions to count code lines in those files
    directory path: .py, .json
"""

import os
import io


__FILENAME = 'code_lines_result.txt'


def lines_counter(dir_path: str, files_ext: tuple, result_file: io, lines=0, header=True, begin_start=None) -> int:
    """
        print the number of lines per file in console and save the result in .txt file 
        in the script directory
    """

    if header:
        print('{:>10} |{:>10} | {:<20}'.format('ADDED', 'TOTAL', 'FILE'))
        print('{:->11}|{:->11}|{:->20}'.format('', '', ''))
        result_file_write_headers(result_file)

    for _file in os.listdir(dir_path):
        _file = os.path.join(dir_path, _file)
        if os.path.isfile(_file):
            if _file.endswith(files_ext):
                with open(_file, 'r') as f:
                    newlines = f.readlines()
                    newlines = len(newlines)
                    lines += newlines

                    if begin_start is not None:
                        reldir_of_file = '.' + _file.replace(begin_start, '')
                    else:
                        reldir_of_file = '.' + _file.replace(dir_path, '')

                    print('{:>10} |{:>10} | {:<20}'.format(
                        newlines, lines, reldir_of_file))
                    result_file_write_count(
                        result_file, newlines, lines, reldir_of_file)

    # close file result
    result_file.close()

    for _file in os.listdir(dir_path):
        _file = os.path.join(dir_path, _file)
        if os.path.isdir(_file):
            result_file = create_result_file()
            lines: int = lines_counter(
                _file, files_ext, result_file, lines, header=False, begin_start=dir_path)

    return lines


def remove_result_file() -> None:
    """
        check if result file exists and remove it
    """
    if os.path.isfile(__FILENAME):
        os.remove(__FILENAME)


def create_result_file() -> io:
    """
        open file in append mode
    """
    return open(__FILENAME, "a")


def result_file_write_headers(result_file: io) -> None:
    """
        write headers in file_result
    """
    result_file.write('{:>10} |{:>10} | {:<20}\r\n'.format(
        'ADDED', 'TOTAL', 'FILE'))
    result_file.write('{:->11}|{:->11}|{:->20}\r\n'.format('', '', ''))


def result_file_write_count(result_file: io, newlines: int, lines: int, reldir_of_file: str) -> None:
    """
        write file count in file_result
    """
    result_file.write('{:>10} |{:>10} | {:<20}\r\n'.format(
        newlines, lines, reldir_of_file))


if __name__ == "__main__":
    remove_result_file()
    result_file = create_result_file()
    print('please, enter the following ↓')
    dir_path: str = input('directory path: ')
    file_extensions: tuple = tuple(x for x in input(
        'file extensions: ').replace(' ', '').split(','))
    lines_counter(dir_path, file_extensions, result_file)

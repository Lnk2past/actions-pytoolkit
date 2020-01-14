def set_env(name, value):
    print(f'::set-env name={name}::{value}')


def set_output(name, value):
    print(f'::set-output  name={name}::{value}')


def add_path(path):
    print(f'::add-path::{path}')


def debug(message):
    print(f'::debug::{message}')


def warning(message, name=None, line=None, col=None):
    print(f'::warning {_format_file_location(name, line, col)}::{message}')


def error(message, name=None, line=None, col=None):
    print(f'::error {_format_file_location(name, line, col)}::{message}')


def add_mask(value):
    print(f'::add-mask::{value}')


def stop_commands(endtoken):
    print(f'::stop-commands::{endtoken}')


def start_commands(starttoken):
    print(f'::{starttoken}::')


def _format_file_location(name, line, col):
    fl = ''
    if name:
        fl += f'file={name}'
        if line or col:
            fl += ','
    if line:
        fl += f'line={line}'
        if col:
            fl += ','
    if col:
        fl += f'col={col}'
    return fl

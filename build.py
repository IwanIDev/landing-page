#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import shutil
import os

def copy_with_extension(src, dest, extension, ignore_files=[]):
    dest_path = dest.resolve()
    parent = Path(__file__).resolve().parent
    src_path = src.resolve().relative_to(parent)
    for file in src.rglob(f'*.{extension}'):
        if file.name in ignore_files:
            continue
        if file.resolve().parent == dest_path:
            continue
        print(f"Copying {file} to {dest}")
        shutil.copy(file.resolve(), dest_path)

def main():
    # Create a new file
    current_dir = Path.cwd()

    # Create build directory
    build = current_dir / 'build'
    build.mkdir(exist_ok=True)

    print(f"Created build directory {build.resolve()}")

    build_path = build.resolve()

    css = build / 'css'
    css.mkdir(exist_ok=True)
    css_path = css.resolve()

    html_ignore = []
    css_ignore = ['tailwind.css', 'style.css']

    copy_with_extension(current_dir / 'src', build_path, 'html')

    copy_with_extension(current_dir / 'src', css_path, 'css', css_ignore)

if __name__ == "__main__":
    main()
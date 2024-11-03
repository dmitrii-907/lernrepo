#!/usr/bin/env python3
import os

def human_readable_size(size_bytes):
    """
    Конвертирует размер в байтах в удобное для чтения представление.
    """
    if size_bytes == 0:
        return "0 B"
    i = float(size_bytes)
    sizes = ["B", "KB", "MB", "GB", "TB"]
    count = 0
    while i >= 1024 and count < len(sizes) - 1:
        i /= 1024
        count += 1
    return f"{i:.2f} {sizes[count]}"

def get_size(file_path):
    """
    Возвращает размер файла или директории в байтах, игнорируя символьные ссылки.
    """
    total_size = 0
    if not os.path.islink(file_path):
        if os.path.isfile(file_path):
            total_size = os.path.getsize(file_path)
        elif os.path.isdir(file_path):
            for root, dirs, files in os.walk(file_path):
                for f in files:
                    fp = os.path.join(root, f)
                    if not os.path.islink(fp):
                        total_size += os.path.getsize(fp)
    return total_size

def main():
    current_dir = os.getcwd()
    items = []

    for item in os.listdir(current_dir):
        full_path = os.path.join(current_dir, item)
        size = get_size(full_path)
        items.append((item, size))

    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    for name, size in sorted_items:
        readable_size = human_readable_size(size)
        print(f"{readable_size:<10} {name}")

if __name__ == "__main__":
    main()

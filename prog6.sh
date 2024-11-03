#!/bin/bash
clear
# Функция для определения размера файла или директории
get_size() {
    du -sh "$1" | cut -f1
}

# Получение списка файлов и директорий
ls -A1 |
while read -r item; do
    size=$(get_size "$item")
    echo "$size $item"
done | sort -hr | column -t


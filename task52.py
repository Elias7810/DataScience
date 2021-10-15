with open("test2.txt", encoding="UTF-8") as test2:
    content = test2.read().splitlines()
    print(f"Количество строк в файле - {len(content)}")
    for i, line in enumerate(content):
        print(f"Количество слов  в строке № {i + 1} - {len(line.split())}")

def custom_write(file_name, strings):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write("\n")
        file.write(strings)

    with open(file_name, "r", encoding="utf-8") as file:
        index = 0
        while True:
            position = file.tell()
            line = file.readline()

            if not line:
                break

            print(f"строка: {index}: ~начало в байтах {position}")
            index += 1

custom_write("products.txt.txt", "error1")
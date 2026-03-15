with open("basics/file.txt", "r") as f:
    content = f.read()
    words = content.split()
    word_count = len(words)
    print(f"Total words: {word_count}")


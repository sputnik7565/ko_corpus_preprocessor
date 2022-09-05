import os
from tqdm import tqdm


def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def parse_text(path):
    texts = []
    for idx, (current, dirs, files) in enumerate(os.walk(path)):
        if idx == 0:
            continue
        print(current, dirs, files)
        for file in tqdm(files, desc="[Parsing]"):
            text = load_file(os.path.join(current, file))
            texts.append(text)

    return texts


def save_file(path, src):
    with open(path, "w", encoding="utf-8") as f:
        f.write(src)


def main():
    texts = parse_text(".")
    save_file("corpus.txt", "\n".join(texts))


if __name__ == '__main__':
    main()

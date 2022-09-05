import argparse
from tqdm import tqdm
import time
import math


# 총 길이
def count_total_length(input_data):
    with open(input_data, "r", encoding="UTF-8") as f:
        total_length = len(f.readlines())

    return total_length


def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]


def main(args):
    input_file = args.input_path
    output_file = args.output_path
    split_count = int(args.split_count)

    # 총 문장 길이
    total_len = count_total_length(input_file)
    print("분할 대상 문장 총 길이: %s" % total_len)

    # 파일 갯수 조정
    divide_len = math.floor(total_len // split_count)
    if split_count * divide_len < total_len:
        divide_len = total_len // split_count + 1

    with open(input_file, 'r', encoding='UTF-8') as f:
        text = f.readlines()

    list_chunked = list_chunk(text, divide_len)

    f_num = 1
    for idx, line in tqdm(enumerate(list_chunked)):
        output = ''.join(s for s in line)
        if idx == len(list_chunked) - 1:
            pass
        else:
            output = output[:-1]

        file_name = output_file + str(f_num) + ".txt"
        with open(file_name, "w", encoding='UTF-8') as f:
            f.write(output)
            f_num += 1

    print("done")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--input_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, default="split_corpus_")
    parser.add_argument("--split_count", type=str, required=True)

    args = parser.parse_args()

    start = time.time()
    main(args)
    end = time.time()

    print("수행시간: %f 초" % (end - start))
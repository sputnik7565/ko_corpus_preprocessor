import re
import argparse
import json
import os
import time
import math

from html2text import html2text
from kss import split_sentences
from tqdm import tqdm
from attrdict import AttrDict

import ray


# 전처리 를 위한 텍스트 처리
temp_string = ""
def func_join_split(text):
    global temp_string
    text = text.strip()
    temp_string += text + " "
    end_point = ['. ', '" ', "? ", "! ", "' "]  # 문장을 나눌 엔드 포인트 조건
    if temp_string[-2:] in end_point:
        output = temp_string
        temp_string = ""
        return output
    else:
        pass


# 최소 글자 처리
temp = ""
def func_priority(text, args):
    temp_text = text.split('\n')
    output = ""
    global temp

    for string in temp_text:
        #  func_min_words_delete = True 최소 글자 갯수 이하면 삭제
        if args.func_min_words_delete:
            if string.count(' ') >= args.min_words:
                if len(string) != 0:
                    output += string.strip() + "\n"
            else:
                pass
        # func_min_words_delete = False 최소 글자 갯수 이하면 다음 라인을 붙임
        else:
            temp += string + ' '
            if string.count(' ') >= args.min_words:
                if len(temp) != 0:
                    temp = temp.strip()
                    output += temp + "\n"
                    temp = ""

    return output


# 정규식
def normalize_text(text):
    text = re.sub(r"\n{2,}", "\n", text)
    text = re.sub(r"[^·A-Za-z0-9가-힣\x00-\x7F]", "", text)
    text = re.sub(r'[\[\](){}|]', " ", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text


@ray.remote
def process(input_data, args):
    global temp_string
    string = input_data
    # --------------------------------------------------------------------------------- html 제거
    string = html2text(string, bodywidth=0) if args.func_html else " ".join(string.split("\n"))
    # --------------------------------------------------------------------------------- 텍스트 사전 처리
    string = func_join_split(string)

    if string is not None:
        # ----------------------------------------------------------------------------- 문장 분리
        temp_sent = ""
        if args.func_kss:  # kss 기준 문장 분리
            if len(string) > 500:
                list_string = string.split(". ")
                for i in range(len(list_string) - 1):
                    list_string[i] = list_string[i] + "."

                for i in list_string:
                    for sent in split_sentences(i):
                        temp_sent += sent + "\n"
                string = temp_sent
            else:
                for sent in split_sentences(string):
                    temp_sent += sent + "\n"
                string = temp_sent
        else:   # 구두점 기준 문장 분리
            string = ".\n".join(string.split(". "))
        # ----------------------------------------------------------------------------- 최소 길이 처리
        string = func_priority(string, args)
        if len(string) <= 1:
            string = ""
        else:
            string = string + "\n"
        # ----------------------------------------------------------------------------- 정규식 처리
        string = normalize_text(string)
    else:
        string = ""

    return string


# 데이터 로드
def load_data(args):
    path = args.input_path
    with open(path, "r", encoding="utf-8") as f:
        loaded_data = f.readlines()
    return loaded_data


# 데이터 저장
def save_data(processed_data, args):
    path = "preprocessed_" + args.input_path
    with open(path, "a", encoding="utf-8") as f:
        f.write(processed_data)


# 병렬 처리를 위한 데이터 분할
def list_chunk(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def split_data(input_data):
    total_len = len(input_data)
    split_count = 100
    divide_len = math.floor(total_len // split_count)
    if split_count * divide_len < total_len:
        divide_len = total_len // split_count + 1

    list_chunked = list_chunk(input_data, divide_len)
    data_list_out = ["".join(i) for i in list_chunked]

    return data_list_out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_dir", type=str, default="config")
    parser.add_argument("--config_file", type=str, default="config.json")
    args = parser.parse_args()
    with open(os.path.join(args.config_dir, args.config_file)) as f:
        main_args = AttrDict(json.load(f))

    start = int(time.time())
    input_data = load_data(main_args)
    data_list = split_data(input_data)
    print("처리할 데이터 길이 :", len(input_data))

    ray.init()
    for i in tqdm(data_list):
        pi = process.remote(i, main_args)
        save_data(ray.get(pi), main_args)

    print("***run time(sec) :", int(time.time()) - start)

# PLM 사전 학습을 위한 한국어 말뭉치 전처리 툴

사전 학습을 위한 한국어 말뭉치를 전처리 하기 위한 툴입니다.  
병렬처리 라이브러리인 ray를 사용해 전처리 속도를 향상시켰습니다.

말뭉치를 kss를 통해 문장 분리 후 html 태그 제거, 맞춤법 처리, 특수 문자를 정규식으로 처리할 수 있습니다.  
html, 정규식 처리 여부 및 출력 코퍼스 라인 당 최소 단어 갯수 지정, 최소 갯수가 안되었을 때 삭제할 것인지,   
다음 라인을 추가할 것인지 여부는  config.json 에서 변경할 수 있습니다.


### Pre-requisite

- Python 3.6 or higher
- attrdict
- html2text
- Cython
- kss==2.5.1
- tqdm
- ray

### Usage

- 환경 세팅 /setting
``` $ python env_setting.py ```

- 전처리 파라미터 세팅 /config/config.json

- 전처리 실행 ``` $ python main.py ```

- 입력 데이터 포맷: txt, utf-8


### Config.json
```bash
{
  "input_path": "corpus_novel_small.txt",   # 입력 파일 경로
  "func_html": true,                        # html 코드 제거 여부
  "func_kss": true,                         # kss 문장 분리 사용 여부
  "func_min_words_delete": false,           # 최소 글자 이하 True 면 삭제, False 면 최소 글자 충족 까지 다음 라인을 붙임 
  "min_words": 10                           # 라인당 최소 단어 갯수
}
```


----

### Util
대용량 코퍼스 전처리를 위한 텍스트 병합 툴과 텍스트 분할 툴, 환경 세팅 툴로 구성 되어 있습니다.
- setting : 환경 세팅  ```$ python env_setting.py```
- splitter : 텍스트 파일 분할 ```$ python splitter.py --input path {대상 파일 경로} --split_count {분할 갯수}```
- merzing : 텍스트 병합 * 하위 폴더 생성 뒤 병합 하려는 텍스트 파일을 넣어야 합니다.  ```$ python merzing.py```


----
### Author
Name: Kim, Chan  
Email: sputnik7565@gmail.com

----
### Contrubutors
- PowerVoice 박정운 프로
- PowerVoice 홍두기 프로

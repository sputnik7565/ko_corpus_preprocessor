## PLM 사전 학습을 위한 한국어 말뭉치 전처리 툴

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
  "input_path": "data.txt",                 # 입력 파일 경로
  "func_html": true,                        # html 코드 제거 여부
  "func_kss": true,                         # kss 문장 분리 사용 여부
  "func_min_words_delete": false,           # 최소 글자 이하 True 면 삭제, False 면 최소 글자 충족 까지 다음 라인을 붙임 
  "min_words": 4                            # 라인당 최소 단어 갯수
}
```
<br/>


----

### Util
대용량 코퍼스 전처리를 위한 텍스트 병합 툴과 텍스트 분할 툴, 환경 세팅 툴로 구성 되어 있습니다.
- setting : 환경 세팅  ```$ python env_setting.py```
- splitter : 텍스트 파일 분할 ```$ python splitter.py --input path {대상 파일 경로} --split_count {분할 갯수}```
- merzing : 텍스트 병합 * 하위 폴더 생성 뒤 병합 하려는 텍스트 파일을 넣어야 합니다.  ```$ python merzing.py```

<br/>

----
### Output Sample


전처리 전 코퍼스
```
<doc id="5" url="https://ko.wikipedia.org/wiki?curid=5" title="지미 카터">
지미 카터
捍門
제임스 얼 카터 주니어(, 1924년 10월 1일 ~ )는 민주당 출신 미국 39대 대통령 (1977년 ~ 1981년)이다.
생애.
어린 시절.
지미 카터는 (조지아주) 섬터 카운티 플레인스 마을에서 태어났다.
조지아 공과대학교를 {졸업}하였다. 그 후 해군에 들어가 전함·원자력·잠수함의 승무원으로 일하였다. 1953년 미국 해군 대위로 예편하였고 이후 땅콩·면화 등을 가꿔 많은 돈을 벌었다. 그의 별명이 "땅콩 농부" (Peanut Farmer)로 알려졌다.
정계 입문.
1962년 {{조지아주}} 상원 의원 선거에서 낙선하나 그 선거가 부정선거 였음을 입증하게 되어 당선되고, 1966년 조지아 주지사 선거에 낙선하지만, 1970년 조지아 주지사를 역임했다. 대통령이 되기 전 조지아주 상원의원을 두번 연임했으며, 1971년부터 1975년까지 조지아 지사로 근무했다. 조지아 주지사로 지내면서, 미국에 사는 흑인 등용법을 내세웠다.
대통령 재임.


	◇경제지표.
	-미국 6월 fhfa주택가격지수.
	-미국 7월 신규주택매매.
	-미국 8월 소비자기대지수.
	-미국 8월 마킷 제조업 pmi.

[증권].
호텔롯데 상장 걸림돌 '5% 보호예수' 손본다.
증권사 레버리지비율 완화.
신용평가사의 딜레마.
'국내1호' 시장선점 효과…나팔부는 인프라社
```
<br/>

전처리 후 코퍼스
1) html 제거, kss 적용, 라인당 최소 단어 0, 최소 단어 유지
```
지미 카터 제임스 얼 카터 주니어 , 1924년 10월 1일 ~ 는 민주당 출신 미국 39대 대통령 1977년 ~ 1981년 이다.
생애.
어린 시절.
지미 카터는 조지아주 섬터 카운티 플레인스 마을에서 태어났다.
조지아 공과대학교를 졸업 하였다.
그 후 해군에 들어가 전함·원자력·잠수함의 승무원으로 일하였다.
1953년 미국 해군 대위로 예편하였고 이후 땅콩·면화 등을 가꿔 많은 돈을 벌었다.
그의 별명이 "땅콩 농부" Peanut Farmer 로 알려졌다.
정계 입문.
1962년 조지아주 상원 의원 선거에서 낙선하나 그 선거가 부정선거 였음을 입증하게 되어 당선되고, 1966년 조지아 주지사 선거에 낙선하지만, 1970년 조지아 주지사를 역임했다.
대통령이 되기 전 조지아주 상원의원을 두번 연임했으며, 1971년부터 1975년까지 조지아 지사로 근무했다.
조지아 주지사로 지내면서, 미국에 사는 흑인 등용법을 내세웠다.
대통령 재임.
경제지표.
-미국 6월 fhfa주택가격지수.
-미국 7월 신규주택매매.
-미국 8월 소비자기대지수.
-미국 8월 마킷 제조업 pmi.
 증권 .
호텔롯데 상장 걸림돌 '5% 보호예수' 손본다.
증권사 레버리지비율 완화.
신용평가사의 딜레마.
```
<br/>

2) html 제거, kss 미적용, 라인당 최소 단어 3, 최소 단어 삭제
```
지미 카터 제임스 얼 카터 주니어 , 1924년 10월 1일 ~ 는 민주당 출신 미국 39대 대통령 1977년 ~ 1981년 이다.
지미 카터는 조지아주 섬터 카운티 플레인스 마을에서 태어났다.
그 후 해군에 들어가 전함·원자력·잠수함의 승무원으로 일하였다.
1953년 미국 해군 대위로 예편하였고 이후 땅콩·면화 등을 가꿔 많은 돈을 벌었다.
그의 별명이 "땅콩 농부" Peanut Farmer 로 알려졌다.
1962년 조지아주 상원 의원 선거에서 낙선하나 그 선거가 부정선거 였음을 입증하게 되어 당선되고, 1966년 조지아 주지사 선거에 낙선하지만, 1970년 조지아 주지사를 역임했다.
대통령이 되기 전 조지아주 상원의원을 두번 연임했으며, 1971년부터 1975년까지 조지아 지사로 근무했다.
조지아 주지사로 지내면서, 미국에 사는 흑인 등용법을 내세웠다.
-미국 8월 마킷 제조업 pmi.
호텔롯데 상장 걸림돌 '5% 보호예수' 손본다.
```
<br/>

3) html 제거, kss 미적용, 라인당 최소 단어 3, 최소 단어 유지
```
지미 카터 제임스 얼 카터 주니어 , 1924년 10월 1일 ~ 는 민주당 출신 미국 39대 대통령 1977년 ~ 1981년 이다.
생애. 어린 시절. 지미 카터는 조지아주 섬터 카운티 플레인스 마을에서 태어났다.
조지아 공과대학교를 졸업 하였다. 그 후 해군에 들어가 전함·원자력·잠수함의 승무원으로 일하였다.
1953년 미국 해군 대위로 예편하였고 이후 땅콩·면화 등을 가꿔 많은 돈을 벌었다.
그의 별명이 "땅콩 농부" Peanut Farmer 로 알려졌다.
정계 입문. 1962년 조지아주 상원 의원 선거에서 낙선하나 그 선거가 부정선거 였음을 입증하게 되어 당선되고, 1966년 조지아 주지사 선거에 낙선하지만, 1970년 조지아 주지사를 역임했다.
대통령이 되기 전 조지아주 상원의원을 두번 연임했으며, 1971년부터 1975년까지 조지아 지사로 근무했다.
조지아 주지사로 지내면서, 미국에 사는 흑인 등용법을 내세웠다.
대통령 재임. 경제지표. -미국 6월 fhfa주택가격지수. -미국 7월 신규주택매매. -미국 8월 소비자기대지수. -미국 8월 마킷 제조업 pmi.
 증권 . 호텔롯데 상장 걸림돌 '5% 보호예수' 손본다.

```
<br/>

4) kss 적용 처리 시간 테스트

|  코퍼스 용량  | kss 적용 여부 |   처리 시간   |
|:--------:|:---------:|:---------:|
|  516mb   |    적용     | 2h 17min  |
|  516mb   |    미적용    |   5min    |
<br/>

----
### Author
Name: Kim, Chan  
Email: sputnik7565@gmail.com
<br/>

----
### Contrubutors
- PowerVoice 박정운 프로
- PowerVoice 홍두기 프로


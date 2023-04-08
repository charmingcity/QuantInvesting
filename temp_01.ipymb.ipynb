import requests as rq 
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_deposit.nhn'  #페이지 주소를 입력한다 
data = rq.get(url)       #get 함수를 통해 해당 페이지 내용을 받아 온다. 
data_html = BeautifulSoup(data.content)
parse_day = data_html.select_one(
    'div.subtop_sise_graph2 > ul.subtop_chart_note > li > span.tah').text

print(parse_day)

import re 

biz_day = re.findall('[0-9]+', parse_day) #findall() 메서드 내에 정규 표현식을 이용해 숫자에 해당하는 부분만을 추출한다. '[0-9]'+는 모든 숫자를 의미하는 정규 표현식  
biz_day = ''.join(biz_day)  #join() 함수를 통해 숫자를 합쳐 준다. 

print(biz_day)

import requests as rq 
from io import BytesIO
import pandas as pd 

gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd' #원하는 항목을 제출할 URL을 입력한다. 
gen_otp_stk = { 
    'locale': 'ko_KR',
    'mktId': 'STK',
    'trdDd': '20230331',
    'money': '1',
    'csvxls_isNo': 'false',
    'name': 'fileDown',
    'url': 'dbms/MDC/STAT/standard/MDCSTAT03901'
}
headers = {'Referer': 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201'}
otp_stk = rq.post(gen_otp_url, gen_otp_stk, headers=headers).text

print(otp_stk)

down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'  #otp를 제출할 url을 down_url에 입력한다.
down_sector_stk = rq.post(down_url, {'code' : otp_stk}, headers=headers) #post() 함수를 통해 위에서 부여받은 OTP 코드를 해당 URL에 제출한다. 
sector_stk = pd.read_csv(BytesIO(down_sector_stk.content), encoding='EUC-KR') # 받은 데이터의 content 부분을 BytesIO()F를 이용해 바이너리 스트림 형태로 만든 후, read_csv() 함수를 통해 데이터를 읽어 온다. 해당 데이터는 EUC-KR 형태로 인코딩 되어 있음 

sector_stk.head()

gen_otp_ksq = {
    'mktId': 'KSQ',
    'trdDd': '20230331',
    'money': '1',
    'csvxls_isNo': 'false',
    'name': 'fileDown',
    'url': 'dbms/MDC/STAT/standard/MDCSTAT03901'
}
otp_ksq = rq.post(gen_otp_url, gen_otp_ksq, headers=headers).text

down_sector_ksq = rq.post(down_url, {'code': otp_ksq}, headers=headers)
sector_ksq = pd.read_csv(BytesIO(down_sector_ksq.content), encoding='EUC-KR')

sector_ksq.head()

krx_sector = pd.concat([sector_stk, sector_ksq]).reset_index(drop=True) #concat() 함수를 통해 두 데이터를 합쳐 주며, reset_index() 메서드를 통해 인덱스를 리셋시킨다. 
krx_sector['종목명'] = krx_sector['종목명'].str.strip() #종목명에 공백이 있는 경우가 있으므로 strip() 메서드를 이용해 이를 제거해 준다.
krx_sector['기준일'] = biz_day #데이터의 기준일에 해당하는 [기준일] 열을 추가한다. 


## 개별종목 지표 크롤링 

import requests as rq
from io import BytesIO
import pandas as pd

gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
gen_otp_data = {
    'searchType': '1',
    'mktId': 'ALL',
    'trdDd': biz_day,
    'csvxls_isNo': 'false',
    'name': 'fileDown',
    'url': 'dbms/MDC/STAT/standard/MDCSTAT03501'
}
headers = {'Referer': 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader'}
otp = rq.post(gen_otp_url, gen_otp_data, headers=headers).text

down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
krx_ind = rq.post(down_url, {'code': otp}, headers=headers)

krx_ind = pd.read_csv(BytesIO(krx_ind.content), encoding='EUC-KR')
krx_ind['종목명'] = krx_ind['종목명'].str.strip()
krx_ind['기준일'] = biz_day

krx_ind.head()


# 데이터 정리하기 
diff = list(set(krx_sector['종목명']).symmetric_difference(set(krx_ind['종목명']))) #symmetric_difference 메서드를 통해 하나의 데이터만 있는 종목 확인 
print(diff)


kor_ticker = pd.merge(krx_sector,                          #merge() 함수는 on 조건을 기준으로 두 데이터를 하나로 합친다 
                      krx_ind,
                      on=krx_sector.columns.intersection(   #intersection() 메서드를 이용해 공통으로 존재하는 [종목코드, 종목명, 종가, 대비, 등락률] 열을 기준으로 입력 
                          krx_ind.columns).tolist(),
                      how='outer')

kor_ticker.head()


print(kor_ticker[kor_ticker['종목명'].str.contains('스팩|제[0-9]+호')]['종목명'].values)
print(kor_ticker[kor_ticker['종목코드'].str[-1:] != '0']['종목명'].values) #국내 종목 중 종목코드 끝이 0이 아닌 종목은 우선주에 해당한다.

import numpy as np 

kor_ticker['종목구분'] = np.where(kor_ticker['종목명'].str.contains('스팩|제[0-9]호'), '스팩',
                              np.where(kor_ticker['종목코드'].str[-1:] != '0', '우선주',
                                       np.where(kor_ticker['종목명'].str.endswitch('리츠'), '리츠',
                                                np.where(kor_ticker['종목명'].isin(diff), '기타',
                                                         '보통주'))))

kor_ticker = kor_ticker.reset_index(drop=True)
kor_ticker.columns = kor_ticker.columns.str.replace('', '')
kor_ticker = kor_ticker[['종목코드', '종목명', '시장구분', '종가',
                         '시가총액', '기준일', 'EPS', '선행EPS', 'BPS', '주당배당금', '종목구분']]
kor_ticker = kor_ticker.replace({np.nan: None})
kor_ticker['기준일'] = pd.to_datetime(kor_ticker['기준일'])

kor_ticker.head()


import numpy as np

kor_ticker['종목구분'] = np.where(kor_ticker['종목명'].str.contains('스팩|제[0-9]+호'), '스팩',
                              np.where(kor_ticker['종목코드'].str[-1:] != '0', '우선주',
                                       np.where(kor_ticker['종목명'].str.endswith('리츠'), '리츠',
                                                np.where(kor_ticker['종목명'].isin(diff),  '기타',
                                                '보통주'))))
kor_ticker = kor_ticker.reset_index(drop=True)
kor_ticker.columns = kor_ticker.columns.str.replace(' ', '')
kor_ticker = kor_ticker[['종목코드', '종목명', '시장구분', '종가',
                         '시가총액', '기준일', 'EPS', '선행EPS', 'BPS', '주당배당금', '종목구분']]
kor_ticker = kor_ticker.replace({np.nan: None})
kor_ticker['기준일'] = pd.to_datetime(kor_ticker['기준일'])

kor_ticker.head()


import pymysql

con = pymysql.connect(user='root',
                      passwd='1234',
                      host='127.0.0.1',
                      db='stock_db',
                      charset='utf8')

mycursor = con.cursor()
query = f"""
    insert into kor_ticker (종목코드,종목명,시장구분,종가,시가총액,기준일,EPS,선행EPS,BPS,주당배당금,종목구분)
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) as new
    on duplicate key update
    종목명=new.종목명,시장구분=new.시장구분,종가=new.종가,시가총액=new.시가총액,EPS=new.EPS,선행EPS=new.선행EPS,
    BPS=new.BPS,주당배당금=new.주당배당금,종목구분 = new.종목구분;
"""

args = kor_ticker.values.tolist()

mycursor.executemany(query, args)
con.commit()

con.close()

#WICS 기준 섹터 정보 크롤링 

import json 
import requests as rq 
import pandas as pd 

url = f'''https://www.wiseindex.com/Index/GetIndexComponets?ceil_yn=0&dt=20230331&sec_cd=G4050'''  #f-string 포매팅
data = rq.get(url).json() #get() 함수를 통해 페이지의 내용을 받아 오며, json() 메서드를 통해 JSON 데이터만 불러올 수 있다.
# 파이썬에서는 JSON 데이터가 딕셔너리 형태로 변경된다. 
type(data)


print(data.keys())
data['list'][0]

data['sector']

data_pd = pd.json_normalize(data['list'])

data_pd.head()


import time
import json
import requests as rq 
import pandas as pd 
from tqdm import tqdm 

sector_code = [
    'G25', 'G35', 'G50', 'G40', 'G10', 'G20', 'G55', 'G30', 'G15', 'G45'
]


data_sector = [] #섹터 정보가 들어갈 빈 리스트(data_sector)를 만든다 

for i in tqdm(sector_code):
    url = f'''http:

import pandas as pd

#함수 모듈 만들 때 외부 변수를 쓰지 않도록 짠다. (전역 변수X)

"""
    날짜 컬럼을 datetime으로 변환하고
    연도, 월 컬럼을 추가
"""

def add_year_month(
    df,
    date_col="일시",
    drop_cols=None,
    date_format="%Y-%m"
):
    df = df.copy()

    #df.DataFrame 타입으로 입력 받는다.
    #"일시" 컬럼은 문자열로 받는다.
    # list이거나 None: 아무 컬럼도 지우지 않는다.
    #날짜 문자열 포맷 지정 "%Y-%m" 한 건 인자만 교체하기 편하도록.
    #반환값은 DataFrame으로 나온다. 표현
    #필수 인자는 1개 : table_df 그 외는 옵션. 

    df[date_col] = pd.to_datetime(
        df[date_col],
        format=date_format
    ) #datetime 변환 함수

    df["연도"] = df[date_col].dt.year
    df["월"] = df[date_col].dt.month

    if drop_cols:
        df = df.drop(columns=drop_cols, errors="ignore")
        #drop_cols가 있으면 실행, errors="ignore"는 없어도 에러 안 뜨게 하고자 함.

    return df


"""
    시트명 = 구역 구조의 엑셀 데이터를
    하나의 DataFrame으로 통합
"""

def merge_region_sheets(sheets: dict):
    dfs = [] #빈 데이터 생성, 활용할 D.F 쓰기 위해

    for region, df in sheets.items():
        temp = df.copy() 
        temp["구역"] = region
        dfs.append(temp)
        
    table_df = pd.concat(dfs, ignore_index=True)
    #pd.concat : 여러개의 df를 하나로 합치는 함수
    return table_df


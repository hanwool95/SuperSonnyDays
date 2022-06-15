import streamlit as st
import pandas as pd
import numpy as np
import emoji
import plotly.express as px
import plotly.graph_objects as go

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sb
from PIL import Image
from konlpy.tag import Komoran
from collections import Counter
import altair as alt

# Webpage Title
st.image("son_golden_boot.jpeg")
st.markdown("<h1 style='text-align: center; color: black;'><big>☀️ SONNY DAYS ☀️</big></h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>⚽ Super Son Data Visualization ⚽</h2>",
            unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'><b>손흥민 아시아 최초 EPL 득점왕 등극! 월드클래스 인정?</b></h3>",
            unsafe_allow_html=True)

st.write(
    "손흥민(30, 토트넘)이 2021/2022시즌 잉글랜드 프리미어리그 (EPL) 득점왕으로 우뚝 섰다. 손흥민은 총 23 골을 넣으며 올 시즌 리그 전체를 통틀어 가장 많은 골을 기록했다. 이로써 리버풀의 모하메드 살라와 함께 공동 득점왕 타이틀을 거머쥐었다. 세계에서 가장 경쟁이 치열하고 수준이 높은 프로축구 리그로 평가되는 EPL에서 아시아인이 득점왕에 오른 것은 사상 처음이다. 잉글랜드를 비롯해 스페인, 독일, 프랑스, 이탈리아 등 유럽 축구 5대 빅리그로 범위를 넓혀도 아시아인 득점왕은 손흥민이 최초다. 한국 축구를 넘어 아시아 축구 역사를 새로 쓴 손흥민의 득점왕 수상을 기념해 드라마 같았던 득점왕 경쟁과 2021~2022시즌 손흥민의 눈 부신 활약을 경기와 언론보도 데이터를 기반으로 살펴본다.")

clicked = st.button("🎉 손흥민의 득점왕 축하하기 🎉")

if clicked:
    st.balloons()
    col_0_1, col_0_2, col_0_3 = st.columns(3)
    with col_0_1:
        st.markdown("![Alt Text](https://media.giphy.com/media/UTKiNBL26wBRsK683S/giphy.gif)")
    with col_0_2:
        st.markdown("![Alt Text](https://media.giphy.com/media/WUTf2RVVtTD7n3W9Sj/giphy.gif)")
    with col_0_3:
        st.markdown("![Alt Text](https://media.giphy.com/media/FrDYUUPYbqBDfqz7mf/giphy.gif)")

st.header("1. 손흥민과 5인의 토트넘 포워드")
df_1 = pd.read_csv("1.csv")
rd_1_son = go.Scatterpolar(r=df_1['손흥민'], theta=df_1['metrics'], fill='toself', name='손흥민')
rd_1_kane = go.Scatterpolar(r=df_1['해리 케인'], theta=df_1['metrics'], fill='toself', name='해리 케인')
rd_1_kulu = go.Scatterpolar(r=df_1['데얀 쿨루세브스키'], theta=df_1['metrics'], fill='toself', name='데얀 쿨루세브스키')
rd_1_bergwijn = go.Scatterpolar(r=df_1['스티븐 베르흐베인'], theta=df_1['metrics'], fill='toself', name='스티븐 베르흐베인')
rd_1_moura = go.Scatterpolar(r=df_1['루카스 모우라'], theta=df_1['metrics'], fill='toself', name='루카스 모우라')

rd_data_1 = [rd_1_son, rd_1_kane, rd_1_kulu, rd_1_bergwijn, rd_1_moura]
rd_fig_1 = go.Figure(data=rd_data_1)
st.plotly_chart(rd_fig_1, user_container_width=True)

st.write(
    "손흥민이 소속된 토트넘 홋스퍼에는 다섯 명의 대표 포워드 선수들이 있다. 손흥민, 해리 케인(29), 데얀 클루셉스키(23), 루카스 모우라(30)와 스티븐 베르바인(23)이다. 각 선수들의 2021~2022 시즌 리그 공격 포인트와 주요 경기 스탯을 6개 지표로 분석했다.")

st.write("✅ **Highlights**")
st.write(
    "💙 다섯 선수 중 손흥민이 전체 골 수, 필드 골 수 (패널티 킥이 아닌 경기 중 넣은 골), 슛 정확도, 경기당 패스 수가 가장 높았다. 패널티 킥 없이 순수 필드골로만 한 시즌에 23골을 넣었기 때문에 득점왕 기록이 더욱 높이 평가된다.")
st.write("💙 슛 정확도는 57%로 손흥민이 팀 내에서 압도적으로 높다. 이번 시즌 득점 시도의 약 57%가 골문으로 향했다는 것을 의미한다.")
st.write(
    "💙 결정적 기회 창출은 해리 케인이 가장 높았는데 손흥민과 EPL 최다 골 합작 듀오로 활약하고 있다는 점에서 해리 케인이 기회를 만들면 손흥민이 골을 넣는 두 선수의 파트너십을 확인할 수 있다. ")

st.markdown("""---""")

st.header("2. '우리흥' vs. '옆집살라' : 득점왕을 향한 레이스")
# df_2_1 = pd.read_csv("2-1.csv", index_col=0, parse_dates=True)
# st.line_chart(df_2_1[["손흥민 누적 골", "살라 누적 골", "누적 골 차이"]], use_container_width=True)
# st.markdown("""---""")

################################################################################################
# def get_data():
#     source = df_2_1
#     source = source[source.date.gt("2004-01-01")]
#     return source

# source = get_data()

source_alt = pd.read_csv("2_alt.csv", header=0, names=['date', 'player', '누적 골'])
source_alt.date = pd.to_datetime(source_alt.date)


def get_chart(data):
    hover = alt.selection_single(
        fields=["date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="손흥민 vs. 살라 누적 골")
            .mark_line()
            .encode(
            x="date",
            y="누적 골",
            color="player",
        )
    )

    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)

    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
            .mark_rule()
            .encode(
            x="yearmonthdate(date)",
            y="누적 골",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("date", title="Date"),
                alt.Tooltip("누적 골", title="누적 골"),
            ],
        )
            .add_selection(hover)
    )
    return (lines + points + tooltips).interactive()


chart = get_chart(source_alt)

ANNOTATIONS = [
    ("2021-09-11", "종아리 부상으로 결장"),
    ("2021-09-19", "A매치 부상 이후 복귀 경기"),
    ("2021-10-30", "누누 산투 감독 마지막 경기, 이후 경질"),
    ("2021-11-07", "안토니오 콘테 감독 리그 데뷔전"),
    # ("2021-12-02", "스파이더맨 세레머니, 이후 톰 홀란드와 만나면서 화제"),
    # ("2021-12-19", "토트넘 소속으로 300번째 경기"),
    ("2022-01-10", "살라 네이션스컵 차출"),
    ("2022-01-19", "손흥민 햄스트링 부상으로 결장"),
    ("2022-02-09", "햄스트링 부상 이후 복귀 경기, 살라 네이션스컵 복귀"),
    # ("2022-02-19", "프리미어리그 Team of the Week 선정"),
    ("2022-02-26", "해리케인과 함께 EPL 역사상 최다 합작골 신기록 달성 (37골)"),
    # ("2022-03-20", "개인 커리어 공식 경기 200번째 득점, 손케듀오 합작골 39개"),
    # ("2022-04-09", "해트트릭"),
    # ("2022-05-01", "개인 커리어 리그 한 시즌 최다골 달성"),
    # ("2022-05-07", "리그 20호골, 득점왕 선두인 살라와 2골 차이"),
    # ("2022-05-12", "득점왕 선두인 살라와 1골 차이"),
    ("2022-05-22", "시즌 마지막 경기에서 22-23호골로 21/22 시즌 득점왕 수상")
]

annotations_df = pd.DataFrame(ANNOTATIONS, columns=["date", "event"])
annotations_df.date = pd.to_datetime(annotations_df.date)
annotations_df["y"] = 10

annotation_layer = (
    alt.Chart(annotations_df)
        .mark_text(size=17, text="⬇", dx=-8, dy=-10, align="left")
        .encode(
        x="date:T",
        y=alt.Y("y:Q"),
        tooltip=["event"],
    )
        .interactive()
)

st.altair_chart(
    (chart + annotation_layer).interactive(),
    use_container_width=True
)

################################################################################################

df_2_2 = pd.read_csv("2-2.csv", index_col=0, parse_dates=True)
st.line_chart(df_2_2[["손흥민 파워랭킹 순위", "살라 파워랭킹 순위"]], use_container_width=True)
st.write("⚠️ **파워랭킹 순위: EPL 선수 375명 중 n등** ⚠️")
st.markdown("""---""")
st.line_chart(df_2_2[["손흥민 파워랭킹 점수", "살라 파워랭킹 점수"]], use_container_width=True)

st.write("✅ **Highlights**")
st.write("💙 1 여기서 이거 중요함요 ")
st.write("💙 2 여기서 이거 중요함요 ")
st.write("💙 3 여기서 이거 중요함요 ")

st.markdown("""---""")

st.header("3. 최상위 Big 6 vs. 그 외 14팀")
st.subheader("이번 시즌 손흥민과 토트넘의 활약 비교")
st.write("**Big 6: 토트넘을 포함하여 EPL 최상위 여섯 팀을 지칭한다.**")

col_3_1, col_3_2 = st.columns(2)

with col_3_1:
    st.subheader("손흥민 활약(골+어시스트)")
    bar_3_1 = pd.DataFrame({
        '손흥민 활약 평균': [0.889, 0.846],
        '상대팀': ['Big 6', '그 외 14팀']
    })

    bar_chart_3_1 = alt.Chart(bar_3_1).mark_bar().encode(
        y='손흥민 활약 평균:Q',
        x='상대팀:O',
    )

    st.altair_chart(bar_chart_3_1, use_container_width=True)

with col_3_2:
    st.subheader("토트넘 활약(득점)")
    bar_3_2 = pd.DataFrame({
        '토트넘 활약 평균': [1.3, 2],
        '상대팀': ['Big 6', '그 외 14팀']
    })

    bar_chart_3_2 = alt.Chart(bar_3_2).mark_bar().encode(
        y='토트넘 활약 평균:Q',
        x='상대팀:O',
    )

    st.altair_chart(bar_chart_3_2, use_container_width=True)

# df_3_1 = pd.read_csv("3-1.csv")

# rd_3_1_tot = go.Scatterpolar(r=df_3_1['tot_indiv_goal_assist'], theta=df_3_1['team_name'], fill='toself', name='토트넘 개인별')
# rd_3_1_son = go.Scatterpolar(r=df_3_1['son_goal_assist'], theta=df_3_1['team_name'], fill='toself', name='손흥민 활약')
# rd_data_3_1 = [rd_3_1_tot, rd_3_1_son]
# rd_fig = go.Figure(data = rd_data_3_1)
# st.plotly_chart(rd_fig, user_container_width=True)
st.markdown("""---""")

df_3_2 = pd.read_csv("3-2.csv")
rd_3_2_tot = go.Scatterpolar(r=df_3_2['tot_indiv_goal_assist'], theta=df_3_2['team_name'], fill='toself',
                             name='토트넘 개인별')
rd_3_2_son = go.Scatterpolar(r=df_3_2['son_goal_assist'], theta=df_3_2['team_name'], fill='toself', name='손흥민 활약')
rd_data_3_2 = [rd_3_2_tot, rd_3_2_son]
rd_fig = go.Figure(data=rd_data_3_2)
st.plotly_chart(rd_fig, user_container_width=True)
st.write("✅ **Highlights**")
st.write("💙 1 여기서 이거 중요함요 ")
st.write("💙 2 여기서 이거 중요함요 ")
st.write("💙 3 여기서 이거 중요함요 ")
st.markdown("""---""")

st.header("4. 손흥민 활약에 따른 언론보도: 기사빈도수")
df_4 = pd.read_csv("4.csv", index_col=0, parse_dates=True)
st.bar_chart(df_4[["기사 빈도수"]], use_container_width=True)
st.bar_chart(df_4[["손흥민 골", "손흥민 어시스트"]], use_container_width=True)

st.write("✅ **Highlights**")
st.write("💙 1 여기서 이거 중요함요 ")
st.write("💙 2 여기서 이거 중요함요 ")
st.write("💙 3 여기서 이거 중요함요 ")
st.markdown("""---""")

st.header("5. 2122시즌 토트넘 38전 22승 5무 11패 (승률 58%)")
col_5_1, col_5_2, col_5_3 = st.columns(3)

stopwords = ['경기', '손흥민', '토트넘', '전반', '후반', '골', '런던', '영국',
             '공격수', '수비수', '골키퍼', '시즌', '출전', '선수', '팀', '라운드',
             '축구', '리그', '한국', '전']

with col_5_1:
    st.subheader("승리 시 기사 본문")
    img = Image.open("win.png")
    st.image(img, width=225)

with col_5_2:
    st.subheader("무승부 시 기사 본문")
    img = Image.open("tie.png")
    st.image(img, width=208)

with col_5_3:
    st.subheader("패배 시 기사 본문")
    img = Image.open("loose.png")
    st.image(img, width=202)

st.write("✅ **Highlights**")
st.write("💙 1 여기서 이거 중요함요 ")
st.write("💙 2 여기서 이거 중요함요 ")
st.write("💙 3 여기서 이거 중요함요 ")

st.markdown("""---""")

st.header("6. 경기에 따른 기사 본문")
df_6 = pd.read_csv("6.csv")

option = st.selectbox('경기를 선택해주세요!', df_6['Matches'])

tagger = Komoran()

if option is not None:
    df_6_index = df_6.index[df_6['Matches'] == option]
    sentences = df_6["기사 본문"][df_6_index]

mask_arr = np.array(Image.open("son.png"))

nouns = []
for sent in sentences:
    tagged_sent = tagger.pos(sent.strip())
    for word, tag in tagged_sent:
        if (tag in ['NNP', 'NNG']) and (word not in stopwords):
            nouns.append(word)

counts = Counter(nouns)
tags = counts.most_common(50)

cloud = WordCloud(width=900, height=1200,
                  font_path='NotoSansKR-Black.otf',  # 이거 없으면 글자 다 깨짐
                  background_color='white',
                  mask=mask_arr,
                  colormap='bwr',
                  prefer_horizontal=True)

cloud = cloud.generate_from_frequencies(dict(tags))
fig = plt.figure(figsize=(15, 20))
plt.axis('off')
plt.imshow(cloud, interpolation='bilinear')
plt.show()
st.pyplot(fig)
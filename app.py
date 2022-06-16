import streamlit as st
import pandas as pd
import numpy as np

import plotly.graph_objects as go

from PIL import Image
import altair as alt

# Webpage Title
st.image("son_golden_boot.jpeg")
st.markdown("<h1 style='text-align: center; color: black;'><big>☀️ SONNY DAYS ☀️</big></h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>⚽ Super Son Data Visualization ⚽</h2>",
            unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'><b>손흥민 아시아 최초 EPL 득점왕 등극! 월드클래스 인정?</b></h3>",
            unsafe_allow_html=True)
st.markdown("<h5><br></br></h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: black;'><b>2022 소셜 네트워크 데이터마이닝과 분석 (이준환 교수님)</b></h5>",
            unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: black;'><b>서울대학교 언론정보학과 허세영 정규하 박진원 김한울</b></h5>",
            unsafe_allow_html=True)
st.markdown("""---""")
# st.markdown("<h5><br></br></h5>", unsafe_allow_html=True)
st.write(
    "**손흥민(30, 토트넘)이 2021/2022시즌 잉글랜드 프리미어리그 (EPL) 득점왕으로 우뚝 섰다.** 손흥민은 총 23 골을 넣으며 올 시즌 리그 전체를 통틀어 가장 많은 골을 기록했다. 이로써 리버풀의 모하메드 살라와 함께 공동 득점왕 타이틀을 거머쥐었다. 세계에서 가장 경쟁이 치열하고 수준이 높은 프로축구 리그로 평가되는 EPL에서 아시아인이 득점왕에 오른 것은 사상 처음이다. 잉글랜드를 비롯해 스페인, 독일, 프랑스, 이탈리아 등 유럽 축구 5대 빅리그로 범위를 넓혀도 아시아인 득점왕은 손흥민이 최초다. 한국 축구를 넘어 아시아 축구 역사를 새로 쓴 손흥민의 득점왕 수상을 기념해 드라마 같았던 득점왕 경쟁과 2021/2022시즌 손흥민의 눈부신 활약을 경기와 언론보도 데이터를 기반으로 살펴본다.")

clicked = st.button("🎉 손흥민의 득점왕 축하하기 🎉")

if clicked:
    st.balloons()
    st.markdown("![Alt Text](https://media.giphy.com/media/WUTf2RVVtTD7n3W9Sj/giphy.gif)")

st.markdown("""---""")

st.header("1. 손흥민과 5인의 토트넘 포워드")
st.write(
    "**손흥민이 소속된 토트넘 홋스퍼에는 다섯 명의 대표 포워드 선수들이 있다.** 손흥민, 해리 케인(29), 데얀 클루셉스키(23), 루카스 모우라(30)와 스티븐 베르바인(23)이다. 각 선수들의 2021/2022 시즌 리그 공격 포인트와 주요 경기 스탯을 6개 지표로 분석했다.")
df_1 = pd.read_csv("1.csv")
rd_1_son = go.Scatterpolar(r=df_1['손흥민'], theta=df_1['metrics'], fill='toself', name='손흥민')
rd_1_kane = go.Scatterpolar(r=df_1['해리 케인'], theta=df_1['metrics'], fill='toself', name='해리 케인')
rd_1_kulu = go.Scatterpolar(r=df_1['데얀 쿨루세브스키'], theta=df_1['metrics'], fill='toself', name='데얀 쿨루세브스키')
rd_1_bergwijn = go.Scatterpolar(r=df_1['스티븐 베르흐베인'], theta=df_1['metrics'], fill='toself', name='스티븐 베르흐베인')
rd_1_moura = go.Scatterpolar(r=df_1['루카스 모우라'], theta=df_1['metrics'], fill='toself', name='루카스 모우라')

rd_data_1 = [rd_1_son, rd_1_kane, rd_1_kulu, rd_1_bergwijn, rd_1_moura]
rd_fig_1 = go.Figure(data=rd_data_1)
st.plotly_chart(rd_fig_1, user_container_width=True)

st.write("✅ **Highlights**")
st.write("💙 **다섯 선수 중 손흥민이 전체 골 수, 필드 골 수 (패널티 킥이 아닌 경기 중 넣은 골), 슛 정확도, 경기당 패스 수가 가장 높았다.**")
st.write("  ➡️ 패널티 킥 없이 순수 필드골로만 한 시즌에 23골을 넣었기 때문에 득점왕 기록이 더욱 높이 평가된다.")
st.write("💙 **슛 정확도는 57%로 손흥민이 팀 내에서 압도적으로 높다.**")
st.write(
    "  ➡️ 이번 시즌 득점 시도의 약 57%가 골문으로 향했다는 것을 의미한다. 이번 시즌 득점 시도의 약 57%가 골문으로 향했다는 것을 의미한다. 프리미어리그 득점 상위 5명(살라, 호날두, 케인, 마네) 중에서 슛 정확도를 50% 넘긴 선수는 아무도 없다. 득점이 높은 선수는 비교적 많은 슛을 시도하게 되어 있고, 슛을 많이 할 수록 정확성이 작아진다. 손흥민은 순도 높은 슛으로 비교적 적은 슛 80개(살라: 139, 호날두: 110, 케인: 133, 마네: 98)를 시도하고도 득점왕을 차지했다.")
st.write(
    "💙 **결정적 기회 창출은 해리 케인이 가장 높았는데 손흥민과 EPL 최다 골 합작 듀오로 활약하고 있다는 점에서 해리 케인이 기회를 만들면 손흥민이 골을 넣는 두 선수의 파트너십을 확인할 수 있다.**")

st.markdown("""---""")

st.header("2. '우리흥' vs. '옆집살라' : 득점왕을 향한 레이스")
st.write(
    "**이번 시즌에 손흥민과 살라 모두 23골을 넣으며 공동 득점왕에 올랐다.** EPL에서 공동 득점왕이 나온 것은 이번이 5번째다. 두 선수의 득점왕 레이스를 누적 골 수와 EPL 파워랭킹 순위/점수로 살펴봤다.")


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

st.write("✅ **Highlights**")
st.write("💙 **시즌 초반부터 살라가 많은 골을 넣으며 손흥민과 상당한 차이를 보인다. 이 기간동안 토트넘 감독 교체가 있었다.**")
st.write("  ➡️ 10월 30일과 11월 7일 경기 사이에 누누 산투 감독이 경질되고 안토니오 콘테 감독이 새로 토트넘 사령탑이 됐다.")

st.write("💙 **시즌 중반에는 두 선수 각각 부상과 국가대항전으로 인한 결장으로 득점왕 레이스에 잠시 휴식기가 있었다. 두 선수 모두 골 상승이 없는 것을 확인할 수 있다.**")

st.write("  ➡️ 1월에는 손흥민이 햄스트링 부상으로 두 경기 결장했다.")
st.write("  ➡️ 같은 기간, 살라는 아프리카 네이션스컵 출전으로 리그 경기에 출전하지 못했다.")

st.write("💙 **3월부터 두 선수 간 골 차이가 점차적으로 줄기 시작했고 시즌 후반부에 손흥민이 압도적으로 상승하며 살라를 따라잡았다.**")
st.write("  ➡️ 손흥민은 4월 9일 아스톤빌라와의 경기에서 해트트릭을 기록했다.")
st.write("  ➡️ 5월 1일에는 레스터시티와의 경기에서 개인 커리어 리그 한 시즌 최다골을 달성했다.")
st.write(
    "  ➡️ 5월 22일 노리치시티와 리그 최종전에서 멀티골을 터뜨리며 23골로 리그 득점왕이 됐다. 이 날 살라도 울버햄튼과의 경기에서 교체 출전해 한 골을 추가하며 손흥민과 공동 득점왕에 올랐다.")

st.markdown("<h5><br></br></h5>", unsafe_allow_html=True)
################################################################################################

st.subheader("손흥민과 살라의 파워 랭킹💪")
st.write(
    "**영국 스포츠 언론 ‘스카이 스포츠’에서 EPL 선수들에게 최근 성적을 토대로 파워랭킹 점수를 부여한다.** 이번 2021/2022 시즌에는 손흥민이 전체 EPL 선수들 중 파워랭킹 1위와 가장 높은 점수를 받았다. 득점왕 레이스 과정에서 손흥민과 살라의 이번 시즌 파워랭킹 순위와 점수의 변화를 살펴봤다.")

df_2_2 = pd.read_csv("2-2.csv", index_col=0, parse_dates=True)

st.line_chart(df_2_2[["손흥민 파워랭킹 순위", "살라 파워랭킹 순위"]], use_container_width=True)
st.caption(
    "⚠️ 파워랭킹 순위는 EPL 선수 375명 중 n등을 의미하며, 위의 그래프에서는 직관적인 시각화를 위해 이를 거꾸로 적어 놓았다(1위 = 375). 이러한 점을 눈치 챘다면, 당신의 👀관찰력도 월드 클래스?")
st.line_chart(df_2_2[["손흥민 파워랭킹 점수", "살라 파워랭킹 점수"]], use_container_width=True)

st.write("✅ **Highlights**")
st.write("💙 **시즌 초반에는 살라가 손흥민보다 높은 순위와 점수를 유지했다.**")
st.write("  ➡️ 하지만 시즌 중반에 들어서 급격하게 하락하고 동시에 손흥민의 파워랭킹이 급상승했다. 1월에는 두 선수 모두 하락세를 보이다 2월부터 다시 상승세를 탔다.")
st.write("💙 **시즌 후반에 손흥민이 375명의 선수 중 1위와 파워랭킹 점수 9923점을 받았고 살라가 52위, 4163점을 받으며 손흥민이 최종 랭킹 1위로 시즌을 마무리했다.**")

st.markdown("""---""")

st.header("3. 최상위 Big 6 vs. 그 외 14팀")
st.write("**이번 시즌 손흥민과 토트넘의 활약을 맨체스터 시티, 리버풀, 맨체스터 유나이티드, 첼시, 토트넘, 아스널 등 6개 팀으로 이뤄진 Big 6와 그 외 14팀과의 경기로 나누어 비교해봤다.**")

col_3_1, col_3_2 = st.columns(2)

with col_3_1:
    st.write("**손흥민 활약(골+어시스트)**")
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
    st.write("**토트넘 활약(득점)**")
    bar_3_2 = pd.DataFrame({
        '토트넘 활약 평균': [1.3, 2],
        '상대팀': ['Big 6', '그 외 14팀']
    })

    bar_chart_3_2 = alt.Chart(bar_3_2).mark_bar().encode(
        y='토트넘 활약 평균:Q',
        x='상대팀:O',
    )

    st.altair_chart(bar_chart_3_2, use_container_width=True)

st.write("✅ **Highlights**")
st.write("💙**손흥민은 이번 시즌 30득점에 관여했다(골 23, 어시스트 3).**")
st.write(
    "  ➡️ 경기당 평균 0.86의 공격포인트를 획득 했는데, 리그 전체(30경기 이상 출전)를 봤을 때 살라(경기당 1.03) 다음으로 높은 기록이다. 손흥민의 놀라운 점은 여기서 끝나지 않는다. 빅 6 상대로는 경기당 0.89개의 공격포인트로 손흥민 자신의 평균보다 더 높은 성적을 기록했다.")
st.write(
    "💙**시즌 끝까지 우승 경쟁을 했던 맨체스터 시티와 리버풀, 4위 경쟁을 했던 첼시, 아스날, 그리고 맨체스터 유나이티드로 구성된 빅 6과의 경기는 다른 14팀과의 경기보다 골을 넣기 힘든 환경이다.**")
st.write(
    "  ➡️ 실제로 토트넘은 빅 6 제외 나머지 14팀 상대로 평균 2득점을 하였지만, 빅6 상대로 경기했을 때 평균 약 1.3골을 넣는 것에 그쳤다. 빅 6과의 경기는 순위와 직접적으로 연관되어 있는 라이벌 팀이기에 골의 가치가 더 크다. 손흥민은 어려운 경기, 그리고 중요한 경기에서도 꾸준히 높은 집중력을 발휘한 것을 본 그래프로 확인할 수 있다.")


st.markdown("""---""")

st.header("4. 손흥민 활약에 따른 언론보도: 기사빈도수")
st.write("**다음으로 손흥민의 활약에 따른 국내 언론보도 양상을 분석했다.** 손흥민의 골, 어시스트 활약에 따라 전국 일간지 11개에서 보도된 관련 기사 수도 변화하는 것을 확인했다.")
df_4 = pd.read_csv("4.csv", index_col=0, parse_dates=True)
st.bar_chart(df_4[["기사 빈도수"]], use_container_width=True)
st.bar_chart(df_4[["손흥민 골", "손흥민 어시스트"]], use_container_width=True)

st.write("✅ **Highlights**")
st.write("💙 **2021/2022 시즌동안 국내 언론도 손흥민에게 꾸준한 관심을 보였는데 손흥민이 골이나 어시스트를 기록한 경기 전후로 기사 수가 평소보다 많았다.**")
st.write("  ➡️ 평소에 기사 빈도수가 한자릿수를 유지하다 경기 전후로 10개에서 20개 사이로 늘었다.")
st.write("💙 **1, 2월에 손흥민이 부상의 여파로 큰 활약이 없을 때 기사 수도 함께 줄었다.**")
st.write("💙 **본격적으로 득점왕 경쟁에 합류한 4, 5월에 기사 수가 증가했다.**")
st.write("  ➡️ 손흥민이 시즌 후반에 상대적으로 더 많은 활약을 펼쳤는데 언론도 이때 더 많은 관심을 보였다.")
st.write("💙 **득점왕을 달성한 날에는 폭발적으로 많은 기사가 보도됐다.**")
st.write("  ➡️ 토트넘과 노리치 시티의 리그 최종전이 열렸던 5월 23일에 총 87개의 관련 기사가 쏟아졌다. 언론의 높은 관심은 득점왕이 그만큼 이례적이고 역사적인 성취라는 점을 의미한다.")
st.markdown("""---""")

st.header("5. 2021/2022시즌 토트넘 38전 22승 5무 11패 (승률 58%)")

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

st.write("🥳 **승리 Keywords**")
st.write("💙 **득점, 기록: 승리한 경기에서 ‘득점’에 대한 키워드가 가장 크다.**")
st.write("  ➡️ 무승부, 그리고 패배로 내려가면 크기가 더 작아진다. 토트넘이 승리한 경기에서는 보통 손흥민의 ‘득점’을 많이 ‘기록’했기에 부각된 것으로 보인다.")
st.write("💙 **시티: 이번 시즌 우승팀은 맨체스터 “시티”이다.**")
st.write("  ➡️ 하지만 토트넘은 맨체스터 시티와의 경기에서 모두 이겼다. 두 경기 모두 손흥민이 선발 출전 했으며, 리그 개막 경기에는 결승골을 기록했다.")
st.write("💙 **케인: 승리한 경기에서 케인의 글자 크기가 상대적으로 크고, 무승부에서 좀 작아지며, 패배에서는 거의 보이지가 않는다.**")
st.write("  ➡️ 손흥민과 케인은 잉글랜드 최고의 듀오이다. 2월 27일 손흥민의 골을 케인이 도우면서 ‘손-케인’ 합작골을 37개로 늘렸다. 이는 종전 36개를 뛰어넘는 잉글랜드 최고 기록이다.")
st.markdown("""---""")
st.write("🫤 **무승부 Keywords**")
st.write("🖤 **리버풀: 이번 시즌 준우승한 팀은 “리버풀”이다.**")
st.write("  ➡️ 토트넘은 리버풀과의 두 경기 모두 ‘무승부’를 기록했으며, 두 경기 모두 손흥민은 득점했다.")
st.write("🖤 **감독: 리버풀 경기에서 손흥민과 가장 많이 등장한 키워드는 '클롭 리버풀 감독'이다.**")
st.write("  ➡️ 손흥민과 클롭 감독의 우정은 많은 사람들의 관심을 받아왔다. 클롭 감독이 도르트문트를 지휘하던 시절, 손흥민은 그 도르트문트에 많은 골을 넣어서 “양봉장”(도르트문트를 꿀벌로 빚댄 표현)이라는 별명을 얻기도 했다. 클롭은 그런 손흥민을 존중해주었다.")
st.markdown("""---""")
st.write("🥲 **패배 Keywords**")
st.write("❤️‍🩹 **호날두: 토트넘은 이번 시즌 맨유 상대로 2경기 모두 패배했다.**")
st.write("  ➡️ 2경기 모두 “호날두”가 득점했으며, 마지막 경기는 호날두가 헤트트릭을 기록했다.")
st.write("❤️‍🩹 **감독: 누누 감독 시절 토트넘은 패배 비율이 높다(5승 5패).**")
st.write("  ➡️ 3연패를 기록한적도 있는 리그 초반에는  매 경기 패배할 때마다 누누 감독에 대한 경질설이 등장했다. 패배한 경우 ‘감독’에 초점을 둔 기사가 많았기에 ‘감독’이라는 키워드가 다른 상황보다 월등히 큰 것으로 보인다.")
st.write("❤️‍🩹 **승점: 승리했을 경우에는 손흥민의 ‘득점’과 활약에 초점을 둔 반면, 패배했을 경우에는 팀 상황에 초점을 둔 기사가 많이 등장한 것으로 보인다.**")
st.write("  ➡️ 시즌 막바지에 챔피언스리그 결정권이 주어지는 4위 싸움이 치열했다. 토트넘은 추격하는 위치였는데, 패배 했을 경우 경쟁(아스날, 맨유) 팀과의 승점이 얼마나 벌어졌는지 설명하는 기사가 많이 등장했다.")
st.markdown("""---""")

st.header("부록. 경기에 따른 기사 본문")
df_6 = pd.read_csv("6.csv")

option = st.selectbox('경기를 선택해주세요!', df_6['Matches'])

if option is not None:
    df_6_index = str(df_6.index[df_6['Matches'] == option][0])
    img = Image.open("daily/6- "+df_6_index+".jpg")
    st.image(img, width=600)

mask_arr = np.array(Image.open("son.png"))

st.markdown("""---""")

# st.markdown("![Alt Text](https://media.giphy.com/media/ZgQi5Fwlh9OJZbWUhW/giphy.gif)")
# st.markdown("![Alt Text](https://media.giphy.com/media/ftdF2GY6642PdW0dh0/giphy.gif)")
# st.markdown("![Alt Text](https://media.giphy.com/media/l1J9HROlxj1WpN8Xe/giphy.gif)")
# st.markdown("![Alt Text](https://media.giphy.com/media/KLq5znDKUI4xfMjlNo/giphy.gif)")
# st.markdown("![Alt Text](https://media.giphy.com/media/xUA7b1AKW9VlX6Lg64/giphy.gif)")

st.image("son_back.jpg")
st.markdown("<h2 style='text-align: center; color: black;'>☀️ 우리는 손흥민의 시대에 살고 있다. ☀️</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>☀️ It's going to be a SONNY DAY. ☀️</h2>", unsafe_allow_html=True)
# st.image("son_win.jpg")

st.markdown("![Alt Text](https://media.giphy.com/media/UTKiNBL26wBRsK683S/giphy.gif)")
st.markdown("![Alt Text](https://media.giphy.com/media/FrDYUUPYbqBDfqz7mf/giphy.gif)")
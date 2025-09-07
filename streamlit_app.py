import streamlit as st
import pandas as pd

# --- 페이지 설정 ---
# st.set_page_config()는 스크립트에서 가장 먼저 실행되어야 하는 Streamlit 명령입니다.
st.set_page_config(
    page_title="'원형 & 설화' 주간 건강 플랜",
    page_icon="💪",
    layout="wide"
)

# --- 제목 및 소개 ---
st.title("💪 '원형 & 설화' 함께하는 주간 건강 플랜")
st.info(
    """
    **두 분이 함께 건강한 라이프스타일을 만들어가는 여정을 응원합니다!**
    이 앱을 통해 주간 계획을 확인하고, 직접 목표를 입력하며 매일의 작은 성공을 기록해보세요.
    """
)

# --- 탭 구성 ---
tab1, tab2, tab3 = st.tabs(["📅 주간 운동 계획", "🥗 주간 식단 가이드", "📝 이번 주 목표 설정"])

# --- 1. 주간 운동 계획 탭 ---
with tab1:
    st.header("📅 주간 운동 계획 (Weekly Exercise Plan)")
    st.markdown(
        """
        - **목표:** 근력 강화, 체성분 개선, 건강한 습관 형성
        - **주의사항:** 모든 운동은 정확한 자세가 가장 중요합니다. 운동 전 5~10분 정도 가벼운 유산소와 동적 스트레칭으로 몸을 풀어주세요.
        """
    )

    # HTML을 사용하여 테이블 생성 (colspan 기능 활용)
    # Streamlit 앱의 디자인과 일관성을 위해 CSS를 약간 수정하여 가독성을 높였습니다.
    exercise_html_table = """
    <style>
        .custom-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        .custom-table th, .custom-table td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
            vertical-align: top;
        }
        .custom-table thead th {
            background-color: #f2f8ff;
            font-weight: bold;
            color: #333;
        }
        .custom-table tbody tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .custom-table strong {
            color: #0056b3;
        }
    </style>
    <table class="custom-table">
        <thead>
            <tr>
                <th>요일</th>
                <th>운동</th>
                <th>원형님 Focus</th>
                <th>설화님 Focus</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>월요일</strong></td>
                <td>Push Day (가슴, 어깨, 삼두)</td>
                <td>벤치프레스, 오버헤드 프레스 등 무게 증량에 집중하여 근육에 강한 자극 주기</td>
                <td>가벼운 무게의 덤벨 프레스, 푸쉬업(무릎 대고) 등 정확한 자세로 자극 느끼기</td>
            </tr>
            <tr>
                <td><strong>화요일</strong></td>
                <td>Pull Day (등, 이두)</td>
                <td>턱걸이(풀업) 횟수 늘리기, 바벨 로우 중량 늘리기</td>
                <td>랫풀다운, 시티드 로우 등 머신을 활용해 안정적인 자세로 등 근육 전체 자극하기</td>
            </tr>
            <tr>
                <td><strong>수요일</strong></td>
                <td>능동적 회복</td>
                <td>가벼운 조깅 또는 산책 (30-40분)</td>
                <td>함께 요가 또는 스트레칭 영상 보며 따라하기</td>
            </tr>
            <tr>
                <td><strong>목요일</strong></td>
                <td>Leg Day (하체)</td>
                <td>스쿼트, 데드리프트 등 고중량 운동으로 하체 근력 강화</td>
                <td>맨몸 스쿼트, 런지 등 기본에 충실하며 뼈와 근육에 자극 주기, 칼슘 섭취 신경쓰기</td>
            </tr>
            <tr>
                <td><strong>금요일</strong></td>
                <td>전신 운동 & 유산소</td>
                <td>좋아하는 운동 위주로 전신을 가볍게 자극 후, 인터벌 트레이닝(HIIT) 15분</td>
                <td>실내 자전거 또는 빠르게 걷기 30~40분으로 체지방 연소</td>
            </tr>
            <tr>
                <td><strong>토요일</strong></td>
                <td>야외 활동</td>
                <td colspan="2" style="text-align: center;">함께 등산, 자전거 타기, 배드민턴 등 즐거운 활동하기</td>
            </tr>
            <tr>
                <td><strong>일요일</strong></td>
                <td>완전한 휴식</td>
                <td colspan="2" style="text-align: center;">충분한 휴식과 영양 섭취, 다음 주 계획 세우기</td>
            </tr>
        </tbody>
    </table>
    """
    st.markdown(exercise_html_table, unsafe_allow_html=True)


# --- 2. 주간 식단 가이드 탭 ---
with tab2:
    st.header("🥗 주간 식단 가이드 (Weekly Meal Guide)")
    st.markdown(
        """
        - **공통 목표:** 매 끼니 단백질 섭취, 가공식품 줄이기, 충분한 수분 섭취 (하루 1.5L 이상)
        - **팁:** 같은 메뉴를 먹되, 각자의 목표에 맞게 탄수화물(밥, 면)과 단백질(고기, 생선)의 양을 조절합니다.
        """
    )

    meal_data = {
        '구분': ['아침', '점심', '저녁'],
        '월': ['현미밥, 계란찜', '닭가슴살 현미볶음밥', '두부김치, 잡곡밥'],
        '화': ['통밀빵 샌드위치', '고등어구이 백반', '소고기 야채구이'],
        '수': ['그릭요거트, 견과류', '버섯 소고기덮밥', '닭가슴살 카레'],
        '목': ['오트밀, 블루베리', '돼지고기 수육 정식', '해물 순두부찌개'],
        '금': ['현미밥, 된장국', '연어포케', '돼지 안심 스테이크'],
        '토': ['닭가슴살 샐러드', '자유식(외식)', '닭백숙'],
        '일': ['간단한 브런치', '자유식(외식)', '간단한 샐러드']
    }
    meal_df = pd.DataFrame(meal_data).set_index('구분')
    st.dataframe(meal_df, use_container_width=True)

    st.success(
        """
        **설화님을 위한 식단 Tip:**
        - **칼슘 UP:** 식단에 우유, 치즈, 멸치, 두부, 브로콜리 등을 적극적으로 추가해보세요.
        - **건강한 지방:** 아보카도, 견과류, 올리브 오일 등을 샐러드나 간식으로 활용하세요.
        """
    )


# --- 3. 이번 주 목표 설정 탭 ---
with tab3:
    st.header("📝 이번 주 목표 및 메모 (Weekly Goals & Memo)")
    st.write("이번 주에 달성하고 싶은 목표를 직접 입력하고 관리해보세요.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("👨 원형님 목표")
        wonhyung_goal = st.text_area("원형님:", "예: 벤치프레스 무게 2.5kg 올리기", height=150, key="wonhyung_goal")

        st.subheader("👩‍❤️‍👨 함께하는 목표")
        together_goal = st.text_area("함께:", "예: 주말에 1시간 이상 함께 산책하기", height=150, key="together_goal")

    with col2:
        st.subheader("👩 설화님 목표")
        seolhwa_goal = st.text_area("설화님:", "예: 맨몸 스쿼트 15개씩 3세트 성공하기", height=150, key="seolhwa_goal")

    if st.button("목표 저장하기 (새로고침 시 초기화됩니다)"):
        # 입력된 값을 확인하고 성공 메시지를 표시할 수 있습니다.
        # 이 예제에서는 단순히 메시지만 표시합니다.
        st.success("목표가 성공적으로 입력되었습니다!")

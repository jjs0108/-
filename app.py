import streamlit as st

st.set_page_config(page_title="사진 앨범", page_icon="📸")

photo_categories = ["인물", "풍경", "여행", "접사", "패션", "음식", "거리", "스포츠", "연예인", "기타"]

default_photos = [
    {
        "name": "고윤정",
        "types": ["연예인"],
        "year": 2023,
        "url": "https://i.namu.wiki/i/xl7WXBmp2VQ7mQRz53DlZ_7S1O4CEA_6RERhydKMTPYsdK9oXAcvqhtijh_rHQNw1fYt7skGA4vnMOJNg40jQA.webp"
    },
    {
        "name": "축구",
        "types": ["스포츠"],
        "year": 2022,
        "url": "https://image.fmkorea.com/files/attach/new3/20240225/33854530/472743249/6757963452/f8cf1080d27ef00da84d2cc0eb089c40.jpg"
    },
    {
        "name": "런던 여행",
        "types": ["여행"],
        "year": 2019,
        "url": "https://i.namu.wiki/i/a77BHpismbAh9SvuEQ-wQdp_-KNrW2jyCwm9FGpClqtL0nufh7pLCZ969vKtNaBy8J2aoV1moCs5bs4DqDLCQVinn-CI7xZzZp4EQmE5ngj6Jc0X_JUrff0gCRdmfEqCN0S99Im4WVNSgTa5U4urSg.webp"
    },
    {
        "name": "김치찌개",
        "types": ["음식"],
        "year": 2024,
        "url": "https://i.namu.wiki/i/8drgvI-cQLUfJDC00zbl2ZolK4W3o4ZkVSpR-zM5FZk_QzT58vYnx_7ohk0qwGYYiSLPiZgwccyIEFUtYKDjUQ.webp"
    }
]

if "photos" not in st.session_state:
    st.session_state.photos = default_photos

st.title("📸 사진 앨범")
st.markdown("좋아하는 사진을 등록하고 나만의 앨범을 만들어보세요!")

auto_fill = st.toggle("예시 자동입력")
example = default_photos[2]

with st.form("photo_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("사진 이름", value=example["name"] if auto_fill else "")
        year = st.number_input("촬영 연도", 1900, 2100, value=example["year"] if auto_fill else 2024)
    with col2:
        types = st.multiselect("사진 종류", photo_categories, max_selections=2,
                               default=example["types"] if auto_fill else [])
    url = st.text_input("사진 URL", value=example["url"] if auto_fill else "")
    if st.form_submit_button("등록"):
        if not name or not types or not url:
            st.error("모든 항목을 입력해주세요.")
        else:
            st.session_state.photos.append({"name": name, "types": types, "year": year, "url": url})
            st.rerun()

cols_num = st.radio("한 줄 사진 수", [2, 4], horizontal=True)

st.subheader("📷 내 앨범")
for i in range(0, len(st.session_state.photos), cols_num):
    row = st.columns(cols_num)
    for j in range(cols_num):
        if i + j < len(st.session_state.photos):
            photo = st.session_state.photos[i + j]
            with row[j]:
                with st.expander(f"📷 {photo['name']}", expanded=True):
                    st.image(photo["url"], use_container_width=True)  # ← 수정된 부분
                    st.markdown(f"**종류:** {', '.join(photo['types'])}  \n**연도:** {photo['year']}")
                    if st.button("삭제", key=f"del_{i+j}"):
                        del st.session_state.photos[i + j]
                        st.rerun()

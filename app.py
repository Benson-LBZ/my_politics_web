import streamlit as st
from supabase import create_client

# 1. 连接数据库 (这里的变量名要和后面设置的 Secret 一致)
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

st.title("🇲🇾 马来西亚政治评价系统")

# --- 侧边栏：填报资料 ---
st.sidebar.header("发表你的评价")
with st.sidebar.form("review_form"):
    name = st.text_input("议员姓名")
    party = st.selectbox("所属政党", ["PH", "BN", "PN", "GPS", "GRS", "其他"])
    rating = st.slider("评分 (1-10)", 1, 10, 5)
    comment = st.text_area("评价内容")
    submit = st.form_submit_button("提交评价")

    if submit:
        data = {"name": name, "party": party, "rating": rating, "comment": comment}
        response = supabase.table("political_reviews").insert(data).execute()
        st.success("提交成功！")

# --- 主页面：展示数据 ---
st.subheader("最新公众评价")
reviews = supabase.table("political_reviews").select("*").order("created_at", desc=True).execute()

for r in reviews.data:
    with st.container():
        st.write(f"**{r['name']}** ({r['party']}) - ⭐ {r['rating']}/10")
        st.info(r['comment'])
        st.caption(f"发布于: {r['created_at']}")
        st.divider()

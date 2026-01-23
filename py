import streamlit as st
from supabase import create_client

# 1. 这里是连接数据库的设置，稍后会在 Streamlit 填入
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

st.title("🇲🇾 马来西亚政治评价系统")

# --- 侧边栏：填写资料 ---
st.sidebar.header("发表你的评价")
with st.sidebar.form("review_form"):
    name = st.text_input("议员/政治人物姓名")
    party = st.selectbox("所属阵营", ["PH", "BN", "PN", "GPS", "GRS", "其他"])
    rating = st.slider("评分 (1-10)", 1, 10, 5)
    comment = st.text_area("你的评价")
    submit = st.form_submit_button("提交")

    if submit:
        # 把数据推送到 Supabase 数据库
        data = {"name": name, "party": party, "rating": rating, "comment": comment}
        try:
            supabase.table("political_reviews").insert(data).execute()
            st.success("✅ 提交成功！数据已存入数据库。")
        except Exception as e:
            st.error(f"❌ 提交失败: {e}")

# --- 主页面：展示数据库里的数据 ---
st.subheader("📊 最新公众评价")
try:
    reviews = supabase.table("political_reviews").select("*").order("created_at", desc=True).execute()
    for r in reviews.data:
        with st.container():
            st.write(f"**{r['name']}** ({r['party']}) - ⭐ {r['rating']}/10")
            st.info(r['comment'])
            st.caption(f"发布时间: {r['created_at']}")
            st.divider()
except Exception as e:
    st.warning("正在等待数据库连接或暂无数据...")

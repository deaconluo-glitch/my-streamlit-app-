import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="我的Streamlit应用",
    page_icon="🚀",
    layout="wide"
)

st.title("🎉 恭喜！我的第一个Streamlit应用")
st.write("这是一个部署在Streamlit Cloud的示例应用")

# 创建两列布局
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 用户交互")
    name = st.text_input("请输入你的名字：")
    if name:
        st.success(f"你好，{name}！欢迎使用Streamlit！")
    
    age = st.slider("选择你的年龄：", 0, 100, 25)
    st.info(f"年龄：{age}岁")

with col2:
    st.subheader("🎮 功能演示")
    
    if st.button("点击有惊喜！"):
        st.balloons()
        st.write("🎈 太棒了！你触发了惊喜效果！")
    
    # 文件上传示例
    uploaded_file = st.file_uploader("上传一个文件（试试txt或csv）：", type=['txt', 'csv', 'png', 'jpg'])
    if uploaded_file is not None:
        st.write(f"✅ 已上传文件：{uploaded_file.name}")
        st.write(f"📏 文件大小：{uploaded_file.size} 字节")

# 数据可视化示例
st.subheader("📊 数据可视化")

# 生成示例数据
data = pd.DataFrame({
    '月份': ['1月', '2月', '3月', '4月', '5月'],
    '销售额': np.random.randint(100, 1000, 5),
    '用户数': np.random.randint(50, 500, 5)
})

st.dataframe(data)  # 显示表格

# 显示折线图
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['产品A', '产品B', '产品C']
)
st.line_chart(chart_data)

# 底部信息
st.divider()
st.caption("✨ 这个应用已成功部署到 Streamlit Cloud")

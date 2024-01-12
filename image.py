import streamlit as st
import numpy as np
import cv2

st.header("Image Integration")

col1, col2 = st.columns(2, gap="medium")
img11 = None
img22 = None
with col1:
    upd_img1 = st.file_uploader("Upload your first image please")
    if upd_img1 is not None:
        img1 = np.frombuffer(upd_img1.read(), dtype=np.uint8)
        img1 = cv2.imdecode(img1, cv2.IMREAD_COLOR)
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        st.image(img1, use_column_width=False, width=175)
        img11 = img1

with col2:
    upd_img2 = st.file_uploader("Upload your second image please")
    if upd_img2 is not None:
        img2 = np.frombuffer(upd_img2.read(), dtype=np.uint8)
        img2 = cv2.imdecode(img2, cv2.IMREAD_COLOR)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        st.image(img2, use_column_width=False, width=175)
        img22 = img2

if img11 is not None and img22 is not None:
    values = st.slider("select the integration rate", 1, 100, 50) / 100

    img11 = cv2.resize(img11, (256, 256))
    img22 = cv2.resize(img22, (256, 256))

    dst = cv2.addWeighted(img11, (values), img22, (1 - values), 0)
    # st.image(img11 + img22)
    st.image(dst)
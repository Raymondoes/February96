import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="February 96", page_icon="", layout="wide")

# LOAD ASSETS

img_sm64_cap = Image.open("images/SM64_Hat.png")

# HEADER
st.subheader("welcome to February 96 Official Webpage!")
st.title("About February 96")
st.write("february 96 is a romhack that is suppost to be a cartoony/beta version of sm64, the first romhack was being worked on in october 28, 2023 but i have now started from scratch since that romhack sucked")
st.write("- Ilya Mynaev the creator of February 96")
st.write("[join the February 96 team >>](https://forms.gle/UkwKhFnkX8Fv4Dzu9)")

# column section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("February 96")
        st.write("##")
        st.write("""to simplify on what February 96 was about, February 96 is a ROM Hack created by Ilya Mynaev and it is supposed to be a cartoony/beta version of SM64, the first Rom Hack was worked on in October 28.
        but the Creator decided to start from Scratch in order to rework and make it look better, after the official Rom is released this website will be updated with the invite link.
        to make it happen faster, we need more capable devs in the Team to accomplish the Rom Hack.
        """
        )

    with right_column:
        st.image(img_sm64_cap)

import streamlit as st

st.set_page_config(
    page_title="My Father's Poetry",
    page_icon="📖"
)

st.title("📖 My Father's Poetry")

st.write("""
Welcome to my father's poetry collection.

This website preserves his poems for family, friends, and future generations.
""")

st.header("Sample Poem")

st.markdown("""
*Replace this with your father's poem.*

The evening sky was full of dreams,
And memories walked beside the trees.
""")

st.caption("Created with love.")

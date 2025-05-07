import streamlit as st
import importlib.util
import os

st.set_page_config(page_title="ATPG Quiz", layout="wide")
st.title("Intermediate ATPG Question Sets")

base_dir = os.path.dirname(__file__)
assign_dir = os.path.join(base_dir, "assignments")

# Discover sets
sets = sorted(int(f.replace("atpg_set","").replace(".py",""))
              for f in os.listdir(assign_dir)
              if f.startswith("atpg_set") and f.endswith(".py"))
choice = st.sidebar.selectbox("Select Question Set", sets)

# Load selection
mod_path = os.path.join(assign_dir, f"atpg_set{choice}.py")
spec = importlib.util.spec_from_file_location("quiz", mod_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
questions = mod.questions

st.header(f"ATPG Question Set {choice}")
for i, q in enumerate(questions, 1):
    st.markdown(f"**{i}. {q}**")
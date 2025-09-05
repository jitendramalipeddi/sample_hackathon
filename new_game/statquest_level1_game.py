# statquest_level1_full_clean.py
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# App Config
# -----------------------------
st.set_page_config(page_title="StatQuest: Level 1 - Frequency Distribution", layout="wide")

# -----------------------------
# Custom CSS for Bright Theme
# -----------------------------
st.markdown("""
    <style>
        /* Background & text */
        .stApp { background-color: #fdfdfd; color: #222; font-family: "Segoe UI", sans-serif; }

        /* Titles */
        h1, h2, h3, h4 { color: #2c3e50; }

        /* Info/Warning/Success boxes */
        .stAlert { border-radius: 12px; }

        /* Radio buttons */
        .stRadio > label { font-weight: 600; }

        /* Table */
        .dataframe { background: #ffffff; border-radius: 10px; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Intro Story
# -----------------------------
st.title("🕵️ StatQuest: Level 1 - Frequency Distribution")
st.markdown("""
Welcome, **Data Detective!**  
Your first mission is to investigate a mysterious case file.  
You’ll need to **organize raw evidence (data)** into patterns using frequency distributions.  
""")

# -----------------------------
# Step 1: Choose Case Dataset
# -----------------------------
st.subheader("Step 1: Collect the Evidence")

dataset_option = st.selectbox("Choose your case file:", 
    ["📘 Students' Test Scores", "🎲 Dice Rolls in Casino", "🍎 Heights of Apple Trees"])

if dataset_option == "📘 Students' Test Scores":
    data = np.random.randint(0, 101, 30)
    story_context = "A teacher suspects cheating in a class of 30 students. You’ve collected their test scores."
elif dataset_option == "🎲 Dice Rolls in Casino":
    data = np.random.randint(1, 7, 60)
    story_context = "A casino is suspected of using unfair dice. You rolled one dice 60 times to check the outcomes."
else:
    data = np.random.normal(170, 10, 40).astype(int)
    story_context = "A farmer is curious about the growth of 40 apple trees. You measured their heights (cm)."

st.info(story_context)

# Show data in a nice table (instead of raw array)
df = pd.DataFrame(data, columns=["Value"])
st.write("Here’s the **raw evidence** from the case file:")
st.dataframe(df, use_container_width=True)

# -----------------------------
# Step 2: Frequency Distribution (Histogram)
# -----------------------------
st.subheader("Step 2: Organize the Evidence")

num_bins = st.slider("Choose how many bins to group the data into:", 2, 20, 5)

fig, ax = plt.subplots(figsize=(6,4))
ax.hist(data, bins=num_bins, color="#74b9ff", edgecolor="black", alpha=0.9)
ax.set_title(f"Histogram with {num_bins} bins", fontsize=14, color="#2c3e50")
ax.set_xlabel("Value Range")
ax.set_ylabel("Frequency")
st.pyplot(fig)

st.markdown("👉 This is your first clue. Notice how the **shape of the histogram** changes as you adjust the number of bins.")

# -----------------------------
# Step 3: Multiple Mini-Questions
# -----------------------------
st.subheader("Step 3: Crack the Case with Clues")

# Question 1
q1 = st.radio("🔎 Q1: If we increase the number of bins, what happens to the histogram?",
              ["Bars become narrower & show more detail", 
               "Bars become wider & show less detail", 
               "The histogram does not change"])

if q1 == "Bars become narrower & show more detail":
    st.success("✅ Correct! More bins = finer detail, but too many can look noisy.")
elif q1:
    st.warning("🤔 Hint: Splitting into *more* groups shows more details... does that make bars wider or narrower?")

# Question 2
q2 = st.radio("🔎 Q2: Looking at your histogram, which value range seems most **frequent**?",
              ["Low values", "Middle values", "High values"])

if q2:
    if "Test Scores" in dataset_option and q2 == "Middle values":
        st.success("✅ Right! Most students scored in the mid-range.")
    elif "Dice Rolls" in dataset_option and q2 == "All values look similar":
        st.success("✅ Correct! A fair dice should have roughly equal frequencies.")
    elif "Apple Trees" in dataset_option and q2 == "Middle values":
        st.success("✅ Yes! Most tree heights cluster around the average.")
    else:
        st.warning("🔍 Look at the tallest bar in your histogram again.")

# -----------------------------
# Step 4: Wrap-up with Reflection
# -----------------------------
st.subheader("Step 4: Detective’s Reflection")
st.markdown("""
🎯 What we learned in this mission:  
- **Frequency distribution** groups raw data into bins.  
- **Histograms** reveal where the data is concentrated.  
- Adjusting bins changes the **level of detail** we see.  

This is the foundation for **all future statistical investigations!**  
""")

# -----------------------------
# Step 5: Level Unlock
# -----------------------------
if q1 == "Bars become narrower & show more detail" and q2:
    st.balloons()
    st.success("🎉 Congratulations, Detective! You’ve cracked Level 1.")
    st.markdown("🚀 You unlocked **Level 2: Measures of Central Tendency.**")

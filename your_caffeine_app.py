import streamlit as st

# Page configuration
st.set_page_config(page_title="CYP1A2 & Caffeine Metabolism", layout="centered")

# Title and intro
st.title("☕ CYP1A2 Genotype & Caffeine Sensitivity Advisor")
st.markdown("""
This tool helps you understand how your **CYP1A2 genotype** affects your **caffeine metabolism rate** and your body's response to caffeine.

The **CYP1A2** gene encodes an enzyme that metabolizes caffeine in the liver. Variations in this gene (called polymorphisms) can lead to differences in how individuals tolerate caffeine.
""")

# Genotype input
genotype = st.selectbox(
    "Select your CYP1A2 genotype:",
    options=["AA (Fast Metabolizer)", "AC (Intermediate)", "CC (Slow Metabolizer)"]
)

# Show interpretation
if st.button("Interpret"):
    if "AA" in genotype:
        st.success("☀️ Fast Metabolizer")
        st.markdown("""
        **You metabolize caffeine quickly.**
        
        - Caffeine is processed efficiently.
        - You're **less likely to experience negative effects** like anxiety or sleep disruption.
        - Moderate to high caffeine intake (up to 400 mg/day) is usually well-tolerated.
        """)
    elif "AC" in genotype:
        st.warning("🌤️ Intermediate Metabolizer")
        st.markdown("""
        **You process caffeine at a moderate rate.**
        
        - Some sensitivity to caffeine may occur.
        - You should **monitor your intake**, especially in the afternoon.
        - Suggested limit: ~200–300 mg/day.
        """)
    elif "CC" in genotype:
        st.error("🌧️ Slow Metabolizer")
        st.markdown("""
        **You metabolize caffeine slowly.**
        
        - Caffeine stays in your system longer.
        - You’re at **higher risk for side effects** like insomnia, anxiety, or increased heart rate.
        - Suggested limit: below 100–200 mg/day.
        """)

# Optional info box
with st.expander("🔬 What is CYP1A2?"):
    st.markdown("""
    **CYP1A2** is a gene that produces an enzyme responsible for metabolizing various substances, including **caffeine**.

    The most well-studied polymorphism is **CYP1A2*1F**, often associated with faster metabolism when present in two copies (*AA* genotype).

    - Reference: [Cornelis et al., JAMA, 2006](https://jamanetwork.com/journals/jama/fullarticle/202339)
    - Affects caffeine clearance rate, not absorption.
    """)

with st.expander("📊 How much caffeine is in common drinks?"):
    st.markdown("""
    - Espresso (1 shot): ~75 mg  
    - Black coffee (250 ml): ~100 mg  
    - Green tea (250 ml): ~30 mg  
    - Cola (330 ml): ~35 mg  
    - Energy drink (250 ml): ~80–100 mg  
    """)

st.caption("Disclaimer: This tool is for informational purposes only and not medical advice.")



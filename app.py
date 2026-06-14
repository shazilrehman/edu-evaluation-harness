import streamlit as st
from evaluator import run_evaluation_experiment, llm_as_judge

st.title("📊 Edu Evaluation Harness & Experiment Framework")
st.markdown("**LLM-as-Judge** System for Scoring Educational Content")

if st.button("🚀 Run Evaluation Experiment"):
    with st.spinner("Running evaluation on test cases..."):
        results = run_evaluation_experiment()
        st.success("✅ Experiment Completed!")
        st.json(results)

st.caption("This project demonstrates evaluation datasets, scoring mechanisms, and experiment harnesses — key requirement for LearnWith.AI")
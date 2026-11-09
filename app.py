"""Streamlit Grade Calculator — a beginner-friendly five-assignment project."""

import pandas as pd
import streamlit as st

from grade_logic import calculate_grade, letter_grade

# Page settings and a small amount of CSS improve usability.
st.set_page_config(page_title="Grade Calculator", page_icon="🎓", layout="centered")
st.markdown(
    """
    <style>
    .block-container { max-width: 850px; padding-top: 2rem; }
    div[data-testid="stMetric"] { border: 1px solid #dbe2ea; border-radius: 12px; padding: 14px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎓 College Grade Calculator")
st.write("Enter **five assignment scores** and their **percentage weights** to calculate your overall grade.")
st.info("All assignment weights must add up to **100%**. Scores and weights must be between **0 and 100**.")

# Session state stores values so the Reset button can restore defaults.
for i in range(5):
    st.session_state.setdefault(f"score_{i}", 0.0)
    st.session_state.setdefault(f"weight_{i}", 20.0)

st.subheader("Assignment information")
col_names = st.columns([2, 2, 2])
col_names[0].markdown("**Assignment**")
col_names[1].markdown("**Score (0–100)**")
col_names[2].markdown("**Weight (%)**")

scores = []
weights = []
for i in range(5):
    cols = st.columns([2, 2, 2], vertical_alignment="center")
    cols[0].write(f"Assignment {i + 1}")
    scores.append(
        cols[1].number_input(
            f"Assignment {i + 1} score",
            min_value=0.0,
            max_value=100.0,
            step=1.0,
            key=f"score_{i}",
            label_visibility="collapsed",
        )
    )
    weights.append(
        cols[2].number_input(
            f"Assignment {i + 1} weight",
            min_value=0.0,
            max_value=100.0,
            step=1.0,
            key=f"weight_{i}",
            label_visibility="collapsed",
        )
    )

st.caption(f"Total weight: **{sum(weights):g}% / 100%**")

# Button clicks trigger calculation or a complete reset.
action_col, reset_col = st.columns([2, 1])
calculate_clicked = action_col.button("Calculate grade", type="primary", use_container_width=True)
reset_clicked = reset_col.button("Reset", use_container_width=True)

if reset_clicked:
    for i in range(5):
        st.session_state[f"score_{i}"] = 0.0
        st.session_state[f"weight_{i}"] = 20.0
    st.session_state.pop("result", None)
    st.rerun()

if calculate_clicked:
    try:
        average, contributions = calculate_grade(scores, weights)
        st.session_state["result"] = {
            "scores": scores.copy(),
            "weights": weights.copy(),
            "average": average,
            "contributions": contributions,
            "letter": letter_grade(average),
        }
    except ValueError as exc:
        st.session_state.pop("result", None)
        st.error(str(exc))

# Only display a saved calculation if the inputs still match it.
result = st.session_state.get("result")
if result and (result["scores"] != scores or result["weights"] != weights):
    st.session_state.pop("result", None)
    result = None

if result:
    st.divider()
    st.subheader("Your results")
    metric_a, metric_b = st.columns(2)
    metric_a.metric("Weighted average", f"{result['average']:.2f}%")
    metric_b.metric("Letter grade", result["letter"])

    st.markdown("**Calculation breakdown**")
    breakdown = pd.DataFrame(
        {
            "Assignment": [f"Assignment {i + 1}" for i in range(5)],
            "Score (%)": result["scores"],
            "Weight (%)": result["weights"],
            "Contribution (points)": result["contributions"],
        }
    )
    st.dataframe(
        breakdown.style.format(
            {"Score (%)": "{:.2f}", "Weight (%)": "{:.2f}", "Contribution (points)": "{:.2f}"}
        ),
        hide_index=True,
        use_container_width=True,
    )
    formula = " + ".join(
        f"({s:g} × {w:g}/100)" for s, w in zip(result["scores"], result["weights"])
    )
    st.code(f"{formula} = {result['average']:.2f}%", language=None)
    st.caption("Grade scale: A = 90–100, B = 80–<90, C = 70–<80, D = 60–<70, F = below 60.")

st.divider()
st.caption("Built with Python and Streamlit • Your inputs are not uploaded to a database.")

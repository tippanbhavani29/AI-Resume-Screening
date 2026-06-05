import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Recruitment Analytics",
    layout="wide"
)

st.title("📊 Recruitment Analytics Dashboard")

try:

    response = requests.get(
        "http://127.0.0.1:8000/results"
    )

    if response.status_code == 200:

        results = response.json()

        if len(results) == 0:

            st.warning(
                "No screening data available."
            )

        else:

            df = pd.DataFrame(
                results
            )

            # -------------------
            # Metrics
            # -------------------

            total_candidates = len(df)

            avg_skill_score = round(
                df["skill_match_score"].mean(),
                2
            )

            avg_overall_score = round(
                df["overall_match_score"].mean(),
                2
            )

            top_candidate = df.loc[
                df["skill_match_score"].idxmax()
            ]

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Candidates",
                    total_candidates
                )

            with col2:
                st.metric(
                    "Average Skill Match %",
                    avg_skill_score
                )

            with col3:
                st.metric(
                    "Average Overall Match %",
                    avg_overall_score
                )

            with col4:
                st.metric(
                    "Top Candidate",
                    top_candidate["resume_name"]
                )

            st.divider()

            # -------------------
            # Bar Chart
            # -------------------

            st.subheader(
                "🏆 Candidate Ranking"
            )

            fig = px.bar(
                df,
                x="resume_name",
                y="skill_match_score",
                text="skill_match_score",
                title="Skill Match Score by Candidate"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.divider()

            # -------------------
            # Histogram
            # -------------------

            st.subheader(
                "📈 Score Distribution"
            )

            hist_fig = px.histogram(
                df,
                x="skill_match_score",
                nbins=10,
                title="Distribution of Candidate Scores"
            )

            st.plotly_chart(
                hist_fig,
                use_container_width=True
            )

            st.divider()

            # -------------------
            # Top Candidates
            # -------------------

            st.subheader(
                "⭐ Top 5 Candidates"
            )

            top_df = df.sort_values(
                by="skill_match_score",
                ascending=False
            ).head(5)

            st.dataframe(
                top_df[
                    [
                        "resume_name",
                        "overall_match_score",
                        "skill_match_score"
                    ]
                ],
                use_container_width=True
            )

    else:

        st.error(
            f"Backend Error: {response.status_code}"
        )

except Exception as e:

    st.error(
        f"Connection Error: {e}"
    )
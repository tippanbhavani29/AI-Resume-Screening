import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# ----------------------------------

# Page Config

# ----------------------------------

st.set_page_config(
page_title="AI Resume Screening Platform",
layout="wide"
)

# ----------------------------------

# Header

# ----------------------------------

st.title("🤖 AI Resume Screening Platform")

st.markdown(
"Upload multiple resumes and rank candidates against a Job Description."
)

# ----------------------------------

# Inputs

# ----------------------------------

jd_text = st.text_area(
"Job Description",
height=250
)

uploaded_files = st.file_uploader(
"Upload Resume PDFs",
type=["pdf"],
accept_multiple_files=True
)

# ----------------------------------

# Screen Button

# ----------------------------------

if st.button("🚀 Screen Candidates"):


    if not jd_text:

        st.warning(
            "Please enter a Job Description."
        )

    elif not uploaded_files:

        st.warning(
            "Please upload at least one resume."
        )

    else:

        with st.spinner(
            "Screening candidates..."
        ):

            files = []

            for file in uploaded_files:

                files.append(
                    (
                        "resumes",
                        (
                            file.name,
                            file,
                            "application/pdf"
                        )
                    )
                )

            response = requests.post(
                "http://127.0.0.1:8000/screen-multiple-resumes",
                data={
                    "jd_text": jd_text
                },
                files=files
            )

            results = response.json()

        st.success(
            "Screening Complete ✅"
        )

    # ----------------------------------
    # Ranking Data
    # ----------------------------------

    table_data = []

    for candidate in results:

        table_data.append({

            "Rank":
                candidate["rank"],

            "Resume":
                candidate["resume_name"],

            "Overall Match %":
                candidate["overall_match_score"],

            "Skill Match %":
                candidate["skill_match_score"],

            "Recommendation":
                candidate["recommendation"]
        })

    df = pd.DataFrame(
        table_data
    )

    # ----------------------------------
    # Dashboard Metrics
    # ----------------------------------

    total_candidates = len(df)

    top_score = df[
        "Skill Match %"
    ].max()

    avg_score = round(
        df[
            "Skill Match %"
        ].mean(),
        2
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Candidates",
            total_candidates
        )

    with col2:

        st.metric(
            "Top Skill Match %",
            top_score
        )

    with col3:

        st.metric(
            "Average Skill Match %",
            avg_score
        )

    st.divider()

    # ----------------------------------
    # Ranking Table
    # ----------------------------------

    st.subheader(
        "🏆 Candidate Ranking"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    # ----------------------------------
    # Ranking Chart
    # ----------------------------------

    st.subheader(
        "📊 Candidate Ranking Chart"
    )

    fig = px.bar(

        df,

        x="Resume",

        y="Skill Match %",

        color="Recommendation",

        title="Candidate Skill Match Ranking"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ----------------------------------
    # CSV Download
    # ----------------------------------

    csv = df.to_csv(
        index=False
    )

    st.download_button(

        label="📥 Download Results CSV",

        data=csv,

        file_name="candidate_ranking.csv",

        mime="text/csv"
    )

    st.divider()

    # ----------------------------------
    # Candidate Details
    # ----------------------------------

    st.subheader(
        "📄 Candidate Details"
    )

    for candidate in results:

        with st.expander(
            f"Rank {candidate['rank']} - {candidate['resume_name']}"
        ):

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Overall Match %",
                    candidate["overall_match_score"]
                )

            with col2:

                st.metric(
                    "Skill Match %",
                    candidate["skill_match_score"]
                )

            recommendation = candidate[
                "recommendation"
            ]

            if recommendation == "Highly Recommended":

                st.success(
                    recommendation
                )

            elif recommendation == "Recommended":

                st.warning(
                    recommendation
                )

            else:

                st.error(
                    recommendation
                )

            st.markdown(
                "### ✅ Matched Skills"
            )

            for skill in candidate[
                "matched_skills"
            ]:

                st.write(
                    f"✅ {skill}"
                )

            st.markdown(
                "### ❌ Missing Skills"
            )

            if len(
                candidate["missing_skills"]
            ) == 0:

                st.success(
                    "No Missing Skills"
                )

            else:

                for skill in candidate[
                    "missing_skills"
                ]:

                    st.write(
                        f"❌ {skill}"
                    )

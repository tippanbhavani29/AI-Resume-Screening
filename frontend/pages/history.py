import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Screening History",
    layout="wide"
)

st.title("📜 Screening History")

try:

    response = requests.get(
        "http://127.0.0.1:8000/results"
    )

    if response.status_code == 200:

        results = response.json()

        if len(results) == 0:

            st.warning(
                "No screening history available."
            )

        else:

            df = pd.DataFrame(
                results
            )

            st.subheader(
                "Previous Screening Results"
            )

            st.dataframe(
                df[
                    [
                        "resume_name",
                        "overall_match_score",
                        "skill_match_score"
                    ]
                ],
                use_container_width=True
            )

            st.divider()

            st.subheader(
                "Candidate Details"
            )

            for _, row in df.iterrows():

                with st.expander(
                    f"📄 {row['resume_name']}"
                ):

                    st.metric(
                        "Overall Match %",
                        row[
                            "overall_match_score"
                        ]
                    )

                    st.metric(
                        "Skill Match %",
                        row[
                            "skill_match_score"
                        ]
                    )

                    st.markdown(
                        "### ✅ Matched Skills"
                    )

                    matched = row[
                        "matched_skills"
                    ]

                    if matched:

                        for skill in matched.split(","):

                            st.write(
                                f"✅ {skill}"
                            )

                    st.markdown(
                        "### ❌ Missing Skills"
                    )

                    missing = row[
                        "missing_skills"
                    ]

                    if missing:

                        for skill in missing.split(","):

                            st.write(
                                f"❌ {skill}"
                            )

                    else:

                        st.success(
                            "No Missing Skills"
                        )

    else:

        st.error(
            f"Backend Error: {response.status_code}"
        )

except Exception as e:

    st.error(
        f"Connection Error: {e}"
    )
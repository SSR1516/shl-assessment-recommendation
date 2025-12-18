import streamlit as st
import requests

# 🔴 CHANGE THIS ONLY IF BACKEND URL CHANGES
API_URL = "https://shl-assessment-recommendation-mvon.onrender.com/recommend"

st.set_page_config(
    page_title="SHL Assessment Recommendation System",
    page_icon="🔍",
    layout="centered"
)

st.title("🔍 SHL Assessment Recommendation System")
st.markdown(
    "This AI-powered system recommends the most relevant **SHL assessments** "
    "based on natural language hiring requirements."
)

query = st.text_area(
    "Enter hiring requirement / job description",
    placeholder="e.g. Hiring Java developers with communication skills"
)

k = st.slider("Number of recommendations", 5, 20, 10)

if st.button("Get Recommendations"):
    if not query.strip():
        st.warning("Please enter a valid hiring requirement.")
    else:
        try:
            response = requests.post(
                API_URL,
                json={"query": query, "k": k},
                timeout=20
            )

            if response.status_code != 200:
                st.error(
                    f"Backend error ({response.status_code}). Please try again."
                )
            else:
                data = response.json()

                if not data:
                    st.info("No recommendations found.")
                else:
                    st.success("Recommended Assessments")
                    for i, item in enumerate(data, 1):
                        st.markdown(f"### {i}. {item['name']}")
                        st.write(item["description"])
                        st.write(
                            f"""
                            **Test Type:** {", ".join(item["test_type"])}  
                            **Duration:** {item["duration"] or "N/A"} mins  
                            **Remote:** {item["remote_support"]}  
                            **Adaptive:** {item["adaptive_support"]}
                            """
                        )
                        st.markdown(f"[Open Assessment]({item['url']})")
                        st.divider()

        except Exception as e:
            st.error("Unable to connect to backend service.")

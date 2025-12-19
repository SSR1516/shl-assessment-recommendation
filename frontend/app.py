import streamlit as st
import requests

<<<<<<< HEAD
# =========================
# CONFIG
# =========================
API_URL = "https://shl-assessment-recommendation-248h.onrender.com/recommend"

st.set_page_config(
    page_title="SHL Assessment Recommender",
    layout="centered"
)

# =========================
# UI
# =========================
st.title("🔍 SHL Assessment Recommendation System")
st.write(
    "Enter a hiring requirement or job description to get relevant SHL assessments."
)
=======
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
>>>>>>> 7ca0e0de0922d03cc21d735928ee238474ec6df9

query = st.text_area(
    "Hiring requirement / Job description:",
    placeholder="e.g. Looking for Java developers with teamwork and communication skills"
)

top_k = st.slider(
    "Number of recommendations",
    min_value=5,
    max_value=20,
    value=10
)

# =========================
# ACTION
# =========================
if st.button("Get Recommendations"):
    if not query.strip():
<<<<<<< HEAD
        st.warning("⚠️ Please enter a valid query.")
    else:
        with st.spinner("🔄 Fetching recommendations..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"query": query, "k": top_k},
                    timeout=30
                )

                if response.status_code != 200:
                    st.error(
                        f"❌ Backend error ({response.status_code}). Please try again."
                    )
                else:
                    data = response.json()

                    if not isinstance(data, list) or len(data) == 0:
                        st.warning("No recommendations found.")
                    else:
                        st.success("✅ Recommended SHL Assessments")

                        for idx, rec in enumerate(data, start=1):
                            st.markdown(f"### {idx}. {rec.get('name', 'N/A')}")
                            st.markdown(f"[🔗 Open Assessment]({rec.get('url', '#')})")

                            if rec.get("test_type"):
                                st.markdown(
                                    f"**Test Type:** {', '.join(rec['test_type'])}"
                                )

                            if rec.get("duration"):
                                st.markdown(
                                    f"**Duration:** {rec['duration']} minutes"
                                )

                            st.markdown(
                                f"**Remote Support:** {rec.get('remote_support', 'N/A')}"
                            )
                            st.markdown(
                                f"**Adaptive Support:** {rec.get('adaptive_support', 'N/A')}"
                            )

                            st.markdown("---")

            except requests.exceptions.RequestException as e:
                st.error(f"❌ Connection error: {e}")
=======
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
>>>>>>> 7ca0e0de0922d03cc21d735928ee238474ec6df9

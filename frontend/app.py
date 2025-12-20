import streamlit as st
import requests
import time

API_URL = " https://shl-assessment-recommendation-mx8m.onrender.com"
st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")


BASE_URL = " https://shl-assessment-recommendation-mx8m.onrender.com" 

st.set_page_config(
    page_title="SHL Assessment Recommendation System",
    layout="centered"
)

st.markdown(
    """
    <style>
    body {
        background-color: #f5f7fa;
    }
    .main-title {
        font-size: 32px;
        font-weight: 700;
        color: #002b5c;
        text-align: center;
    }
    .subtitle {
        font-size: 16px;
        color: #4f5d75;
        text-align: center;
        margin-bottom: 30px;
    }
    .card {
        background-color: white;
        padding: 18px;
        border-radius: 10px;
        margin-bottom: 15px;
        border-left: 6px solid #002b5c;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">SHL Assessment Recommendation System</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI-powered recommendations for selecting the right SHL assessments</div>',
    unsafe_allow_html=True
)

# ==============================
# INPUT SECTION
# ==============================

query = st.text_area(
    "Hiring requirement / Job description",
    placeholder="e.g. Looking for Java developers with strong collaboration and problem-solving skills"
)

k = st.slider(
    "Number of recommendations",
    min_value=5,
    max_value=10,
    value=10
)

# ==============================
# BACKEND WARM-UP
# ==============================

def warm_up_backend():
    try:
        requests.get(HEALTH_URL, timeout=15)
        time.sleep(1)
        return True
    except:
        return False


# ==============================
# ACTION
# ==============================

if st.button("Get Recommendations"):
    if not query.strip():
        st.warning("Please enter a valid hiring requirement.")
    else:
        with st.spinner("Connecting to SHL recommendation service..."):
            backend_ready = warm_up_backend()

        if not backend_ready:
            st.error(
                "Backend service is waking up (Render cold start). "
                "Please wait a few seconds and try again."
            )
        else:
            with st.spinner("Generating recommendations..."):
                try:
                    response = requests.post(
                        API_URL,
                        json={"query": query, "k": k},
                        timeout=30
                    )

                    if response.status_code == 200:
                        results = response.json().get("recommendations", [])

                        if not results:
                            st.info("No suitable assessments found.")
                        else:
                            st.success("Recommended SHL Assessments")
                            for i, rec in enumerate(results, start=1):
                                st.markdown(
                                    f"""
                                    <div class="card">
                                        <b>{i}. {rec.get("name","")}</b><br>
                                        <a href="{rec.get("url","")}" target="_blank">
                                            View Assessment
                                        </a>
                                    </div>
                                    """,
                                    unsafe_allow_html=True
                                )

                    else:
                        st.error("API returned an error. Please try again later.")

                except requests.exceptions.Timeout:
                    st.error("Request timed out. Backend may still be waking up.")
                except requests.exceptions.ConnectionError:
                    st.error("Unable to connect to backend service.")
                except Exception as e:
                    st.error(f"Unexpected error: {e}")

# ==============================
# FOOTER
# ==============================

st.markdown(
    "<hr><center><small>Powered by SHL Assessment Recommendation System</small></center>",
    unsafe_allow_html=True
)

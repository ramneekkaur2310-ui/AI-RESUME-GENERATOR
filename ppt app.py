#================== STEP 2 ==========================#
#To show web-app: complete page layout
st.set_page_config(layout="wide")

st.title("AI PPT GENERATOR")
st.divider()
st.sidebar.title("Enter API-KEYS")

#====================== STEP 3 =========================#
GOOGLE_API_KEY=st.sidebar.text_input("GOOGLE-API",type="password")
TAVILY_API_KEY=st.sidebar.text_input("TAVILY-API",type="password")

#===================== API VALIDATION ==================#
ALL_API=[GOOGLE_API_KEY,TAVILY_API_KEY]

if not all(ALL_API):
    st.sidebar.error("MUST PASS ALL API-KEYS")

elif all(ALL_API):
    st.sidebar.success("API-KEYS LOADED SUCCESSFULLY")

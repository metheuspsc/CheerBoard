import streamlit as st
import pandas as pd

# Load Excel file
file_path = 'CheerBoard.xlsx'
sheet_names = ['Geral', 'Simplificado', 'Allstar', 'Universitário', 'Campeonatos']
data = pd.read_excel(file_path, sheet_name=None)

# Streamlit Dashboard
st.title("Cheerleading Data Dashboard")

# Dropdown to select the sheet (tab)
tab_selection = st.selectbox("Select the Tab to Visualize", sheet_names)

# Display selected sheet data
if tab_selection == 'Geral':
    df = data['Geral']
    st.subheader("Geral - Ginásio Performance Overview")
    st.dataframe(df)

elif tab_selection == 'Simplificado':
    df = data['Simplificado']
    st.subheader("Simplificado - Overall Performance")
    st.dataframe(df)

elif tab_selection == 'Allstar':
    df = data['Allstar']
    st.subheader("All Star - Cheerleading Zone Rankings")
    st.dataframe(df)

elif tab_selection == 'Universitário':
    df = data['Universitário']
    st.subheader("Universitário - University Rankings")
    st.dataframe(df)

elif tab_selection == 'Campeonatos':
    df = data['Campeonatos']
    st.subheader("Campeonatos - Competition Results")
    st.dataframe(df)

# Additional improvements for visualization
# Auto-resize columns for better readability
st.write("Data Displayed Above")


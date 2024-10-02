import streamlit as st
import pandas as pd


# Load the CSV file from the local repository
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['Ano'] = df['Ano'].astype(str).str.replace(",", "").astype(float).astype(int)
    return df


# Sidebar filters with 'All' option
def sidebar_filters(df):
    st.sidebar.header("Filters")

    # Filter by Campeonato
    campeonatos = st.sidebar.multiselect(
        'Select Campeonato (or leave empty for all)',
        options=df['Campeonato'].unique(),
        default=df['Campeonato'].unique()
    )

    # Filter by Year
    Anos = st.sidebar.multiselect(
        'Select Ano (or leave empty for all)',
        options=df['Ano'].unique(),
        default=df['Ano'].unique()
    )

    # Filter by Ginásio
    Ginásios = st.sidebar.multiselect(
        'Select Ginásio (or leave empty for all)',
        options=df['Ginásio'].unique(),
        default=df['Ginásio'].unique()
    )

    # Filter by Categoria
    Categorias = st.sidebar.multiselect(
        'Select Categoria (or leave empty for all)',
        options=df['Categoria'].unique(),
        default=df['Categoria'].unique()
    )

    # Apply filters
    df_filtered = df[
        (df['Campeonato'].isin(campeonatos)) &
        (df['Ano'].isin(Anos)) &
        (df['Ginásio'].isin(Ginásios)) &
        (df['Categoria'].isin(Categorias))
        ]

    return df_filtered


# Display charts and data
def display_data(df):
    st.title("CheerBoard")

    st.dataframe(df.style.format(thousands=''))  # Show filtered data

    st.subheader("Times por Campeonato")
    campeonatos_count = df['Campeonato'].value_counts()
    st.bar_chart(campeonatos_count)

    st.subheader("Rotinas apresentadas por ano")
    Anos_count = df['Ano'].value_counts()
    st.line_chart(Anos_count)

    st.subheader("Medalhas por Ginásio")
    Ginásio_count = df['Ginásio'].value_counts()
    st.bar_chart(Ginásio_count)

    st.subheader("Participantes por Categoria")
    Categoria_count = df['Categoria'].value_counts()
    st.bar_chart(Categoria_count)


# Main function
def main():
    st.sidebar.title("CheerBoard")

    file_path = "cheerboard.csv"  # Assuming your file is in the same repo
    df = load_data(file_path)

    df_filtered = sidebar_filters(df)
    display_data(df_filtered)


if __name__ == "__main__":
    main()

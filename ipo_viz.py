import pandas as pd
import requests
import streamlit as st


def main():
    st.title('Stock Charts of Last 100 IPOs')

    ipo_url = 'https://www.iposcoop.com/last-100-ipos/'
    r = requests.get(ipo_url)
    df_list = pd.read_html(r.text) 
    df = df_list[0]
    st.dataframe(df)
    st.markdown('Data source: https://www.iposcoop.com/last-100-ipos')
    st.markdown('---')

    with st.spinner('Loading stock charts...'):
        for t in reversed(df.Symbol):
            url = f'https://finviz.com/chart.ashx?t={t}&ty=c&ta=1&p=d&s=l'
            st.image(url, use_column_width=True)
        
    st.markdown('---')
    st.markdown('Visualization: https://finviz.com/')

    # Hide footer
    hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}
    """
    # Hide hamburger menu
    st.markdown(hide_footer_style, unsafe_allow_html=True)
    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
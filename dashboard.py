import streamlit as st
import yfinance as yf
import pandas as pd

tickers = pd.read_html('https://pt.wikipedia.org/wiki/Lista_de_companhias_citadas_no_Ibovespa')[0]
tickers.drop(['Tipo', 'Site'], axis=1, inplace=True)
tickers = tickers.Código.to_list()
acoes = []
for ticker in tickers:
  acoes.append(ticker+'.SA')

st.sidebar.header('Escolha as ações')
st.write(
    """
    **AÇÕES WEB APP **

    """
)

dropdown = st.sidebar.multiselect('Escolha as ações', acoes)

start = st.sidebar.date_input('Data Início', value=pd.to_datetime('2021-01-01'))
end = st.sidebar.date_input('Data Final', value=pd.to_datetime('today'))

def rel_ret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod()-1
    cumret = cumret.fillna(0)
    return cumret

if len(dropdown) > 0:
    
    teste = st.sidebar.checkbox('Variação %')
    if teste:
        df = rel_ret(yf.download(dropdown,start,end)['Adj Close'])
    else:
        df = yf.download(dropdown,start,end)['Adj Close']
    
    df1 = yf.download(dropdown,start,end)['Volume']
    
    st.header('Ações: {}'.format(dropdown))
    st.write('Preço de Fechamento')
    st.line_chart(df)

    st.write('Volume Negociado')
    st.line_chart(df1)
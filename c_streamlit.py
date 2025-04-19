# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import time

# Set Page Configuration
st.set_page_config(page_title="📈 Stock Insights Dashboard", layout="wide")

# --- Animated Home Page ---
def home():
    st.title("🚀 Welcome to the Stock Analysis Dashboard")
    st.subheader("Explore key insights from the Stock Market 📊")
    
    with st.spinner('Loading the magic... ✨'):
        time.sleep(2)
    st.success('Ready to dive into the data! 🎯')
    
    st.markdown("""
    **Insights Available:**  
    - ⚡ Top 10 Most Volatile Stocks  
    - 📈 Top 5 Stocks by Cumulative Return  
    - 🏢 Sector-Wise Performance  
    - 🧠 Stock Price Correlation  
    - 📅 Monthly Top Gainers and Losers
    - Top 5 losers and gainers 
    - Market overview
    """)
    st.balloons()

# --- Volatility Analysis ---
def volatility_analysis():
    st.header("⚡ Top 10 Most Volatile Stocks")
    vol_data = pd.read_csv(r"C:\prj_stock_analysis\datas\volatility\volatility_mean.csv")
    top_vol = vol_data.nlargest(10, 'Volatility Percentage')
    fig = px.bar(
    top_vol, 
    x='Ticker', 
    y='Volatility Percentage', 
    color='Ticker',
    title="Top 10 Most Volatile Stocks")
    st.plotly_chart(fig, use_container_width=True)


# --- Cumulative Return Over Time ---
def cumulative_return_analysis():
        
    df = pd.read_csv(r"C:\prj_stock_analysis\datas\Returns_cum\final_top_5_cum.csv")
    df_sorted = df.sort_values(by='percentage_cum', ascending=False).head(5)
    fig = px.line(df_sorted, x='Ticker', y='percentage_cum', title='Top 5 Cumulative Returns',
                  labels={'percentage_cum': 'Cumulative Return (%)', 'Ticker': 'Stock Ticker'})
    st.plotly_chart(fig)
    

# --- Sector-Wise Performance ---
def sector_performance():
    st.header("🏢 Sector-Wise Average Return")

    # Read sector data
    sector_data = pd.read_csv(r"C:\prj_stock_analysis\datas\sector wise performance\sector_avg_return.csv")

    # Split data into positive and negative returns
    positive_sectors = sector_data[sector_data['Percentage'] > 0]
    negative_sectors = sector_data[sector_data['Percentage'] < 0]

    # Plot positive returns
    st.subheader("📈 Sectors with Positive Average Return")
    fig_positive = px.bar(
        positive_sectors, 
        x='sector', 
        y='Percentage', 
        color='sector',
        title="Positive Sector Average Returns"
    )
    st.plotly_chart(fig_positive, use_container_width=True)

    # Plot negative returns
    st.subheader("📉 Sectors with Negative Average Return")
    fig_negative = px.bar(
        negative_sectors, 
        x='sector', 
        y='Percentage', 
        color='sector',
        title="Negative Sector Average Returns"
    )
    st.plotly_chart(fig_negative, use_container_width=True)


# --- Stock Price Correlation ---
def stock_correlation():
    st.header("🧠 Stock Price Correlation Heatmap")
    corr_df = pd.read_csv(r"C:\prj_stock_analysis\datas\correlation\correlation_matrix.csv", index_col=0)
    corr_df = corr_df.astype(float)

    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_df, annot=False, cmap="coolwarm", linewidths=0.5)
    plt.title("Stock Price Correlation Heatmap")
    st.pyplot(plt.gcf())

# --- Monthly Top Gainers and Losers ---
def monthly_top_movers():
    st.header("📅 Monthly Top Movers")
    df_movers = pd.read_csv(r"C:\prj_stock_analysis\datas\montly returns top gainers and losers\top_5_gainers_losers.csv")  # Update your path

    month_selected = st.selectbox("Select Month:", df_movers['Month'].unique())
    movers_filtered = df_movers[df_movers['Month'] == month_selected]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top 5 Gainers")
        top5 = movers_filtered[movers_filtered['Type'] == 'Top Gainers']
        fig1 = px.bar(top5, x='Ticker', y='Monthly Return (%)', color='Monthly Return (%)', title="Top 5 Gainers")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Top 5 Losers")
        bottom5 = movers_filtered[movers_filtered['Type'] == 'Top Losers']
        fig2 = px.bar(bottom5, x='Ticker', y='Monthly Return (%)', color='Monthly Return (%)', title="Top 5 Losers")
        st.plotly_chart(fig2, use_container_width=True)
def yearly_g_l():

    st.title("📈 Yearly Top Gainers & Losers")

    # Read the already saved CSVs
    top_gainers = pd.read_csv(r"C:\prj_stock_analysis\datas\top yearly gain and losers\top_5_gainers.csv")  # Update your path
    top_losers = pd.read_csv(r"C:\prj_stock_analysis\datas\top yearly gain and losers\top_5_losers.csv")    # Update your path

    st.subheader("🏆 Top 5 Gainers")
    st.dataframe(top_gainers)

    st.subheader("📉 Top 5 Losers")
    st.dataframe(top_losers)

def market_overview():

    st.title("🌍 Market Overview")

    total_green_stocks = 25  
    total_red_stocks = 25   
    avg_latest_close = 2295.34  

    col1, col2, col3 = st.columns(3)

    col1.metric("✅ Total Green Stocks", total_green_stocks)
    col2.metric("❌ Total Red Stocks", total_red_stocks)
    col3.metric("📊 Avg Closing Price", f"{avg_latest_close:.2f}")


# --- Sidebar Navigation ---
st.sidebar.title("Navigation 🚀")
options = ["Home", "Volatility Analysis", "Cumulative Return", "Sector-Wise Performance", "Stock Correlation", "Monthly Top Movers",'yearly gainers and losers','market overview']
choice = st.sidebar.radio("Go to:", options)

# --- Page Management ---
if choice == "Home":
    home()
elif choice == "Volatility Analysis":
    volatility_analysis()
elif choice == "Cumulative Return":
    cumulative_return_analysis()
elif choice == "Sector-Wise Performance":
    sector_performance()
elif choice == "Stock Correlation":
    stock_correlation()
elif choice == "Monthly Top Movers":
    monthly_top_movers()
elif choice == 'yearly gainers and losers':
    yearly_g_l()
elif choice == 'market overview':
    market_overview()

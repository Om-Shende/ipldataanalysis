import streamlit as st
import live_data


def main():
    st.title("Home")

    st.subheader("Live Points Table 2022")
    st.write("This is the Live points Table 2022 Data which is web scraped from the website cricbuzz")
    st.dataframe(live_data.web_scraping_data())

    st.subheader("Welcome to IPL Data Analysis Web App!!!!")
    st.subheader("")
    st.write("Your one-stop web app for all the IPL data and analysis from the year 2008-2021.")

    st.subheader("")
    st.subheader("How does our Web site help you?")
    st.subheader("")

    st.write("Our data analysis is collected from various authentic websites. The collected data is "
             "arranged, organized in such a way that it fills the gaps in information which other"
             " websites fail to provide.")
    st.write("Be it personal changes, points table or ball by ball analysis, all the information along with"
             " analysis is provided in our website. You need not search multiple websites for information,"
             " as we have done that work for you. We collected, comprehended, organized, cleansed the data"
             " and done exploratory data analysis so that you get the information by just one click.")

    st.subheader("")
    st.subheader("The IPL data provided on our site will assist you in")
    st.subheader("")

    st.write("- Making Comparisons among IPL teams")
    st.write("- Strengthen arguments /opinions")
    st.write("- Increase Credibility of your opinion")
    st.write("- Developing content on IPL teams")

    st.subheader("")
    st.subheader("Benefits of Using Our Site")
    st.subheader("")

    st.write("- We have provided infographics of team performance that helps you in understanding the "
             "team and predict the team’s future performance")
    st.write("- Ball by ball analysis gives you information about the net run rate, player performance for"
             "particular year as well as cumulative years")
    st.write("- Personnel changes provide you about the information of particular player’s auction price and "
             "whether he is retained/sold/ not sold.")
    st.write("- Personnel changes also provides Franchise fund details, their overall expenditure on players, "
             "number of overseas players, their price and so on.")
    st.write("- Net worth of IPL player can also be determined looking at his price. Whether it is fluctuating "
             "or holding.")
    st.write("- The points table given in web app gives information on overall team performance, their "
             "earned points in particular year as well as cumulative years.")

    st.subheader("")
    st.subheader("")
    st.write("The site provides you all-in-one information about IPL.")
    st.write("Come explore your interest on IPL and be benefited with our webapp.")

    st.subheader("")
    st.subheader("")
    st.subheader("The Key contributors for the project is")
    st.write("Om Shende")

    st.subheader("")

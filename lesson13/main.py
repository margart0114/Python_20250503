import streamlit as st
import pandas as pd

def main():
    st.title("My Streamlit App")
    st.write("Hello, Streamlit!")

    #Load the CSV file
    df = pd.read_csv("taiwan.csv")

    #Display the DataFrame  
    st.write("以下是'taiwan.csv'的內容:")   
    st.DataFrame(df)
    

if __name__=="__main__":
    main()
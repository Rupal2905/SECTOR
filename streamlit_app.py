import streamlit as st
import pandas as pd

def load_data():
   
    df = pd.read_excel('DATASET.xlsx')
    df.columns = df.columns.str.strip()  
    return df

def filter_data(df, company_name, sector, sub_sector, symbol, supplier_company, customer_company):
    filtered_df = df
    
    if company_name:
        filtered_df = filtered_df[filtered_df['COMPANY NAME'].str.contains(company_name, case=False, na=False)]
    if sector:
        filtered_df = filtered_df[filtered_df['SECTOR'].str.contains(sector, case=False, na=False)]
    if sub_sector:
        filtered_df = filtered_df[filtered_df['SUB SECTOR'].str.contains(sub_sector, case=False, na=False)]
    if symbol:
        filtered_df = filtered_df[filtered_df['SYMBOL'].str.contains(symbol, case=False, na=False)]
    if supplier_company:
        filtered_df = filtered_df[filtered_df['SUPPLIER COMPANY'].str.contains(supplier_company, case=False, na=False)]
    if customer_company:
        filtered_df = filtered_df[filtered_df['CUSTOMER COMPANY'].str.contains(customer_company, case=False, na=False)]
    
    return filtered_df

def supplier_occurrence_by_sector(df, selected_sector):
    sector_df = df[df['SECTOR'].str.contains(selected_sector, case=False, na=False)]
    supplier_count = sector_df['SUPPLIER COMPANY'].value_counts().reset_index()
    supplier_count.columns = ['SUPPLIER COMPANY', 'Occurrences']
    
    return supplier_count

def main():
    st.title("Company Data Filter and Supplier Occurrence")
    df = load_data()
    st.sidebar.header("Filters")
    
    
    company_name = st.sidebar.selectbox("Select Company Name", [""] + list(df['COMPANY NAME'].unique()))
    
    sector = st.sidebar.selectbox("Select Sector", [""] + list(df['SECTOR'].unique()))

    sub_sector = st.sidebar.selectbox("Select Sub Sector", [""] + list(df['SUB SECTOR'].unique()))
    
    symbol = st.sidebar.selectbox("Select Symbol", [""] + list(df['SYMBOL'].unique()))
    
    supplier_company = st.sidebar.selectbox("Select Supplier's Company", [""] + list(df['SUPPLIER COMPANY'].unique()))
    
    customer_company = st.sidebar.selectbox("Select Customer's Company", [""] + list(df['CUSTOMER COMPANY'].unique()))
    
    filtered_df = filter_data(df, company_name, sector, sub_sector, symbol, supplier_company, customer_company)

    selected_sector = st.sidebar.selectbox("Select Sector for Occurrence", filtered_df['SECTOR'].unique())
    
    supplier_count = supplier_occurrence_by_sector(filtered_df, selected_sector)

    st.subheader("Filtered Data")
    if not filtered_df.empty:
        st.dataframe(filtered_df)
    else:
        st.write("No data available with the selected filters.")

    st.subheader(f"Supplier Occurrences in {selected_sector} Sector")
    if not supplier_count.empty:
        st.dataframe(supplier_count)
    else:
        st.write("No suppliers found for the selected sector.")

if __name__ == "__main__":
    main()

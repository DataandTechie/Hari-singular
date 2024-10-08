pip install streamlit
import streamlit as st
import pandas as pd
import plotly.express as px
from numerize.numerize import numerize
import query
from datetime import datetime

result = query.view_all_data()

df=pd.DataFrame(result,columns=['vendor','posted_on','job_title','job_location','category_skill','Employment_type'])
df['posted_on']=df['posted_on'].str.slice(0,10)
df['posted_on']=pd.to_datetime(df['posted_on'], errors='coerce')

st.dataframe(df)
col1,col2 = st.columns((2))
startDate = pd.to_datetime(df['posted_on']).min()
endDate = pd.to_datetime(df['posted_on']).max()
today = datetime.today().date()

with col1:
    date1 = pd.to_datetime(st.date_input('Start Date',today, min_value=startDate, max_value=today))

with col2:
    date2 = pd.to_datetime(st.date_input('End Date',today, max_value=endDate))

df = df[(df['posted_on'] >= date1) & (df['posted_on'] <= date2)].copy()

st.sidebar.header('Filter')

vendor = st.sidebar.multiselect(
    'Select Vendor',
    options= df['vendor'].unique(),
)
if  not vendor:
    df2 = df.copy()
else:
    df2 = df[df['vendor'].isin(vendor)]

# filter job title
job_title = st.sidebar.multiselect(
    'Select job_title',
    options= df2['job_title'].unique(),
)

# filter data bsaed on vendor and job title
if not vendor and not job_title:
    filtered_df = df
elif vendor:
    filtered_df = df2[df['vendor'].isin(vendor)]
elif job_title:
    filtered_df = df2[df['job_title'].isin(job_title)]
else:
    filtered_df = df2[df['vendor'].isin(vendor) & df2['job_title'].isin(job_title)]

print(filtered_df)
print('------------')

vendor_df = filtered_df.groupby('vendor')['job_title'].count().reset_index()

with col1:
    st.subheader('vendor vise positions')
    fig = px.bar(vendor_df, x='vendor', y='job_title',template = 'seaborn')
    st.plotly_chart(fig,use_container_width=True)


    st.subheader('vendor vise positions')
    fig1 = px.pie(vendor_df, values='job_title', names='vendor',hole = 0.5)
    fig1.update_traces(text = filtered_df['vendor'], textposition = 'outside')
    st.plotly_chart(fig1,use_container_width=True)


job_df = filtered_df.groupby('job_title')['vendor'].count().reset_index()


with col2:
    st.subheader('job vise positions')
    fig = px.bar(job_df, x='job_title', y='vendor',template = 'seaborn')
    st.plotly_chart(fig,use_container_width=True)

    st.subheader('job vise positions')
    fig1 = px.pie(job_df, values='vendor', names='job_title',hole = 0.5)
    fig1.update_traces(text = filtered_df['job_title'], textposition = 'outside')
    st.plotly_chart(fig1,use_container_width=True)
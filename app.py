from PIL import Image
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.figure_factory as ff
import plotly.express as px
import numpy as np
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")

def main():
   st.title('Exploratory analysis of banking data')
   @st.cache
   def data_reader():
      df=pd.read_csv('Bank XYZ dataset.csv')
      return df
   df=data_reader()

   with st.sidebar:
      selected=option_menu("Main",['Home','Data','EDA'],icons=['house-fill','clipboard-data','table'],menu_icon='cast',default_index=0)

   if selected=='Home':
      st.subheader('There are a number of factors that influence the rate of defaulting on loans')
      st.write('The various factors that affect the rate of defaulting include; the debt to income ratio, the ability to stay steadly employed, the number of years in employment and level of education')
      bank_img=Image.open('finance.jpg')
      st.image(bank_img,caption='Currency')


   elif selected=='Data':
      st.subheader('Banking Dataset')
      st.dataframe(df)

   elif selected=='EDA':
      st.subheader('Banking data Visualization')
      data_list=['All','Defaulted','Undefaulted']
      data_selector=st.selectbox('Status',data_list)

      default_col,debtinc_col,income_col=st.columns(3)
      


      if data_selector=='All':
         df1=df
         st.dataframe(df1)
      elif data_selector=='Defaulted':
         df1=df[df['default']=='Yes']
         st.dataframe(df1)

      else:
         df1=df[df['default']=='No']
         st.dataframe(df1)
   
      with default_col:
         def default_gram():
            fig = plt.figure(figsize = (8,4))

            plt.bar(df['default'], df['debtinc'])
            plt.xlabel("default status")
            plt.ylabel("debtinc ratio")
            plt.grid(True)
            plt.title("Debtinc ratio to defaulting status")
            st.plotly_chart(fig,use_container_width=True)
            
         default_gram()
      with debtinc_col:
         def debtinc_gram():
            plot = px.histogram(data_frame=df,x='debtinc',color='default', title='Histogram of debtinc ratio')
            st.plotly_chart(plot,use_container_width=True)
         debtinc_gram()
      
      with income_col:
         def income_gram():
            fig=px.histogram(data_frame=df,x='income',color='default',title='Histogram of income')
            st.plotly_chart(fig,use_container_width=True)
         income_gram()
      
main()
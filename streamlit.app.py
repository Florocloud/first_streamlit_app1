import streamlit
streamlit.title('My parents ne healthy Diner')


streamlit.header('breakfast menu')
streamlit.text('🥣 Omega 3 & blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard - Boiled Free - Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# let's put a pick list here so they can pick the fruit they want to include.

streamlit.multiselect("pick some fruits:",list (my_fruit_list.index))
#let's put a pick list here so they can pick the fruit they want  to include
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['avocado','Strawberries'])
#display the table on the page
#fruits_to_show =  my_fruit_list.loc[fruits_selected]
streamlit.dataframe(my_fruit_list)

import snowflake.connector

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hthe fruit load list contains")
#streamlit.text(my_data_row)

streamlit.write('tanks for adding ' , add_my_fruit)

my_cur.execute("insert into fruit_load_list values('from streamlit')")


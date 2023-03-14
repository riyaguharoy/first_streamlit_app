import streamlit;
import pandas;
streamlit.title('My parents new healthy breakfast')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"); 
streamlit.dataframe(my_fruit_list);
#######Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list=my_fruit_list.set_index('Fruit');
fruit_selected=streamlit.multiselect("pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries']);
##fruit_show=my_fruit_list.loc[fruit_selected]
##streamlit.dataframe(fruit_show);
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)
streamlit.text(fruityvice_response.json())
# json data retrive
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# listing data
streamlit.dataframe(fruityvice_normalized)

import openai
from dotenv import load_dotenv
import time
import logging
from datetime import datetime
import os
import requests
import json
import streamlit as st

load_dotenv()

# new_api_key = os.environ.get("NEWS_API_KEY")
new_api_key = os.environ.get("NEWS_API_KEY")


# client = openai.OpenAI()
# model = "gpt-3.5-turbo-16k"

def get_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={new_api_key}&pageSize=5"
    
    try:
        response = requests.get(url)  # Pass URL as argument to requests.get()
        if response.status_code == 200:
            news = json.dumps(response.json(), indent=4)
            news_json = json.loads(news)
            
            data = news_json
            status = data["status"]
            total_results = data["totalResults"]
            articles = data["articles"]
            final_news = []
            
            for article in articles:
                source_name = article["source"]["name"]
                author = article["author"]
                title = article["title"]
                content = article["content"]  # Correct variable name
                url = article["url"]
                title_description = f"""
Title: {title},
Description: {content},  # Correct variable name
Source: {source_name},
Content: {content},
Author: {author},
URL: {url}
"""
                final_news.append(title_description)
            
            return final_news  # Return the list of news
        else:
            print("Error occurred:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

def main():
    # create a input to put the news do we went to see
#   enter_news = input("Enter the news: ")
#   news =  get_news(enter_news)
    
#     # Vérifiez d'abord si la liste de news n'est pas vide
#   if news:
#         for idx, item in enumerate(news, start=1):  # Utilisez enumerate pour obtenir l'index de chaque élément
#             print(f"News {idx}:")
#             print(item)
#             print()  # Ajoutez une ligne vide après chaque nouvelle pour une meilleure lisibilité
#   else:
#         print("No news found for the entered topic.")
 st.title("AI News Generator")
 st.header("Enter the topic")
 st.text("1. Enter the news: ")
 propt = st.text_area("Enter the news: ", placeholder="Enter the news: ", height=20)   
 if st.button("Generate"):
     news =  get_news(propt)
     st.write("some information about the news of: ", propt)
     if news:
         for idx, item in enumerate(news, start=1):  # Utilisez enumerate pour obtenir l'index de chaque élément
             
             print(f"News {idx}:")
             print(item)
             st.write(f"News {idx}:")
             st.info(item)
             st.write()
             print()
             # Ajoutez une ligne vide après chaque nouvelle pour une meilleure lisibilité
     else:
         st.write("No news found for the entered topic About.  ", propt)
         print("No news found for the entered topic.")
       

if __name__ == "__main__":
    main()
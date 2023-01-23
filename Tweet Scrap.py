import snscrape.modules.twitter as snt
import pandas as pd
from pymongo import MongoClient
import json
import streamlit as st
import datetime as dt
from PIL import Image

st.set_page_config(page_title="Twitter Scrapping",page_icon=Image.open(r'C:\Users\SINDHIYA\Downloads\Scrap.jpg'))
st.title(":red[Welcome to our page:exclamation::exclamation::exclamation:]")

st.header(":blue[Scrap tweets from Twitter]")
img =Image.open(r'C:\Users\SINDHIYA\OneDrive\Desktop\twit.jpg')
st.image(img)


tag= st.text_input("Enter the Keyword/Hashtag to scrap:")

tweet_count=st.number_input("Enter the count of data to scrap:",step=1)

from_date=st.date_input("Select From Date:date:")
to_date=st.date_input("Select To date:date:")
tweets=[]
search_tweets= st.checkbox("Click to Search_Tweets")

if search_tweets:
    st.write('Tweets related to your search inputs ')
    Scrap=snt.TwitterSearchScraper("tag from_date to_date")
    for tweet in Scrap.get_items():
        if len(tweets)==tweet_count:
            break
        else:
            req_data={"Date":tweet.date,"ID":tweet.id,"URL":tweet.url,"Content":tweet.rawContent,"Username":tweet.user.username,
                  "Reply Count":tweet.replyCount,"Retweet Count":tweet.retweetCount,
                  "Language":tweet.lang,"Source":tweet.source,"Like Count":tweet.likeCount}
            tweets.append(req_data)
        
    df=pd.DataFrame(tweets)
    st.write(df)
    
    df.to_csv(f"{tag}_Tweets.csv",index=False)
    

    df.reset_index(inplace=True)
    Data_dict =df.to_dict(orient="records")

    display= pd.read_csv(f"{tag}_Tweets.csv")
    #st.write(display)

    client= MongoClient("localhost",27017)
    db=client.Twitter_Scrap
    db.scrap.insert_many(Data_dict)

   
    Data_json= json.dumps(Data_dict,default=str)
    

    data_format = display.to_csv(index=False).encode("utf-8")

    
    Download_1= st.download_button("Download json",data=df.to_json(),
                                file_name=f"{tag}_Tweets.json")
    if Download_1:

        st.success('Your file is sucessfully downloaded',icon="✅")


    Download=st.download_button("Download CSV",data=data_format,
                                file_name=f"{tag}_Tweets.csv",mime="text/csv")

    if Download:
        st.success('Your file is sucessfully downloaded',icon="✅")


        st.text("Thanks for using our page.Visit us again !!!")
        


        
st.markdown("**Was this page helpful?**")
col1,col2=st.columns(2)
with col1:
    st.button(":thumbsup:  Yes")
with col2:
    st.button(":thumbsdown:  No")
        




   

  

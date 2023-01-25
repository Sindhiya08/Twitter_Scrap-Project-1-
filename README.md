

https://user-images.githubusercontent.com/118071774/214391971-e5cbf57b-e415-4372-97b5-9d757967d87d.mp4

# Twitter Scrap using snscrape

In this, we are going to see how to scrap tweets from Twitter using python and its packages.

Before proceeding, we have to install the required packages. If not installed, install the required packages using --> ***pip install <package_name>***

Packages/libraries used -  * Snscrape, Pandas, Streamlit, PyMongo, Pillow , Datetime *

To extract the tweets by searching the required number of tweets by Hashtag/keyword from particular date range using modules.twitter in snscrape

Refer to the code file.

In this code, tweets are extracted using snscrape.modules.twitter and the extracted data is displayed to the user using Pandas DataFrame which can be stored in the Database if the user chooses so. Later the user will be given an option to download the extracted data in the different formats( json & csv)

Here, we are using Mongodb by importing pymongo library to store the data.

All the visualized elements are done using streamlit library in python which will be viewable to the user in a webpage.

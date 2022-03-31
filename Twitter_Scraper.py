import twint
import pandas as pd
#import nest_asyncio

#nest_asyncio.apply()

c = twint.Config()
#c.Limit = 
c.Search = "#ecofriendly" or "#zerowaste" or "#plasticfree"
#c.Username = "sfbart"
c.Since = "2021-1-1"
#c.To = "2020-1-1"
c.until= '2022-01-1'
c.Store_csv = True
c.Custom_csv = ["date", "time", "username", "tweet", "link", "likes", "retweets", "replies", "mentions", "hashtags"]
c.Pandas = True
c.Output = "eco1friendly.csv"

#dataframes.append(df)

twint.run.Search(c)


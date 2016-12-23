# Kishore Prasad
# Data 602 - HW Assignment 9

import Tkinter
import tkFileDialog
import pandas as pd

root = Tkinter.Tk()
root.withdraw()

# read the data file from a file prompt
filename = tkFileDialog.askopenfilename(parent=root)
http_data = pd.read_csv(filename, delimiter = " ", names = ["host","date", "request", "reply", "bytes"],  header=None)

# Generate Datetime column
http_data["date"] = pd.to_datetime("1995-08" + http_data["date"], format="%Y-%m[%d:%H:%M:%S]")

# Fix sizes that contain "-" to nan
http_data["bytes"] = pd.to_numeric(http_data["bytes"], errors="coerce")

#Which hostname or IP address made the most requests?
highest_requests = http_data.groupby("host").count().sort_values(by="request", ascending=False)
print '"%s" made the most requests : %d \n' %(highest_requests.index[0], highest_requests.iloc[0,0])

#Which hostname or IP address received the most total bytes from the server?  How many bytes did it receive? 
highest_total_bytes = http_data.groupby("host")["bytes"].sum().sort_values(ascending=False)
print '"%s" received the most total bytes from the server : %.0f bytes\n' %(highest_total_bytes.index[0], highest_total_bytes.iloc[0])

#During what hour was the server the busiest in terms of requests?  (You can do this by grouping each hour period e.g. 13:00 – 14:00. Then count the number of requests in each hour)
http_data["hour"]= http_data["date"].dt.hour.astype(str) + " - " + (http_data["date"].dt.hour + 1).astype(str)
busiest_hour = pd.groupby(http_data, "hour").size().sort_values(ascending=False)
print 'Between %s, the server was the busiest with %d requests\n' %(busiest_hour.index[0], busiest_hour.iloc[0])

#Which .gif image was downloaded the most during the day?
downloaded_gifs = http_data.request.str.extract('(?P<gifname>/.*.gif)', expand=True)
downloaded_gifs = downloaded_gifs.gifname.value_counts()
print 'The most downloaded gif was "%s" with %d downloads\n' %(downloaded_gifs.index[0], downloaded_gifs.iloc[0])

#What HTTP reply codes were sent other than 200?
reply_codes = http_data['reply'].unique().astype(int)
other_than_200 = reply_codes[reply_codes > 200]
print 'The following HTTP codes were replied with apart from 200: %s.\n' %', '.join(other_than_200.astype(str))


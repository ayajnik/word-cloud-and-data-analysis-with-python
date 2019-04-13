print "\n Run by Ayush Yajnik."

import pandas as pd
import csv
import matplotlib.pyplot as plt

from wordcloud import WordCloud


data123 = pd.read_csv('H_Clinton-emails.csv')

sender = data123.MetadataFrom.tolist()
senderunique = set(sender) #list of unique senders

Content = data123.RawText.tolist() #list of content
count = data123['MetadataFrom'].value_counts()

descending_names = count.sort_values(ascending = False)
print '\nThe top 15 senders:\n', descending_names.head(15)

MYlist = []
with open('H_Clinton-emails.csv', 'rb') as a:
    reader = csv.reader(a)
    MYlist = '\t'.join([i[21] for i in reader])


wordcloud = WordCloud(max_font_size=40).generate(MYlist) #generate a word cloud image

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

#Display the generated image:
plt.figure()
num = ['H','Abedin Huma','Mills Cheryl D' ,'Sullivan Jacob J','sbwhoeop','Jiloty Lauren C','Valmoro Lona J','Slaughter Anne-Marie','Verma Richard R' ,'PIR ' ,'McHale Judith A','hrod17@clintonemail.com','Muscatine Lissa','MillsCD@state.gov','Verveer Melanne S' ]

xaxis = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14] #set values for the x-axis
plt.bar(xaxis,descending_names.head(15),align="center") #create the bar chart 

plt.xticks(xaxis, num, rotation = 90) #assign labes to the x-axis 
plt.show()

    



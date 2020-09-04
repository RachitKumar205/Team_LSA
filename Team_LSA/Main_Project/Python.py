from profanity_filter import ProfanityFilter
import pandas as pd

# Create a ProfanityFilter() object
pf = ProfanityFilter()

# Get the CSV file. Currently looks for data only under the column Name, and stores in variable: data
#data = pd.read_csv("mydata.csv", sep = ',', usecols=["tweet_text"], squeeze = True)

# Converts variable: data to string array
#final = list(data)

# Prints the value stored under the array: final
#print(final[0])

#length = len(final)
#print(length)

#Fetches the string: "cd" in the array: final and returns its index value
#print(final.index("cd"))


#We are reading the columns and storing them. The default file is mydata.csv - Change it as needed. Dont change the column name
text = pd.read_csv("mydata.csv", sep = ",", usecols = ["tweet_text"], squeeze = True)
user = pd.read_csv("mydata.csv", sep = ",", usecols = ["username"], squeeze = True)

#Converting the stored data into lists
text_list = list(text)
user_list = list(user)
   
# Getting length of list 
length = len(text_list)
i = 0
   
# Iterating using while loop 
while (i < length): 
    if(pf.is_profane(text_list[i])):
        print("Bullying Detected. User" + " " + user_list[i])
    else:
        print("No bullying detected")
    i += 1
    




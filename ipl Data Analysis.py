#importing the required libraries
import pandas as pd

#loading the ipl data from csv file to DataFrame object
ipl_data = pd.read_csv('IPL Matches.csv')

#showing the first five records of ipl dataset
print(ipl_data.head())


#finding the number of rows and columns in ipl dataset
print(ipl_data.shape)

#Getting the information of all columns of ipl dataset
ipl_data.info()


#Getting total number of player of match awards
print(ipl_data['player_of_match'].value_counts())


#Getting top 10 players with most player of match awards
print(ipl_data['player_of_match'].value_counts()[0:10])

#Getting names of top 10 players with most player of match awards
print(list(ipl_data['player_of_match'].value_counts()[0:10].keys()))

#Getting number of player of match awards of top 10 players
print(list(ipl_data['player_of_match'].value_counts()[0:10]))

#Getting frequency of result column
print(ipl_data['result'].value_counts())

#Finding how many times every team won the toss  
print(ipl_data['toss_winner'].value_counts())

#Extracting records where team batting first won the match  
batting_first_data = ipl_data[ipl_data['result'] == 'runs']
print(batting_first_data.shape)

print(batting_first_data.head())

#Finding how many times each team won batting first
print(batting_first_data['winner'].value_counts())

batting_second_data = ipl_data[ipl_data['result'] == 'wickets']
print(batting_second_data.shape)
print(batting_second_data.head())

#Finding out how many times each team won matches batting second
print(batting_second_data['winner'].value_counts())

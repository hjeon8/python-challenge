import os
import csv

budget_data = os.path.join('..', 'Resources', 'election_data.csv')
a = budget_data["Voter ID"].count()
b = training_data["Candidate"].value_counts()
percent = b/a*100
winner = index(max(b))

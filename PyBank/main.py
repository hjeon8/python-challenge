import os
import csv

budget_data = os.path.join('..', 'Resources', 'budget_data.csv')


budget_data["Date"].count()
budget_data["Profit/Losses"].sum()
budget_data["Profit/Losses"].mean()
budgetmax = budget_data["Profit/Losses"].max()
budget_data["Profit/Losses"].min()
budget_data["Date"].index(max(budgetmax))

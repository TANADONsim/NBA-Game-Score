# Observing NBA Game Score as a Stat Line
Observing Game Score of daily leaders and what it shows us about a player's/team's match performance.

## What is Game Score?
1. This statistic was invented by John Hollinger to provide a rough measure of a player's performance in a given game.  The scale upon which the player's game score is based is the same as points scored.  If a player has a game score of 40, that is amazing, while a game score of 10 is average.
2. The formula for calculating game score is as follows: (Points x 1.0) + (FGM x 0.4) + (FGA x -0.7) + ((FTA-FTM) x -0.4) + (OREB x 0.7) + (DREB x 0.3) + (STL x 1.0) + (AST x 0.7) + (BLK x 0.7) + (PF x -0.4) + (TO x -1.0). 

As can be plainly seen, this statistic takes into account almost everything a player does during a game that can be quantified.  These statistics are then weighted and added together to get a game score.  This method is similar to Dr. Dean Oliver's Four Factors, but attempts to add value by considering all the stats, rather than just the four most important ones.

## The Data 
We take a look at the NBA Daily Stat Leaders according to [https://www.basketball-reference.com](https://www.basketball-reference.com/friv/dailyleaders.fcgi?month=11&day=1&year=2018) from 01/11/2018 to 27/11/2018.

## Building the code to get the data 
```
import urllib3
import csv
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import datetime
```
These are the modules we imported into our Python codes:    
**urllib3** is a powerful HTTP client for Python.  
**csv** allows us to import or export spreadsheets and databases for use in the Python interpreter.  
**BeautifulSoup** is a Python library for pulling data out of HTML and XML files.  
**datetime** provides a number of function to deal with dates, times and time intervals.

import pandas as pd
import numpy as np

import sqlite3

database='database.sqlite'
conn = sqlite3.connect(database)

tables=pd.read_sql("""SELECT *
                    FROM sqlite_master
                    WHERE type='table';""", conn)
print(tables)

team=pd.read_sql("""SELECT * FROM Team;""", conn)
print(team)

season=pd.read_sql("""SELECT * FROM Season;""", conn)
print(season)

csk_matches_2015=pd.read_sql("""SELECT Match_Id,Team_2 AS Away_Team,Toss_Winner,Match_Winner
                            FROM Match
                             WHERE Team_1=
                             (SELECT Team_1 FROM Match WHERE Team_1==3 AND Season_Id==8)""", conn)

print("Matches played by Chennai Super Kings in 2015:")
print(csk_matches_2015)

csk_wins=pd.read_sql("""SELECT *
                     FROM Match
                     WHERE Match_Winner==3 AND Season_Id==8;""", conn)

print(csk_wins)

match_runs=pd.read_sql("""SELECT Match_Id,Runs_Scored AS Total_Runs,Innings_No
                       FROM BatsmAn_Scored
                       WHERE Total_Runs>5 AND Match_Id IN
                       (SELECT Match_Id 
                        FROM Match
                        WHERE Season_Id==8)""", conn)

print("Matches with scored runs greater than 5 in 2015:")
print(match_runs)

avg_runs=pd.read_sql("""SELECT Match_Id,Runs_Scored AS Total_Runs,Innings_No
                       FROM BatsmAn_Scored
                     WHERE Innings_No==1 AND Runs_Scored>
                     (SELECT AVG(Runs_Scored)
                      FROM BatsmAn_Scored)""", conn)

print("Matches with scored runs greater than average scored runs:")
print(avg_runs)
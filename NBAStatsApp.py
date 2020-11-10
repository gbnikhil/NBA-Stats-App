from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from functools import partial
import pymysql

t=Tk()

def sel_team_info(x1):
    n1=x1.get()
    sql="select t1.team_name,t1.team_short_name,t1.active,t1.years,t1.champions,t1.total_games,t1.total_wins,t1.total_losses,TRUNCATE(((t1.total_wins/t1.total_games)*100),2) as Win_Loss_Percentage,sum(t2.minutes_played),sum(t2.field_goals_made),sum(t2.3_Point_field_goals_made),sum(t2.2_Point_field_goals_made),sum(t2.free_throws_made),sum(t2.offensive_rebounds),sum(t2.defensive_rebounds),sum(t2.total_rebounds),sum(t2.assists),sum(t2.steals),sum(blocks),sum(t2.turnovers),sum(t2.personal_fouls),sum(t2.points),t1.other_names from teams_info t1,teams_season_stats t2 where t1.team_name=%s and t1.team_id=t2.team_id group by t1.team_name"
    cr.execute(sql,n1)
    final=cr.fetchall()
    messagebox.showinfo("Team Info","Name : "+str(final[0][0])+"\n"+"-------------------------------------------------------------------------"+"\n"+"Short Name : "+str(final[0][1])+"\n"+"Active : "+str(final[0][2])+"\n"+"No. of Years in Association : "+str(final[0][3])+"\n"+"Champions : "+str(final[0][4])+"\n"+"Games Played : "+str(final[0][5])+"\n"+"Wins : "+str(final[0][6])+"\n"+"Losses : "+str(final[0][7])+"\n"+"Win-Loss Percentage : "+str(final[0][8])+"\n"+"Minutes Played : "+str(final[0][9])+"\n"+"Field Goals Made : "+str(final[0][10])+"\n"+"3-Points Scored : "+str(final[0][11])+"\n"+"2-Points Scored : "+str(final[0][12])+"\n"+"Free Throws Made : "+str(final[0][13])+"\n"+"Offensive Rebounds : "+str(final[0][14])+"\n"+"Defensive Rebounds : "+str(final[0][15])+"\n"+"Total Rebounds : "+str(final[0][16])+"\n"+"Assists : "+str(final[0][17])+"\n"+"Steals : "+str(final[0][18])+"\n"+"Blocks : "+str(final[0][19])+"\n"+"Turnovers : "+str(final[0][20])+"\n"+"Personal Fouls : "+str(final[0][21])+"\n"+"Points Scored : "+str(final[0][22])+"\n"+"Other Names : "+str(final[0][23]))

def sel_player_info(x7):
    n2=x7.get()
    sql="select p1.player_name,p1.player_full_name,p1.birth_place,p1.height,p1.weight,p1.retired, p1.position,sum(p2.minutes_played),sum(p2.field_goals),sum(p2.3_Point_field_goals), sum(p2.free_throws),sum(p2.offensive_rebounds),sum(p2.defensive_rebounds),sum(p2.total_rebounds), sum(p2.assists),sum(p2.steals),sum(p2.blocks),sum(p2.turnovers),sum(p2.personal_fouls),sum(p2.points) from players_info p1,player_game_stats p2 where p1.player_name=%s and p1.player_id=p2.player_id group by p1.player_id"
    cr.execute(sql,n2)
    final=cr.fetchall()
    messagebox.showinfo("Player Info","Name : "+str(final[0][0])+"\n"+"Full Name : "+str(final[0][1])+"\n"+"-------------------------------------------------------------------------"+"\n"+"Birth Place : "+str(final[0][2])+"\n"+"Height : "+str(final[0][3])+"\n"+"Weight : "+str(final[0][4])+"\n"+"Retired : "+str(final[0][5])+"\n"+"Position : "+str(final[0][6])+"\n"+"Minutes Played : "+str(final[0][7])+"\n"+"Field Goals made : "+str(final[0][8])+"\n"+"3-Points Scored : "+str(final[0][9])+"\n"+"Free Throws : "+str(final[0][10])+"\n"+"Offensive Rebounds : "+str(final[0][11])+"\n"+"Defensive Rebounds : "+str(final[0][12])+"\n"+"Total Rebounds : "+str(final[0][13])+"\n"+"Assists : "+str(final[0][14])+"\n"+"Steals : "+str(final[0][15])+"\n"+"Blocks : "+str(final[0][16])+"\n"+"Turnovers : "+str(final[0][17])+"\n"+"Personal Fouls : "+str(final[0][18])+"\n"+"Points : "+str(final[0][19]))

def sel_coach_info(x13):
    n3=x13.get()
    sql="select c1.coach_name,c1.years_coaching,c1.retired,sum(c2.regular_season_games),sum(c2.regular_season_wins),sum(c2.regular_season_losses),TRUNCATE(((sum(c2.regular_season_wins)/sum(c2.regular_season_games))*100),2),sum(c2.playoff_games),sum(c2.playoff_wins),sum(c2.playoff_losses),TRUNCATE(((sum(c2.playoff_wins)/sum(c2.playoff_games))*100),2) from coaches_info c1,coaches_season_stats c2 where coach_name=%s and c1.coach_id=c2.coach_id group by c1.coach_name"
    cr.execute(sql,n3)
    final=cr.fetchall()
    messagebox.showinfo("Coach Info","Name : "+str(final[0][0])+"\n"+"-------------------------------------------------------------------------"+"\n"+"Years Coaching : "+str(final[0][1])+"\n"+"Retired : "+str(final[0][2])+"\n"+"Regular Season Games : "+str(final[0][3])+"\n"+"Regular Season Wins : "+str(final[0][4])+"\n"+"Regular Season Losses : "+str(final[0][5])+"\n"+"Regular Season Win-Loss Percentage : "+str(final[0][6])+"\n"+"Playoff Games : "+str(final[0][7])+"\n"+"Playoff Wins : "+str(final[0][8])+"\n"+"Playoff Losses : "+str(final[0][9])+"\n"+"Playoff Win-Loss Percentage : "+str(final[0][10]))

def comp_teams(x4,x5):
    n4=x4.get()
    n5=x5.get()
    sql="select t1.team_name,t1.team_short_name,t1.active,t1.years,t1.champions,t1.total_games,t1.total_wins,t1.total_losses,TRUNCATE(((t1.total_wins/t1.total_games)*100),2) as Win_Loss_Percentage,sum(t2.minutes_played),sum(t2.field_goals_made),sum(t2.3_Point_field_goals_made),sum(t2.2_Point_field_goals_made),sum(t2.free_throws_made),sum(t2.offensive_rebounds),sum(t2.defensive_rebounds),sum(t2.total_rebounds),sum(t2.assists),sum(t2.steals),sum(blocks),sum(t2.turnovers),sum(t2.personal_fouls),sum(t2.points),t1.other_names from teams_info t1,teams_season_stats t2 where t1.team_name in (%s,%s) and t1.team_id=t2.team_id group by t1.team_name"
    cr.execute(sql,(n4,n5))
    final=cr.fetchall()
    messagebox.showinfo("Teams Head-to-Head","Name : "+str(final[0][0])+"\n"+"-------------------------------------------------------------------------"+"\n"+"Short Name : "+str(final[0][1])+"\n"+"Active : "+str(final[0][2])+"\n"+"No. of Years in Association : "+str(final[0][3])+"\n"+"Champions : "+str(final[0][4])+"\n"+"Games Played : "+str(final[0][5])+"\n"+"Wins : "+str(final[0][6])+"\n"+"Losses : "+str(final[0][7])+"\n"+"Win-Loss Percentage : "+str(final[0][8])+"\n"+"Minutes Played : "+str(final[0][9])+"\n"+"Field Goals Made : "+str(final[0][10])+"\n"+"3-Points Scored : "+str(final[0][11])+"\n"+"2-Points Scored : "+str(final[0][12])+"\n"+"Free Throws Made : "+str(final[0][13])+"\n"+"Offensive Rebounds : "+str(final[0][14])+"\n"+"Defensive Rebounds : "+str(final[0][15])+"\n"+"Total Rebounds : "+str(final[0][16])+"\n"+"Assists : "+str(final[0][17])+"\n"+"Steals : "+str(final[0][18])+"\n"+"Blocks : "+str(final[0][19])+"\n"+"Turnovers : "+str(final[0][20])+"\n"+"Personal Fouls : "+str(final[0][21])+"\n"+"Points Scored : "+str(final[0][22])+"\n"+"Other Names : "+str(final[0][23])+"\n"+"***************************************************************"+"Name : "+str(final[1][0])+"\n"+"-------------------------------------------------------------------------"+"\n"+"Short Name : "+str(final[1][1])+"\n"+"Active : "+str(final[1][2])+"\n"+"No. of Years in Association : "+str(final[1][3])+"\n"+"Champions : "+str(final[1][4])+"\n"+"Games Played : "+str(final[1][5])+"\n"+"Wins : "+str(final[1][6])+"\n"+"Losses : "+str(final[1][7])+"\n"+"Win-Loss Percentage : "+str(final[1][8])+"\n"+"Minutes Played : "+str(final[1][9])+"\n"+"Field Goals Made : "+str(final[1][10])+"\n"+"3-Points Scored : "+str(final[1][11])+"\n"+"2-Points Scored : "+str(final[1][12])+"\n"+"Free Throws Made : "+str(final[1][13])+"\n"+"Offensive Rebounds : "+str(final[1][14])+"\n"+"Defensive Rebounds : "+str(final[1][15])+"\n"+"Total Rebounds : "+str(final[1][16])+"\n"+"Assists : "+str(final[1][17])+"\n"+"Steals : "+str(final[1][18])+"\n"+"Blocks : "+str(final[1][19])+"\n"+"Turnovers : "+str(final[1][20])+"\n"+"Personal Fouls : "+str(final[1][21])+"\n"+"Points Scored : "+str(final[1][22])+"\n"+"Other Names : "+str(final[1][23]))

def comp_players(x10,x11):
    n6=x10.get()
    n7=x11.get()
    sql="select p1.player_name,p1.player_full_name,p1.birth_place,p1.height,p1.weight,p1.retired, p1.position,sum(p2.minutes_played),sum(p2.field_goals),sum(p2.3_Point_field_goals), sum(p2.free_throws),sum(p2.offensive_rebounds),sum(p2.defensive_rebounds),sum(p2.total_rebounds), sum(p2.assists),sum(p2.steals),sum(p2.blocks),sum(p2.turnovers),sum(p2.personal_fouls),sum(p2.points) from players_info p1,player_game_stats p2 where p1.player_name in (%s,%s) and p1.player_id=p2.player_id group by p1.player_id"
    cr.execute(sql,(n6,n7))
    final=cr.fetchall()
    messagebox.showinfo("Players Head-to-Head","Name : "+str(final[0][0])+"\n"+"Full Name : "+str(final[0][1])+"\n"+"-------------------------------------------------------------------------"+"\n"+"Birth Place : "+str(final[0][2])+"\n"+"Height : "+str(final[0][3])+"\n"+"Weight : "+str(final[0][4])+"\n"+"Retired : "+str(final[0][5])+"\n"+"Position : "+str(final[0][6])+"\n"+"Minutes Played : "+str(final[0][7])+"\n"+"Field Goals made : "+str(final[0][8])+"\n"+"3-Points Scored : "+str(final[0][9])+"\n"+"Free Throws : "+str(final[0][10])+"\n"+"Offensive Rebounds : "+str(final[0][11])+"\n"+"Defensive Rebounds : "+str(final[0][12])+"\n"+"Total Rebounds : "+str(final[0][13])+"\n"+"Assists : "+str(final[0][14])+"\n"+"Steals : "+str(final[0][15])+"\n"+"Blocks : "+str(final[0][16])+"\n"+"Turnovers : "+str(final[0][17])+"\n"+"Personal Fouls : "+str(final[0][18])+"\n"+"Points : "+str(final[0][19])+"\n"+"*******************************************************"+"\n"+"Name : "+str(final[1][0])+"\n"+"Full Name : "+str(final[1][1])+"\n"+"-------------------------------------------------------------------------"+"\n"+"Birth Place : "+str(final[1][2])+"\n"+"Height : "+str(final[1][3])+"\n"+"Weight : "+str(final[1][4])+"\n"+"Retired : "+str(final[1][5])+"\n"+"Position : "+str(final[1][6])+"\n"+"Minutes Played : "+str(final[1][7])+"\n"+"Field Goals made : "+str(final[1][8])+"\n"+"3-Points Scored : "+str(final[1][9])+"\n"+"Free Throws : "+str(final[1][10])+"\n"+"Offensive Rebounds : "+str(final[1][11])+"\n"+"Defensive Rebounds : "+str(final[1][12])+"\n"+"Total Rebounds : "+str(final[1][13])+"\n"+"Assists : "+str(final[1][14])+"\n"+"Steals : "+str(final[1][15])+"\n"+"Blocks : "+str(final[1][16])+"\n"+"Turnovers : "+str(final[1][17])+"\n"+"Personal Fouls : "+str(final[1][18])+"\n"+"Points : "+str(final[1][19]))

def comp_coaches(x16,x17):
    n8=x16.get()
    n9=x17.get()
    sql="select c1.coach_name,c1.years_coaching,c1.retired,sum(c2.regular_season_games),sum(c2.regular_season_wins),sum(c2.regular_season_losses),TRUNCATE(((sum(c2.regular_season_wins)/sum(c2.regular_season_games))*100),2),sum(c2.playoff_games),sum(c2.playoff_wins),sum(c2.playoff_losses),TRUNCATE(((sum(c2.playoff_wins)/sum(c2.playoff_games))*100),2) from coaches_info c1,coaches_season_stats c2 where coach_name in (%s,%s) and c1.coach_id=c2.coach_id group by c1.coach_name"
    cr.execute(sql,(n8,n9))
    final=cr.fetchall()
    messagebox.showinfo("Coaches Head-to-Head","Name : "+str(final[0][0])+"\n"+"-------------------------------------------------------------------------"+"\n"+"Years Coaching : "+str(final[0][1])+"\n"+"Retired : "+str(final[0][2])+"\n"+"Regular Season Games : "+str(final[0][3])+"\n"+"Regular Season Wins : "+str(final[0][4])+"\n"+"Regular Season Losses : "+str(final[0][5])+"\n"+"Regular Season Win-Loss Percentage : "+str(final[0][6])+"\n"+"Playoff Games : "+str(final[0][7])+"\n"+"Playoff Wins : "+str(final[0][8])+"\n"+"Playoff Losses : "+str(final[0][9])+"\n"+"Playoff Win-Loss Percentage : "+str(final[0][10])+"\n"+"********************************************************"+"\n"+"Name : "+str(final[1][0])+"\n"+"-------------------------------------------------------------------------"+"\n"+"Years Coaching : "+str(final[1][1])+"\n"+"Retired : "+str(final[1][2])+"\n"+"Regular Season Games : "+str(final[1][3])+"\n"+"Regular Season Wins : "+str(final[1][4])+"\n"+"Regular Season Losses : "+str(final[1][5])+"\n"+"Regular Season Win-Loss Percentage : "+str(final[1][6])+"\n"+"Playoff Games : "+str(final[1][7])+"\n"+"Playoff Wins : "+str(final[1][8])+"\n"+"Playoff Losses : "+str(final[1][9])+"\n"+"Playoff Win-Loss Percentage : "+str(final[1][10]))

def Team(): 
    # Toplevel object which will  
    # be treated as a new window 
    teams = Toplevel(t) 
    # sets the title of the 
    # Toplevel widget 
    teams.title("Team") 
    # sets the geometry of toplevel 
    teams.geometry("600x600")
    teams.resizable(width=False, height=False)
    teams.configure(background="black")
    background_team_image = PhotoImage(file='D:\\Python tuts\\Tkinter Apps\\kobeBryant.png')
    bg_team = Label(teams, image=background_team_image, bd=0)    
    l0=Label(teams,font="calibri",padx=1,pady=1,text="Team")
    l0.place(x=100,y=20)
    l1=Label(teams,font="calibri",padx=1,pady=1,text="Enter Team Name : ")
    l1.place(x=50,y=75)
    e1=Entry(teams)
    e1.place(x=230,y=75)
    teams_button=Button(teams,font="calibri",padx=1,pady=1,text="Search Team",command=partial(sel_team_info,e1),width=12,height=2,relief="solid",background="White",foreground="Black",activebackground="Red")
    teams_button.place(x=200,y=110)
    l3=Label(teams,font="calibri",padx=1,pady=1,text="Head-to-Head")
    l3.place(x=100,y=250)
    l4=Label(teams,font="calibri",padx=1,pady=1,text="Enter Team 1 : ")
    l4.place(x=50,y=305)
    e4=Entry(teams)
    e4.place(x=230,y=305)
    l5=Label(teams,font="calibri",padx=1,pady=1,text="Enter Team 2 : ")
    l5.place(x=50,y=355)
    e5=Entry(teams)
    e5.place(x=230,y=355)
    teams_compare=Button(teams,font="calibri",padx=1,pady=1,text="Compare Teams",command=partial(comp_teams,e4,e5),width=14,height=2,relief="solid",background="White",foreground="Black",activebackground="Red")
    teams_compare.place(x=200,y=390)
    bg_team.pack()
    teams.mainloop()

def Player(): 
    # Toplevel object which will  
    # be treated as a new window 
    players = Toplevel(t) 
    # sets the title of the 
    # Toplevel widget 
    players.title("Player") 
    # sets the geometry of toplevel 
    players.geometry("600x600")
    players.resizable(width=False, height=False)
    players.configure(background="black")
    background_player_image = PhotoImage(file='D:\\Python tuts\\Tkinter Apps\\player.png')
    bg_player = Label(players, image=background_player_image, bd=0)
    l6=Label(players,font="calibri",padx=1,pady=1,text="Player")
    l6.place(x=180,y=20)
    l7=Label(players,font="calibri",padx=1,pady=1,text="Enter Player Name : ")
    l7.place(x=50,y=75)
    e7=Entry(players)
    e7.place(x=230,y=75)
    players_button=Button(players,font="calibri",padx=1,pady=1,text="Search Player",command=partial(sel_player_info,e7),width=12,height=2,relief="solid",background="Red",foreground="Black",activebackground="White")
    players_button.place(x=200,y=110)
    l9=Label(players,font="calibri",padx=1,pady=1,text="Head-to-Head")
    l9.place(x=180,y=250)
    l10=Label(players,font="calibri",padx=1,pady=1,text="Enter Player 1 : ")
    l10.place(x=50,y=305)
    e10=Entry(players)
    e10.place(x=230,y=305)
    l11=Label(players,font="calibri",padx=1,pady=1,text="Enter Player 2 : ")
    l11.place(x=50,y=355)
    e11=Entry(players)
    e11.place(x=230,y=355)
    players_compare=Button(players,font="calibri",padx=1,pady=1,text="Compare Players",command=partial(comp_players,e10,e11),width=14,height=2,relief="solid",background="Red",foreground="Black",activebackground="White")
    players_compare.place(x=200,y=390)
    bg_player.pack()
    players.mainloop()

def Coach(): 
    # Toplevel object which will  
    # be treated as a new window 
    coaches = Toplevel(t) 
    # sets the title of the 
    # Toplevel widget 
    coaches.title("Coach") 
    # sets the geometry of toplevel 
    coaches.geometry("650x600")
    coaches.resizable(width=False, height=False)
    coaches.configure(background="black")
    background_coach_image = PhotoImage(file='D:\\Python tuts\\Tkinter Apps\\coach.png')
    bg_coach = Label(coaches, image=background_coach_image, bd=0)
    l12=Label(coaches,font="calibri",padx=1,pady=1,text="Coach")
    l12.place(x=180,y=20)
    l13=Label(coaches,font="calibri",padx=1,pady=1,text="Enter Coach Name : ")
    l13.place(x=50,y=75)
    e13=Entry(coaches)
    e13.place(x=230,y=75)
    coaches_button=Button(coaches,font="calibri",padx=1,pady=1,text="Search Coach",command=partial(sel_coach_info,e13),width=12,height=2,relief="solid",background="White",foreground="Black",activebackground="Red")
    coaches_button.place(x=200,y=110)
    l15=Label(coaches,font="calibri",padx=1,pady=1,text="Head-to-Head")
    l15.place(x=180,y=250)
    l16=Label(coaches,font="calibri",padx=1,pady=1,text="Enter Coach 1 : ")
    l16.place(x=50,y=305)
    e16=Entry(coaches)
    e16.place(x=230,y=305)
    l17=Label(coaches,font="calibri",padx=1,pady=1,text="Enter Coach 2 : ")
    l17.place(x=50,y=355)
    e17=Entry(coaches)
    e17.place(x=230,y=355)
    coaches_compare=Button(coaches,font="calibri",padx=1,pady=1,text="Compare Coaches",command=partial(comp_coaches,e16,e17),width=15,height=2,relief="solid",background="White",foreground="Black",activebackground="Red")
    coaches_compare.place(x=200,y=390)
    bg_coach.pack()
    coaches.mainloop()

#specify Database connection credentials
serverName='localhost'
userName='root'
passw=''
dbName='nba'
db=pymysql.connect(serverName,userName,passw,dbName) #syntax for connecting
cr=db.cursor()
C = Canvas(t, height=550, width=680)
t.resizable(width=False, height=False)
t.title("NBA Stats App")
background_image=PhotoImage(file='D:\\Python tuts\\Tkinter Apps\\SEO-image-NBA-logoman2.png')
background_label = Label(t, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
l=Label(t,font="calibri",padx=1,pady=1,text="Michael 'Air' Jordan or Lebron 'King' James? \n LA Lakers or Boston Celtics? \n Phil Jackson or Gregg Popovich? \n For stats nerds that need to put an end to \n this argument, this App aims to do just that. \n This App gives you the stats of over \n 30 NBA teams, 4000+ players and 300+ coaches \n and allows you to do a Head-to-Head comparison.")
l.place(x=250,y=50)
b1=Button(t,font="calibri",padx=1,pady=1,text="Team",command=Team,width=15,height=3,relief="solid",background="White",foreground="Black",activebackground="Red")
b1.place(x=370,y=250)
b2=Button(t,font="calibri",padx=1,pady=1,text="Player",command=Player,width=15,height=3,relief="solid",background="White",foreground="Black",activebackground="Red")
b2.place(x=370,y=350)
b3=Button(t,font="calibri",padx=1,pady=1,text="Coach",command=Coach,width=15,height=3,relief="solid",background="White",foreground="Black",activebackground="Red")
b3.place(x=370,y=450)
C.pack()
t.mainloop()
db.close()

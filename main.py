import turtle,pandas,os
os.system("clear")
screen=turtle.Screen()
screen.bgpic("map.gif")
screen.setup(width=960,height=490)
screen.title("Map Game")
data=pandas.read_csv("coordinates.csv")
countries=data.country.to_list()
print(countries)
guessed=[]
while len(guessed) < len(countries):
    answer=screen.textinput(title=f"Guess the country {len(guessed)} from {len(countries)}",prompt="Type the country name and hit enter !").title()
    
    if answer in countries:
        guessed.append(answer)
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        country_x=data[data.country==answer]["x"].item()
        country_y=data[data.country==answer]["y"].item()
        t.goto(country_x,country_y)
        t.fillcolor("red")
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.write(answer,font=("arial",15))
    elif answer=="Exit":     
        non_guessed=[]
        for i in countries:  
            if i not in guessed:
                non_guessed.append(i) 
        final_csv=pandas.DataFrame(non_guessed).to_csv("wrong_countries.csv")
        break

screen.exitonclick()
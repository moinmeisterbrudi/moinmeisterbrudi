from turtle import * 

def schneeflocke(stufe,länge):
    if stufe == 1:  
        forward(länge)
    else:
        schneeflocke(stufe - 1, länge / 3)
        left(60)
        schneeflocke(stufe - 1, länge / 3)
        right(120)
        schneeflocke(stufe - 1, länge / 3)
        left(60)
        schneeflocke(stufe - 1, länge / 3)
speed(0)   
color("Grün", "lightgreen")   
begin_fill() 
schneeflocke(5, 400)
right(120)
schneeflocke(5, 400)
right(120)
schneeflocke(5, 400)
end_fill()

done()
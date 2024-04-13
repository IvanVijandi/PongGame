import turtle
import tkinter as tk









##JUEGO PING PONG

def start_ping_pong():
    
    ventana.destroy()
    
    ##Funciones paddleUno

    def subir_Rojo():
        if rojo.ycor() < 275.5:
            rojo.sety(rojo.ycor()+10)
        
    def bajar_Rojo():
        if rojo.ycor() > -275.5:
            rojo.sety(rojo.ycor()-10)
        
    ##Funciones paddleDos

    def subir_Verde():
        if verde.ycor() < 275.5:
            verde.sety(verde.ycor()+10)
        
    def bajar_Verde():
        if verde.ycor() > -275.5:
            verde.sety(verde.ycor()-10)
    
  
    ##Pantalla

    pantalla = turtle.Screen()
    pantalla.setup(600,600)
    pantalla.bgcolor("black")
    pantalla.title("PONG")
    pantalla.listen()
    pantalla.tracer(0)
    pantalla.onkeypress(subir_Rojo, "w")
    pantalla.onkeypress(bajar_Rojo, "s")
    
    
    ##Pelota

    pelota = turtle.Turtle("circle")
    pelota.color("white")
    pelota.goto(0,0)
    pelota.penup()

    ##Texto
    texto = turtle.Turtle()
    texto.hideturtle()  
    texto.penup()       
    texto.goto(0, 0)
    


    
    ##Paddle Verde 
    verde= turtle.Turtle("square")
    verde.penup()
    verde.color("green")
    verde.shapesize(4.5,1)
    verde.goto(285,0)
    
    ##Paddle Rojo ---> lo seteamos para ping pong
    rojo = turtle.Turtle("square")
    rojo.penup()
    rojo.color("red")
    rojo.shapesize(4.5,1)
    rojo.goto(-291,0)

    ##Seteamos Velocidad
    velocidadX = 0.1
    velocidadY = 0.1
    
    
    while True:
        
        
        
        
        pelota.setx(pelota.xcor()+velocidadX)
        pelota.sety(pelota.ycor()+velocidadY)
        
        pantalla.update()
        
        
    
        
        if pelota.distance(rojo) < 37 or pelota.distance(verde) < 37:
            
            if pelota.ycor() > rojo.ycor() or pelota.ycor() > verde.ycor():
                
                velocidadX*=-1
                velocidadY=0.1
                velocidadY+=0.0001
                
                if velocidadX < 0:
                    velocidadX-=0.0001
                else:
                    velocidadX+=0.0001
                
                    
                        
            elif pelota.ycor() < rojo.ycor() or pelota.ycor() < verde.ycor():
                
                velocidadX*=-1
                velocidadY=-0.1
                velocidadY-=0.0001 
                
                if velocidadX < 0:
                    velocidadX-=0.0001
                else:
                    velocidadX+=0.0001
                
                
            elif pelota.ycor() == verde.ycor() or pelota.ycor() == rojo.ycor():
                
                velocidadX*=-1
                velocidadY=0.1
                velocidadY+=0.0001
                
                if velocidadX < 0:
                    velocidadX-=0.0001
                else:
                    velocidadX+=0.0001
                
                
        
        if pelota.ycor() > 300 or pelota.ycor() < -300:
            velocidadY*=-1
            velocidadX*=1
        
        if pelota.xcor() > 300:
            pantalla.clear()
            pantalla.bgcolor("black")
            texto.color("red")  
            texto.write("RED WIN", align="center", font=("Arial", 30, "normal"))
            break
            
        if pelota.xcor() < -300 :
            pantalla.clear()
            pantalla.bgcolor("black")
            texto.color("green")  
            texto.write("RED WIN", align="center", font=("Arial", 30, "normal"))
            break
        
        verde.sety(pelota.ycor())
        
    
        
##JUEGO PONG

def start_game_pong():
    
    ventana.destroy()
    
    ##Funnciones
    
    def derecha():
        if paddle.xcor() < 290: 
            paddle.setx((paddle.xcor())+10)
            

    def izquierda():
        if paddle.xcor() > -290:  
            paddle.setx((paddle.xcor())-10)

    ##pantalla
    pantalla = turtle.Screen()
    pantalla.title("PONG")
    pantalla.setup(600,600)
    pantalla.bgcolor("black")
    pantalla.listen()
    pantalla.tracer(0)



    ##Paddle

    paddle = turtle.Turtle("square")
    paddle.goto(0,-280)
    paddle.color("white")
    paddle.shapesize(1,5)
    paddle.penup()

    ##Pelota

    pelota = turtle.Turtle("circle")
    pelota.goto(0,0)
    pelota.color("white")
    pelota.penup()
    pantalla.onkeypress(derecha,"Right")
    pantalla.onkeypress(izquierda,"Left")


    velocidadX = 0.15
    velocidadY = 0.1
        
    while True:
        


        pelota.setx(pelota.xcor()+velocidadX)
        pelota.sety(pelota.ycor()+velocidadY)
        pantalla.update()
        
        ##Colision con paddle
        
        if pelota.distance(paddle) < 40:
            
            velocidadY*=-1
            
            if velocidadX == -1 or velocidadY == -1:
                velocidadX-=0.05
                velocidadY -= 0.05
            elif  velocidadX == 1:
                velocidadX+=0.05
                velocidadY+=0.05
            
            
            
            
            if pelota.xcor() < paddle.xcor():
                if velocidadX == -1 :
                    velocidadX *=-1
                else:
                    velocidadX*=1
            else:
                if velocidadX == -1:
                    velocidadX *=1
                else:
                    velocidadX *=-1
            
            
            
            
            
            
        ##Colision con paredes
        
        if pelota.xcor() > 299:
            velocidadX*=-1
            #velocidadX+=0.05
        elif pelota.xcor() < -299:
            velocidadX*=-1
            #velocidadX+=0.05
        elif pelota.ycor() > 299:
            velocidadY*=-1
        elif pelota.ycor() < -299:
            break
        
    

    
    
    

        



##Ventana
ventana = tk.Tk()
ventana.title("Juego")
##boton pingpong
boton_play_pingpong = tk.Button(ventana, text="Play PingPong", command=start_ping_pong)
boton_play_pingpong.pack(pady=40)
##boton pong
boton_play_pong = tk.Button(ventana, text="Play Pong", command=start_game_pong)
boton_play_pong.pack(pady=40)









ventana.mainloop()
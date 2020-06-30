# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals 
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
LEFT = False
RIGHT = True
point_one = [8,200]
point_two =[8,300]
point_three=[592,200]
point_four=[592,300]
player1 = 0
player2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH/2,HEIGHT/2]
#ball_vel = [-240/60,190.0/60.0]
ball_vel =[0,0]
paddle_growth =[0,0]
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if(direction == RIGHT):
        random_x = -random.randrange(120,240)
        ball_vel[0] = random_x/60
        random_y = random.randrange(60,180)
        ball_vel[1] = random_y/60
    elif(direction == LEFT):
        random_x = - random.randrange(120,240)
        ball_vel[0] = random_x/60
        random_y = - random.randrange(60,180)
        ball_vel[1] = random_y/60
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global player1, player2  
    spawn_ball(LEFT)

def draw(canvas):
    global player1, player2 , paddle1_pos, paddle2_pos, ball_pos, ball_vel
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    
    
    if(ball_pos[0]<=(PAD_WIDTH+BALL_RADIUS) ):
        spawn_ball(LEFT)
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]
    elif(ball_pos[1]<=BALL_RADIUS ):
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]
        spawn_ball(RIGHT)

    elif(ball_pos[0]>=(WIDTH-(PAD_WIDTH+BALL_RADIUS)) ):
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]
        spawn_ball(LEFT)
    elif((ball_pos[1]>=(HEIGHT-BALL_RADIUS))):
        spawn_ball(RIGHT)
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]

    

        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_circle(ball_pos,BALL_RADIUS,2,"Red","Yellow")  
    canvas.draw_line(point_one,point_two, 5, 'Red')
    canvas.draw_line(point_three,point_four, 5, 'Red')
    canvas.draw_text(str(player1),(100,50),25,'White')
    canvas.draw_text(str(player2),(500,50),25,'White')
    
    
#draw scores   
    if(point_one[1]<=ball_pos[1] and ball_pos[1]<=point_two[1] and ball_pos[0]<=(PAD_WIDTH+BALL_RADIUS)):
        print "*****HIT*****"
    elif(ball_pos[0]<=(PAD_WIDTH+BALL_RADIUS)):
        player2=player2+1
        print "Player2 got point "+ str(player2)
    elif(point_three[1]<=ball_pos[1] and ball_pos[1]<=point_four[1] and ball_pos[0]>=(WIDTH-(PAD_WIDTH+BALL_RADIUS))):    
        print "*****HIT*****"
    elif(ball_pos[0]>=(WIDTH-(PAD_WIDTH+BALL_RADIUS))):        
        player1=player1+1
        print "Player1 got point "+str(player1)

#keyup and keydown        
def keyup(key):
    global point_one,point_two, point_three,point_four

    if (key == simplegui.KEY_MAP['up'] and point_one[1]>0 ):
        point_one[0]+=0 
        point_one[1]-=20
        point_two[0]+=0
        point_two[1]-=20
    elif (key ==simplegui.KEY_MAP['w'] and point_three[1]>0):
        point_three[0]+=0 
        point_three[1]-=20
        point_four[0]+=0
        point_four[1]-=20

def keydown(key):
     global point_two,point_one,point_three,point_four
     if (key == simplegui.KEY_MAP['down'] and point_two[1]<HEIGHT and point_one[1]<300) :
         point_one[0]+=0 
         point_one[1]+=10
         point_two[0]+=0
         point_two[1]+=10
     elif (key == simplegui.KEY_MAP['s'] and point_four[1]<HEIGHT and point_three[1]<300):
         point_three[0]+=0 
         point_three[1]+=10
         point_four[0]+=0
         point_four[1]+=10
    
def reset_count():
    global player1 ,player2
    player1 = 0
    player2 = 0
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background('Pink')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset',reset_count)


# start frame
#new_game()
frame.start()

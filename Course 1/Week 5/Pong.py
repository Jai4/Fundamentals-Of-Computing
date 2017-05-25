# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 500
HEIGHT = 300
BALL_RADIUS = 15
PAD_WIDTH = 7
PAD_HEIGHT = 70
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
L = False
R = True

# initialize ball_pos and ball_vel for new bal in middle of table
ball_position = [WIDTH / 2, HEIGHT / 2];
ball_velocity = [0, 1];

paddle1_velocity = 0;
paddle2_velocity = 0;
paddle1_position = HEIGHT / 2.5;
paddle2_position = HEIGHT / 2.5;
padd_velocity = 6;
s1 = 0;
s2 = 0;


# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_position, ball_velocity
    ball_position = [WIDTH / 2, HEIGHT / 2];
    ball_velocity[0] = -random.randrange(120, 240) / 100;
    if (direction == True):
        ball_velocity[0] *= -1;
    ball_velocity[1] = -random.randrange(60, 180) / 100;


# define event handlers
def new_game():
    global paddle1_position, paddle2_position, paddle1_velocity, paddle2_velocity, s1, s2;

    s2 = 0;
    s1 = 0;
    spawn_ball(0);
    paddle1_pos = HEIGHT / 2.5;
    paddle2_pos = HEIGHT / 2.5;


def draw(canvas):
    global s1, s2, paddle1_position, paddle2_position, ball_position, ball_velocity
    global paddle1_velocity, paddle2_velocity, BALL_RADIUS;

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "Red")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "Red")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "Red")

    # update ball
    ball_position[0] = ball_position[0] + ball_velocity[0];
    ball_position[1] = ball_position[1] + ball_velocity[1];
    if ((ball_position[0] <= (BALL_RADIUS + PAD_WIDTH)) or (ball_position[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS))):
        ball_velocity[0] = ball_velocity[0] * -1;
        if (ball_position[0] < (WIDTH / 2)):
            if ((ball_position[1] < paddle1_position) or (ball_position[1] > paddle1_position + PAD_HEIGHT)):
                s2 = s2 + 1;
                spawn_ball(R);
            else:
                ball_velocity[0] = ball_velocity[0] + (.1 * ball_velocity[0]);
        if (ball_position[0] > (WIDTH / 2)):
            if ((ball_position[1] < paddle2_position) or (ball_position[1] > paddle2_position + PAD_HEIGHT)):
                s1 = s1 + 1;
                spawn_ball(L);
            else:
                ball_velocity[0] = ball_velocity[0] + (.1 * ball_velocity[0]);
    if ((ball_position[1] <= BALL_RADIUS) or (ball_position[1] >= (HEIGHT - BALL_RADIUS))):
        ball_velocity[1] = ball_velocity[1] * -1;

    # draw ball
    canvas.draw_circle(ball_position, BALL_RADIUS, 2, "Green", "white");

    # update paddle's vertical position, keep paddle on the screen
    if ((paddle2_position <= HEIGHT - PAD_HEIGHT and paddle2_velocity > 0) or (
            paddle2_position >= 0 and paddle2_velocity < 0)):
        paddle2_position = paddle2_position + paddle2_velocity;
    elif ((paddle1_position <= HEIGHT - PAD_HEIGHT and paddle1_velocity > 0) or (
            paddle1_position >= 0 and paddle1_velocity < 0)):
        paddle1_position = paddle1_position + paddle1_velocity;
        # draw paddles
    canvas.draw_polygon(
        [[0, paddle1_position], [PAD_WIDTH, paddle1_position], [PAD_WIDTH, (paddle1_position) + PAD_HEIGHT],
         [0, (paddle1_position) + PAD_HEIGHT]], 1, "blue", "white")
    canvas.draw_polygon(
        [[WIDTH, paddle2_position], [WIDTH - PAD_WIDTH, paddle2_position],
         [WIDTH - PAD_WIDTH, paddle2_position + PAD_HEIGHT],
         [WIDTH, paddle2_position + PAD_HEIGHT]], 1, "blue", "white")
    # draw scores
    canvas.draw_text(str(s1), [200, 90], 55, "yellow")
    canvas.draw_text(str(s2), [310, 90], 55, "yellow")


def keydown(key):
    global paddle1_velocity, paddle2_velocity, padd_velocity
    if (key == simplegui.KEY_MAP["w"]):
        paddle1_velocity = -padd_velocity
    elif (key == simplegui.KEY_MAP["s"]):
        paddle1_velocity = padd_velocity
    if (key == simplegui.KEY_MAP["up"]):
        paddle2_velocity = -padd_velocity
    elif (key == simplegui.KEY_MAP["down"]):
        paddle2_velocity = padd_velocity


def keyup(key):
    global paddle1_velocity, paddle2_velocity
    if (key == simplegui.KEY_MAP["w"]):
        paddle1_velocity = 0
    elif (key == simplegui.KEY_MAP["s"]):
        paddle1_velocity = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_velocity = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_velocity = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("RESTART", new_game, 170)

# start frame
new_game()
frame.start()



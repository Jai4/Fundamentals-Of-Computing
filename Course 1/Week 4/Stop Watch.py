# template for "Stopwatch: The Game"
import math
import simplegui


# define global variables
scount = 0;
tcount = 0;
ct = 0;
T = True;
F = True;


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = str(t // 600);
    tem = (t // 10);
    tem = (tem) % 60;
    B = str(tem // 10);
    C = str(tem % 10);
    D = str(t % 10);
    return A + ":" + B + C + "." + D;


# define event handlers for buttons; "Start", "Stop", "Reset"
def stop():
    global scount, tcount, T;
    timer.stop();
    if (T == True):
        if (F == False):
            tcount = tcount + 1;
        T = False;
        if ((ct % 10 == 0) and (ct != 0)):
            scount = scount + 1;


def start():
    global T, F;
    T = True;
    F = False;
    timer.start();


def reset():
    global scount, tcount, ct, F;
    ct = 0;
    scount = 0;
    tcount = 0;
    F = True;


# define event handler for timer with 0.1 sec interval
def tick():
    global ct;
    ct = ct + 1;


# define draw handler
def draw(canvas):
    global ct;
    canvas.draw_text(format(ct), [300, 300], 45, "Blue");
    canvas.draw_text(str(scount) + "/" + str(tcount), [450, 250], 40, "Red");


# create frame
frame = simplegui.create_frame("Stopwatch", 600, 600);
frame.add_button("START", start);
frame.add_button("STOP", stop);
frame.add_button("RESET", reset);

# register event handlers
frame.set_draw_handler(draw);
timer = simplegui.create_timer(100, tick)

# start frame
frame.start();

# Please remember to review the grading rubric

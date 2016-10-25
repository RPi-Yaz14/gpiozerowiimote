# Wiimote GPIOZero code by Yasmin Bey
from gpiozero import RyanteckRobot
import cwiid, time
robot = RyanteckRobot()

button_delay = 0.01

print("Hold down buttons 1 and 2 to start the connection process!")
time.sleep(1)

try:
    wiimote = cwiid.Wiimote()
except RuntimeError:
    print("Failed connection. Please re-run the program!")
    quit()

print("Connection successful. Buttons will be active after 2 seconds")
wiimote.rumble = 1 # This can be removed if you don't want the remote to rumble when connected!
time.sleep(2)
wiimote.rumble = 0

wiimote.rpt_mode = cwiid.RPT_BTN

while True:
    buttons = wiimote.state["buttons"]
    speed = 0.7 # This can be altered between 0 and 1, dependent on requirements.
    if (buttons & cwiid.BTN_LEFT):
        robot.left(speed)

    if (buttons & cwiid.BTN_RIGHT):
         robot.right(speed)

    if (buttons & cwiid.BTN_UP):
         robot.forward(speed)

    if (buttons & cwiid.BTN_DOWN):
         robot.backward(speed)


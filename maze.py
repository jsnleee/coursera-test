import event, time, cyberpi, mbot2, mbuild

import time

# initialize variables

base_power = 0

kp = 0

left_power = 0

right_power = 0

 

#stop

@event.is_press('a')

def is_btn_press():

    global base_power, kp, left_power, right_power

    cyberpi.stop_other()

    mbot2.drive_power(0, 0)

 

#start

@event.is_press('b')

def is_btn_press1():

    global base_power, kp, left_power, right_power

    cyberpi.stop_other()

    base_power = 30

    kp = 0.3

    coolDown = 0

    start = 0

    timed = False

    while True:

        left_power = (base_power - kp * mbuild.quad_rgb_sensor.get_offset_track(1))

        right_power = -1 * ((base_power + kp * mbuild.quad_rgb_sensor.get_offset_track(1)))

        mbot2.drive_power(left_power, right_power)

        if mbuild.ultrasonic2.get(1) < 8 and coolDown == 0:

            timed = True

            coolDown = 1

            start = time.time()

            cyberpi.console.println("wall")

            cyberpi.mbot2.turn(-92)

            if mbuild.ultrasonic2.get(1) < 8 or mbuild.ultrasonic2.get(1) == 300:

                cyberpi.console.println("wall wall")

                cyberpi.mbot2.turn(180)

                continue

        if mbuild.quad_rgb_sensor.get_line_sta() == 0 and coolDown == 0:

            timed = True

            start = time.time()

            coolDown = 1

            cyberpi.console.println("color")

            cyberpi.mbot2.turn(-92)

            if mbuild.ultrasonic2.get(1) < 8 or mbuild.ultrasonic2.get(1) == 300:

                cyberpi.console.println("color wall")

                cyberpi.mbot2.turn(92)

            cyberpi.mbot2.forward(200)

            time.sleep(0.2)

 

        if time.time() - start >= 2 and timed == True:

            coolDown = 0

            timed = False

## Lab Exercise 10/26/2022
## projectileTest.py
## author: nmessa
## Test file for the Projectile class
## Demostrate plot using Pylab


from projectile import Projectile
import pylab

def getInputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (in meters/sec): "))
    h = float(input("Enter the initial height (in meters): "))
    dt = float(input("Enter the time interval between position calculations: "))
    return a, v, h, dt

def main():
    time = 0.0
    #Create two lists for holding x and y values
    x_list = []
    y_list = []
    t_list = []
    v_list = []
    angle, velocity, h0, deltaT = getInputs()      #get inputs from user
    cBall = Projectile(angle, velocity, h0)         #construct Projectile

    #prepare for first position calculation
    time += deltaT                                              
    cBall.update(time)
    
    #simulation loop
    while cBall.getY() > 0:
        x_list.append(cBall.getX()) #capture x-coordinate
        y_list.append(cBall.getY()) #capture y-coordinate
        t_list.append(time)
        v_list.append(cBall.getY()/time)
        cBall.update(time)
        print ("Distance traveled: ", round(cBall.getX(), 3),
               "meters at Time =", round(time, 2), "seconds")
        print ("Altitude: ", round(cBall.getY(), 3), "meters")
        print()
        time += deltaT
    print("Maximum altitude =", round(max(y_list),2), "meters")
    print("Distance projectile traveled down range =",
          round(max(x_list),2), "meters")
    pylab.plot(x_list, y_list, 'r')
    pylab.xlabel("Distance down range (meters)")
    pylab.ylabel("Altitude (meters)")
    pylab.grid(True)
    pylab.show()

    pylab.plot(t_list, y_list, 'r')
    pylab.ylabel("Altitude (meters)")
    pylab.xlabel("Time (seconds)")
    pylab.grid(True)
    pylab.show()

    pylab.plot(t_list, v_list, 'r')
    pylab.ylabel("Velocity (meters/second)")
    pylab.xlabel("Time (seconds)")
    pylab.grid(True)
    pylab.show()
main()

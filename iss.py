#!/usr/bin/env python

__author__ = "Matthew Perry collaborating with Zachary Kline and Dennis Christenson"


import requests
import json
import time
import turtle


def get_all_astronauts():
    '''returns a comma delmitted '''
    members = requests.get("http://api.open-notify.org/astros.json")
    text_members = members.text
    as_dict = json.loads(text_members)
    astros = []
    for astro_the_dog in as_dict['people']:
        astros.append(astro_the_dog['name'])
    return astros


def location_of_iss(n):
    loc = requests.get("http://api.open-notify.org/iss-now.json")
    loc_dict = json.loads(loc.text)
    current_loc = loc_dict["iss_position"]
    stampy = time.ctime(loc_dict["timestamp"])
    people_str = ", ".join(n)[:-2]
    print ("At this time ({}), the astronauts {} are at:\nlongitude: {} \nlatitude: {}".format(stampy, people_str, current_loc["longitude"], current_loc["latitude"]))
    return(float(current_loc["longitude"]), float(current_loc["latitude"]))


# provided by Zach Kline
def turtley_enough(iss_position, next_pass):
    new_screen = turtle.Screen()
    new_screen.bgpic('./map.gif')
    new_screen.addshape('iss.gif')
    new_screen.setup(width=720, height=360)
    new_screen.setworldcoordinates(-180, -90, 180, 90)
    new_var = turtle.Turtle()
    new_var.shape('iss.gif')
    new_var.penup()
    new_var.goto(iss_position)
    indy_dot = turtle.Turtle()
    indy_dot.shape('circle')
    indy_dot.color('yellow')
    indy_dot.penup()
    indy_dot.goto(-86.1349, 40)
    msg = turtle.Turtle()
    msg.color('white')
    msg.write(next_pass, True, align='center')
    new_screen.exitonclick()


def over_indy():
    r = requests.get("http://api.open-notify.org/iss-pass.json?lat=40&lon=-86.1349")
    dictionary = r.text
    dictionary = json.loads(dictionary)
    next_pass = dictionary["response"][0]
    return("The next pass over Indianapolis is {}".format(time.ctime(next_pass["risetime"])))


pos = location_of_iss(get_all_astronauts())
turtley_enough(pos, over_indy())


def main():
    pass


if __name__ == '__main__':
    main()

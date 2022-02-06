from mongoengine import *


def global_init():
    connect('home_net')

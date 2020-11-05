# MonsterBorg code V1- Val Coppo

# Setup

import ThunderBorg
TB = ThunderBorg.ThunderBorg()
TB.Init()

from pyPS4Controller.controller import Controller


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    def on_square-press(self):
        SetMotors(0.75)


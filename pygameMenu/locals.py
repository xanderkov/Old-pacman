class PymenuAction(object):

    def __init__(self, action):
        assert isinstance(action, int)
        self._action = action

    def __eq__(self, other):
        if isinstance(other, PymenuAction):
            return self._action == other._action
        return False



PYGAME_MENU_BACK = PymenuAction(0)
PYGAME_MENU_CLOSE = PymenuAction(1)
PYGAME_MENU_DISABLE_CLOSE = PymenuAction(10)
PYGAME_MENU_EXIT = PymenuAction(3)
PYGAME_MENU_RESET = PymenuAction(4)


PYGAMEMENU_PYMENUACTION = "<class 'pygameMenu.locals._PymenuAction'>"
PYGAMEMENU_TEXT_NEWLINE = ''
PYGAMEMENU_TYPE_SELECTOR = PymenuAction(2)


JOY_AXIS_X = 0
JOY_AXIS_Y = 1
JOY_BUTTON_BACK = 1
JOY_BUTTON_SELECT = 0
JOY_CENTERED = (0, 0)
JOY_DEADZONE = 0.5
JOY_DOWN = (0, -1)
JOY_LEFT = (-1, 0)
JOY_RIGHT = (1, 0)
JOY_UP = (0, 1)

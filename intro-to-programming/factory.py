from __future__ import print_function
from abc import ABCMeta, abstractmethod


class Button:
    __metaclass__ = ABCMeta

    @abstractmethod
    def paint(self):
        pass


class LinuxButton(Button):
    def paint(self):
        return "Render a button in linux style"


class WindowsButton(Button):
    def paint(self):
        return "Render a button in windows style"


class MacOSButton(Button):
    def paint(self):
        return "Render a button in MacOS Style"


class GUIFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_button(self):
        pass


class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()


class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()


class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSFactory()


appearance = "linux"

if appearance == "linux":
    factory = LinuxFactory()
elif appearance == "osx":
    factory = MacOSFactory()
elif appearance == "win":
    factory = WindowsFactory()
else:
    raise NotImplementedError("Not Implemented for your platform: {}".
                              format(appearance))

if factory:
    button = factory.create_button()
    result = button.paint()
    print(result)

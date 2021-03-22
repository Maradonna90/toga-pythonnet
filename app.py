import clr
SWF = clr.AddReference("System.Windows.Forms")
import System.Windows.Forms as WinForms

print(SWF.Location)


class HelloApp(WinForms.Form):
    """A simple hello world app that demonstrates the essentials of
       winforms programming and event-based programming in Python."""

    def __init__(self):
        pass

    def run(self):
        WinForms.Application.Run(self)


def main():
    form = HelloApp()
    print("form created")
    app = WinForms.Application
    print("app referenced")
    app.Run(form)


if __name__ == '__main__':
    main()

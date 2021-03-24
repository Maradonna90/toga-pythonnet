import toga_proactor as tpa
import asyncio
import clr
clr.AddReference("System.Windows.Forms")
import System.Windows.Forms as WinForms
from System import Threading


class App:
    def __init__(self):
        print("INIT")
        thread = Threading.Thread(Threading.ThreadStart(self.run_app))
        thread.SetApartmentState(Threading.ApartmentState.STA)
        thread.Start()
        thread.Join()

    def run_app(self):
        loop = tpa.WinformsProactorEventLoop()
        app_context = WinForms.ApplicationContext()
        asyncio.set_event_loop(loop)
        # print("Start Forever Loop")
        # loop.run_forever(app_context)

import toga_proactor as tpa
import asyncio
import clr
clr.AddReference("System.Windows.Forms")
import System.Windows.Forms as WinForms
from System import Threading


class App:
    def __init__(self):
        print("INIT")

    def create(self):
        print("CREATE")
        thread = Threading.Thread(Threading.ThreadStart(self.run_app))
        thread.SetApartmentState(Threading.ApartmentState.STA)
        thread.Start()
        thread.Join()

    def run_app(self):
        print("RUN")
        self.native = WinForms.Application
        self.loop = tpa.WinformsProactorEventLoop()
        self.app_context = WinForms.ApplicationContext()
        asyncio.set_event_loop(self.loop)
        print("Start Forever Loop")
        self.loop.run_forever(self.app_context)

    def exit(self):
        self.native.Exit()

import toga_proactor as tpa
import asyncio
import clr
clr.AddReference("System.Windows.Forms")
import System.Windows.Forms as WinForms
from System import Threading

# TODO: Figure out the function call tree for an WindowsApp and recreate.
# 1. App.__init__
# 2. self._create_impl()
# 3. factory.App(interface=self)
# 4. (Winforms).App.__init__()
# 5. 
# TODO: fix the main loop getting stuck


class App:
    def __init__(self):
        print("INIT")

    def create(self):
        print("CREATE")
        self.loop = tpa.WinformsProactorEventLoop()
        asyncio.set_event_loop(self.loop)
        thread = Threading.Thread(Threading.ThreadStart(self.run_app))
        thread.SetApartmentState(Threading.ApartmentState.STA)
        thread.Start()
        thread.Join()

    def run_app(self):
        print("RUN")
        self.native = WinForms.Application
        self.app_context = WinForms.ApplicationContext()
        print("Start Forever Loop")
        # self.loop.run_forever(self.app_context)

    def exit(self):
        self.native.Exit()

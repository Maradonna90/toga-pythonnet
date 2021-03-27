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
        print("THREAD STARTED!")
        thread.Join()
        print("THREAD JOINED!")

    def run_app(self):
        print("RUN")
        self.native = WinForms.Application
        self.app_context = WinForms.ApplicationContext()
        self.native.ApplicationExit += self.winforms_application_exit
        print("Start Forever Loop")
        self.loop.call_soon_threadsafe(self.do_generator)
        self.exit()
        self.loop.run_forever(self.app_context)

    def do_generator(self):
        "A generator-based handler"
        # The generator yields a number; that number is the number of seconds
        # to yield to the main event loop before processing is resumed.
        for i in range(1, 10):
            print("Iteration {}".format(i))
            yield 1

    def exit(self):
        print("EXIT!")
        self.loop.call_later(5, self.loop.stop())

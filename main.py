import toga_proactor as tpa
import asyncio
import clr
clr.AddReference("System.Windows.Forms")
import System.Windows.Forms as WinForms


def main():
    print("Start Main!")
    loop = tpa.WinformsProactorEventLoop()
    app_context = WinForms.ApplicationContext()
    asyncio.set_event_loop(loop)
    # print("Start Forever Loop")
    # loop.run_forever(app_context)


if __name__ == '__main__':
    main()

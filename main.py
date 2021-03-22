import toga_proactor as tpa
import app


def main():
    print("Start Main!")
    appl = app.HelloApp()
    tpa.WinformsProactorEventLoop().run_forever(appl)

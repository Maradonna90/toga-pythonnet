import toga_proactor as tpa
import app


def main():
    appl = app.HelloApp
    tpa.WinformsProactorEventLoop().run_forever(appl)

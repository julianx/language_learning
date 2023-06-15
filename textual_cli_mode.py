from textual.app import App, ComposeResult
from textual.widgets import Input
from textual.widgets import TextLog
from textual import events


class InputApp(App):
    def compose(self) -> ComposeResult:
        # yield Input(placeholder="First Name")
        # yield Input(placeholder="Last Name")
        yield TextLog()

    def on_key(self, event: events.Key) -> None:
        self.query_one(TextLog).write(event)


if __name__ == "__main__":
    app = InputApp()
    app.run()

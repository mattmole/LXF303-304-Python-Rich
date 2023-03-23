# Using the logging helper function to colour code log messages, according to the severity
from rich.table import Table
from rich.live import Live
import time
import random
from rich.layout import Layout
from rich.markdown import Markdown
from rich.panel import Panel
from rich.console import Console
from rich import print
import logging
from rich.logging import RichHandler
import os

consoleWidth = 120

# FORMAT = "%(message)s"
# logging.basicConfig(
#    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
# )

# log = logging.getLogger("rich")
# log.debug("Hello, World!")
# log.info("Hello, World!")
# log.warning("Hello, World!")
# log.error("Hello, World!")

# Using the justify functionality to change how text is rendered
console = Console(width=consoleWidth)
style = "italic white on blue"
console.print("Title of the script", style=style, justify="center")
console.print("")
console.print("Line one of output")
console.print("Line two of script "*10)

print()
print()

# Using the panel functionality to border some text
print(Panel("Hello, [red]World!", width=consoleWidth))

print()

textToDraw = "[yellow]Line one of the script[/yellow]" + os.linesep
textToDraw += "[green]Line two of the script [/green]"*10+os.linesep
textToDraw = textToDraw[0:-1]
textToDraw += "Visit my [red][link=https://www.linuxformat.co.uk]blog[/link]!"


panel = Panel(textToDraw, width=consoleWidth)
panel.title = "Title"
panel.title_align = "left"
panel.subtitle = "Subtitle"
panel.subtitle_align = "right"
# print(panel)

print()
print()

# Rendering markdown

markdownContent = open("markdownForTutorial.md").read()
# console = Console(width=consoleWidth)
md = Markdown(markdownContent)
# console.print(md)


# Using the layout functionality
console = Console(width=consoleWidth)
layout = Layout()
layout.minimum_size = 28
topRow = Layout(md, name="upper")
topRow.size = 20
bottomRow = Layout(name="lower")
bottomRow.size = 8
bottomLeft = Layout(panel, name="left")
bottomRight = Layout(panel, name="right")
layout.split_column(
    topRow,
    bottomRow
)
layout["lower"].split_row(
    bottomLeft,
    bottomRight,
)
console.print(layout)


# Using the live functionality to build an application that updates
def generate_table():
    """Make a new table."""
    table = Table()
    table.add_column("ID")
    table.add_column("Value")
    table.add_column("Status")

    for row in range(random.randint(2, 6)):
        value = random.random() * 100
        table.add_row(
            f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
        )
    return table


with Live(generate_table(), refresh_per_second=4) as live:
    for _ in range(40):
        time.sleep(0.4)
        live.update(generate_table())

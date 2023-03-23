from rich.table import Table
import time
from rich.progress import track
from time import sleep
from rich.console import Console
from rich.prompt import Prompt
from rich import print

# Print coloured text and include emojis
print("[red underline]:thumbs_up: hello world")


# Request feedback from the user and only allow certain options
options = ["1", "2", "3", "4", "5"]
promptResponse = None
while promptResponse == None:
    promptResponse = Prompt.ask(
        "Enter your favourite number between 1 and 5", choices=options, default="3")
print(promptResponse)


# Demonstration of the spinner functionality
status_list = ["Completing item 1", "Completing item 2", "Completing item 3"]
console = Console()
with console.status("Initial status") as status:
    sleep(3)  # process that takes some time
    for stat in status_list:
        status.update(stat)
        sleep(3)  # process that takes some time


# Demonstration of the progress bar functionality
for i in track(range(20), description="Processing..."):
    time.sleep(1)  # process that takes some time


# Demonstration of the table functionality
table = Table(title="Table Title")
table.add_column("Column 1", justify="right", style="cyan", no_wrap=True)
table.add_column("Column 2", style="magenta")

table.add_row("Row 1, Column 1", "Row 1, Column 2")
table.add_row("Row 2, Column 1", "Row 2, Column 2")

console = Console()
console.record = True
console.print(table)


# Write the output of the table demonstration to a HTML file
html = console.export_html()
f = open("file.html", "w")
f.write(html)
f.close()

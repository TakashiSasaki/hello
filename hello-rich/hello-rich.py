from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
import time

console = Console()

layout = Layout()
layout.split(
    Layout(name="header", size=3),
    Layout(name="main", ratio=1)
)

layout["header"].update(Panel("Header Area: Display Information Here", style="bold red"))
layout["main"].update(Panel("Main Area"))

console.clear()
console.print(layout)

# Simulate updating the header with new information
for i in range(1, 6):
    layout["header"].update(Panel(f"Header Area: New Information {i}", style="bold red"))
    console.clear()
    console.print(layout)
    time.sleep(1)

from blessed import Terminal
import time

term = Terminal()

print(term.clear)

def update_header(text):
    print(term.move_xy(0, 0) + term.red_on_black(text))

def update_main(text):
    print(term.move_xy(0, 3) + text)

with term.fullscreen(), term.hidden_cursor():
    update_header("Header Area: Display Information Here")
    update_main("Main Area")

    # Simulate updating the header with new information
    for i in range(1, 6):
        update_header(f"Header Area: New Information {i}")
        time.sleep(1)

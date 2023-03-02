# Russian Reversal Joke Generator
# Idea by Mary Zotter

import tkinter

# Window Stuff
window = tkinter.Tk()
window.title("Russian Reversal Joke Generator")
window.geometry("500x500")

def joke():
    # Gets User Input
    noun = noun_entry.get()
    verb = verb_entry.get()

    # Button States
    reset_button["state"] = "normal"
    joke_button["state"] = "disabled"

    # Returns Joke
    label_joke["text"] = f"In America, you {verb} {noun}. In Soviet Russia, {noun} {verb} you."

def reset():
    reset_button["state"] = "disabled"
    joke_button["state"] = "normal"
    label_joke["text"] = ""
    noun_entry.delete(0, "end")
    verb_entry.delete(0, "end")

# Fun Stuff
enter_noun = tkinter.Label(window, text="Enter a noun:")
enter_noun.pack()

noun_entry = tkinter.Entry(window)
noun_entry.pack()

enter_verb = tkinter.Label(window, text="Enter a verb:")
enter_verb.pack()

verb_entry = tkinter.Entry(window)
verb_entry.pack()

joke_button = tkinter.Button(window, text="Create Joke", command=joke)
joke_button.pack()

label_joke = tkinter.Label(window, text="")
label_joke.pack()

reset_button = tkinter.Button(window, text="Reset", command=reset, state="disabled")
reset_button.pack()

window.mainloop()

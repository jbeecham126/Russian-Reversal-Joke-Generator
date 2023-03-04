# Russian Reversal Joke Generator
# Idea by Mary Zotter

import tkinter

# Window Stuff
window = tkinter.Tk()
window.title("Russian Reversal Joke Generator")
window.geometry("500x500")

def create_joke():
    # Gets User Input
    noun = noun_entry.get()
    verb = verb_entry.get()

    # Button States
    reset_button.configure(state="normal")
    joke_button.configure(state="disabled")

    # Creates Joke
    joke = f"In America, you {verb} {noun}. In Soviet Russia, {noun} {verb} you."
    label_joke.configure(text=joke)

def reset():
    reset_button.configure(state="disabled")
    joke_button.configure(state="normal")
    label_joke.configure(text="")
    noun_entry.delete(0, tkinter.END)
    verb_entry.delete(0, tkinter.END)

# Fun Stuff
enter_noun = tkinter.Label(window, text="Enter a noun:")
enter_noun.pack()

noun_entry = tkinter.Entry(window)
noun_entry.pack()

enter_verb = tkinter.Label(window, text="Enter a verb:")
enter_verb.pack()

verb_entry = tkinter.Entry(window)
verb_entry.pack()

joke_button = tkinter.Button(window, text="Create Joke", command=create_joke)
joke_button.pack()

label_joke = tkinter.Label(window, text="")
label_joke.pack()

reset_button = tkinter.Button(window, text="Reset", command=reset, state="disabled")
reset_button.pack()

window.mainloop()

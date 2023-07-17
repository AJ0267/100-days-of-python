import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#label
my_label = tkinter.Label(text="my name is Aniket", font=("Arial", 24, "bold"))
my_label.pack()
# my_label["text"] = "new text"
my_label.config(text="new text")

#button
def button_clicked():
    print("button clicked")
    # my_label["text"] = "button is clicked"
    new_text = input.get()
    my_label.config(text=new_text)
    

button = tkinter.Button(text= "click me", command=button_clicked)
button.pack()

#entry
input = tkinter.Entry(width=10)
input.pack()
print(input.get())


window.mainloop()

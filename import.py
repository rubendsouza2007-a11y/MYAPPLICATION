
import tkinter as tk
#create a root window
root=tk.Tk()

root .title("my app")       #Application name 

root.geometry("240x340")    #width x length of the root window

 #Add widgets here
label1=tk.Label(root,text="hello world")
label1.pack()               #this will pack the label in the root window

def click():
    print("Button clicked!")
button=tk.Button(root,text="click me",command=click)  #this will create a button and when we click the button it will call the click function which will print "Button clicked!" in the console  
button.pack()               #this will pack the button in the root window 

entry=tk.Entry(root)        #this will create an entry widget in the root window
entry.pack()                #this will pack the entry widget in the root window
text=entry.get()            #Get the value entered in the entry widget and store it in the variable text
print(text)                 #this will print the value entered in the entry widget in the console 

text = tk.Text(root, height=5, width=30)        #this will create a text widget in the root window with height 5 and width 30
text.pack()                 #this will pack the text widget in the root window
text.insert(tk.END, "This is a text widget")    #this will insert the text "This is a text widget" in the text widget at the end of the text widget
 
""" # Grid example
label = tk.Label(root, text="Name:")            #this will create a label widget with the text "Name:" in the root window
label.grid(row=0, column=0) #this will place the label widget in the first row and first column of the grid in the root window"""

entry = tk.Entry(root)
#entry.grid(row=1, column=1)
 
def handle_event(event):                        #this will handle the event when a key is pressed in the root window 
    print(f"Key pressed: {event.char}")         #this will print the key that is pressed in the console  

root.bind("<Key>", handle_event) #this will bind the key event to the root window and when a key is pressed in the root window it will call the handle_event function which will print the key that is pressed in the console
 
 
 
 #run the application
root.mainloop()

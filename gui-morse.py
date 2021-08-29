import tkinter as tk
from tkinter import font
import morsecode,time


####################
#Initial setup

win=tk.Tk()
win.geometry('800x800')
win.title("Morse Code Translator")
win.configure(bg='gray15')

#Icon
photo=tk.PhotoImage(file="icon.png")
win.iconphoto(False,photo)

#tkinter Variables
user_text=tk.StringVar()
translated_morse=tk.StringVar()
timeunit_var=tk.DoubleVar()
frequency_var=tk.DoubleVar()

#Setting default font
defaultFont=font.nametofont("TkDefaultFont")
defaultFont.configure(family="Segoe UI Semibold",size=15)

#Setting text font
textFont=font.nametofont("TkTextFont")
textFont.configure(family="Segoe UI Semibold",size=15)




#######################
#Button functions

#Function for encrypt_button
def encrypt():
    generated_morse=morsecode.encrypt(user_entry.get().upper())
    morse_entry.delete(0,tk.END)
    morse_entry.insert(0,generated_morse)
    

#Function for beep_button
def playsound():
    morsecode.playsound(translated_morse.get(),timeunit_var.get(),frequency_var.get())


######################
#Header

header_frame=tk.Frame(bg='gray15')

#Heading
header=tk.Label(header_frame,text="Morse Code translator",font=('Source Code Pro Semibold',30),
                bg='gray15',fg='steelblue1'
                )
header.pack()

#Morse design
design=tk.Label(header_frame,text='-- --- .-. ... . / -.-. --- -.. .',bg='gray15',fg='red',
                font=('Source Code Pro Semibold',20),)
design.pack()

header_frame.pack(pady=20)


#####################
#User entry

#Text entry frame
user_entry_frame=tk.Frame()

#Text entry label
user_entry_label=tk.Label(text="Enter text",master=user_entry_frame,bg='gray15',
                fg='steelblue1',width=50,anchor='w'
                )
user_entry_label.pack(fill=tk.X)

#Text entry
user_entry=tk.Entry(textvariable=user_text,master=user_entry_frame,font=("Helvetica",15)
                    ,width=50,bg='black',fg='white')
user_entry.pack(fill=tk.Y)

user_entry_frame.pack(pady=30)

#########################
#Button to encrypt

encrypt_button=tk.Button(text='Translate to morse',command=encrypt,bg='firebrick4',fg='white')
encrypt_button.pack()

#########################
#Translated morse

#Morse code frame
morse_code_frame=tk.Frame(bg='gray15')

#Morse code label
morse_code_label=tk.Label(master=morse_code_frame,text="Morse code",bg='gray15',fg='steelblue1',
                anchor='w'
                )
morse_code_label.pack(fill=tk.X)

#Translated morse
morse_entry=tk.Entry(master=morse_code_frame,font=("Helvetica",15),textvariable=translated_morse,
                    width=50,bg='black',fg='white'
                    )
morse_entry.pack()

#Button to play sound
beep_button=tk.Button(master=morse_code_frame,text='Play sound',command=playsound,bg='firebrick4',fg='white',
            width=10)
beep_button.pack(pady=10,anchor='e')

morse_code_frame.pack(pady=30)


######################
#Scales

sliders_frame=tk.Frame(bg='gray15')

#Time unit scale
timeunit_scale=tk.Scale(sliders_frame,orient=tk.HORIZONTAL,from_=0.1,to=1,resolution=0.1,
                variable=timeunit_var,bg='gray15',fg='steelblue1',length=500,label="Set time unit (seconds)",
                relief=tk.FLAT,bd=0,highlightthickness=0
                )
timeunit_scale.set(0.2)
timeunit_scale.pack(pady=10)

#Frequency scale
frequency_scale=tk.Scale(sliders_frame,orient=tk.HORIZONTAL,from_=100,to=3000,resolution=100,
                variable=frequency_var,bg='gray15',fg='steelblue1',length=500,label="Set frequency (Hz)",
                highlightthickness=0
                )
frequency_scale.set(1000)
frequency_scale.pack(pady=10)

sliders_frame.pack()



#####################
win.mainloop()


##To-do

#Folder

#multi-threading
#Efficiency of program
#Hanging when long message
#Stop sound playing

#Widgets javatpoint
#Borders
#relief
#bd
#All widgets functions attributes
#Layout function attributes

#Colors and font
#Color theme
#Entry color
#UI primary and secondary colors

#Text to speech
#pyttsx3

#Layout
#TextBox

#image for speaker

#About menu

#readme.md, pip
#Only for windows

#error handling




import tkinter as tk
from tkinter import font
from tkinter.constants import HORIZONTAL
import morsecode,time


win=tk.Tk()
win.geometry('1920x1080')
win.title("Morse Code Translator")
win.configure(bg='gray15')

#Variables
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

#Function for encrypt_button
def encrypt():
    generated_morse=morsecode.encrypt(user_entry.get().upper())
    morse_entry.delete(0,tk.END)
    morse_entry.insert(0,generated_morse)
    

    
    

#Function for beep_button
def playsound():
    morsecode.playsound(translated_morse.get())

######################
#Header

header=tk.Label(text="Morse Code translator",font=('Source Code Pro Semibold',30),
                bg='gray15',fg='steelblue1'
                )
header.pack(pady=10)
#

design=tk.Label(text='-- --- .-. ... . / -.-. --- -.. .',bg='gray15',fg='red',font=('Segoe UI Semibold',20))
design.pack()





######################

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

#Scale 

sliders_frame=tk.Frame()

#Time unit frame
timeunit_scale=tk.Scale(master=sliders_frame,orient=HORIZONTAL,from_=0.1,to=4,resolution=0.1,
                variable=timeunit_var,bg='gray15',fg='white',length=500
                )
timeunit_scale.pack()

#Frequency frame
frequency_scale=tk.Scale(master=sliders_frame,orient=HORIZONTAL,from_=500,to=3000,resolution=100,
                variable=frequency_var,bg='gray15'
                )
frequency_scale.pack()

sliders_frame.pack()






#####################
win.mainloop()


##To-do

#Beep debugging
#call dot and dash functions


#Speed of beep
#frequency of beep
#Stop sound
#Frequency


#Efficiency of program
#Hanging when long message

#Text to speech
#pyttsx3





#Layout

#Icon

#Borders
#relief
#bd
#All widgets functions

#image for speaker

#TextBox

#Colors and font
#Color theme
#Entry color
#UI primary and secondary colors



#About menu

#readme.md, pip
#Only for windows



#error handling

#winsound sleep



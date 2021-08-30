import tkinter as tk
from tkinter import Variable, font
from tkinter.constants import FLAT, SUNKEN
import morsecode,time


####################
#Initial setup

win=tk.Tk()
win.geometry('800x780+300+0')
win.resizable(False,False)
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

#Function for decrypt_button
def decrypt():
    text=morsecode.decrypt(morse_entry.get())
    user_entry.delete(0,tk.END)
    user_entry.insert(0,text)


#Function for speak
def speak():
    morsecode.speak(user_entry.get())
    
def dot_insert():
    morse_entry.insert(tk.END,'.')

def dash_insert():
    morse_entry.insert(tk.END,'-')

def space_insert():
    morse_entry.insert(tk.END,' ')

def clear():
    morse_entry.delete(0,tk.END)





######################
#Header

header_frame=tk.Frame(bg='gray15')

#Heading
header=tk.Label(header_frame,text="Morse Code translator",font=('Source Code Pro Semibold',30),
                bg='gray15',fg='#f20d0d'
                )
header.pack()

#Morse design
design=tk.Label(header_frame,text='-- --- .-. ... . / -.-. --- -.. .',bg='gray15',fg='#f20d0d',
                font=('Source Code Pro Semibold',20),
                )
design.pack()

header_frame.pack(pady=20)


#####################
#User entry

#Text entry frame
user_entry_frame=tk.Frame(bg='gray15')

#Text entry label
user_entry_label=tk.Label(user_entry_frame,text="Text",bg='gray15',
                fg='#f20d0d',width=50,anchor='w'
                )
user_entry_label.pack()

#Text entry
user_entry=tk.Entry(user_entry_frame,textvariable=user_text,
                    width=50,bg='#D0D0D0',fg='black',relief=tk.FLAT,bd=2
                    )
user_text.set('Enter text here')
user_entry.pack()

speak_button=tk.Button(user_entry_frame,text="Speak",command=speak,bg='#a11212',fg='white',
            activebackground='#a11212',activeforeground='white', relief=tk.FLAT, bd=3)
speak_button.pack(anchor='e',pady=5)

user_entry_frame.pack(pady=30)

#########################
#Button to encrypt

translate_buttons=tk.Frame(bg='gray15')

encrypt_button=tk.Button(translate_buttons,text='Translate text to morse',command=encrypt,bg='#a11212',fg='white',
                activebackground='#a11212',activeforeground='white',
                relief=tk.FLAT,bd=3
                )
encrypt_button.grid(row=0,column=0,padx=5)

decrypt_button=tk.Button(translate_buttons,text='Translate morse to text',command=decrypt,bg='#a11212',fg='white',
                activebackground='#a11212',activeforeground='white',
                relief=tk.FLAT,bd=3
                )
decrypt_button.grid(row=0,column=1,padx=5)

translate_buttons.pack(pady=10)


#########################
#Translated morse

#Morse code frame
morse_code_frame=tk.Frame(bg='gray15')

#Morse code label
morse_code_label=tk.Label(morse_code_frame,text="Morse code",bg='gray15',fg='#f20d0d',
                width=50,anchor='w'
                )
morse_code_label.pack()

#Translated morse
morse_entry=tk.Entry(morse_code_frame,textvariable=translated_morse,
                    width=50,bg='#D0D0D0',fg='black',relief=tk.FLAT,bd=2,
                    )
morse_entry.pack()

#Button to play sound
beep_button=tk.Button(morse_code_frame,text='Play sound',command=playsound,bg='#a11212',fg='white',
            activebackground='#a11212',activeforeground='white', relief=tk.FLAT, bd=3
            )
beep_button.pack(pady=5,anchor='e')



morse_code_frame.pack(pady=30)


######################
#Scales

sliders_frame=tk.Frame(bg='gray15')

#Time unit scale
timeunit_scale=tk.Scale(sliders_frame,orient=tk.HORIZONTAL,from_=0.1,to=1,resolution=0.1,
                variable=timeunit_var,bg='gray15',fg='#f20d0d',length=500,label="Set time unit (seconds)",
                relief=tk.FLAT,bd=0,highlightthickness=0,troughcolor='#D0D0D0',font=("Segoe UI Semibold",12),
                activebackground='#a11212'
                )
timeunit_scale.set(0.2)
timeunit_scale.pack(pady=10)

#Frequency scale
frequency_scale=tk.Scale(sliders_frame,orient=tk.HORIZONTAL,from_=100,to=3000,resolution=100,
                variable=frequency_var,bg='gray15',fg='#f20d0d',length=500,label="Set frequency (Hz)",
                highlightthickness=0,troughcolor='#D0D0D0',font=("Segoe UI Semibold",12),
                activebackground='#a11212'
                )
frequency_scale.set(1000)
frequency_scale.pack(pady=10)

sliders_frame.pack(pady=0)



#####################
win.mainloop()


##To-do

#Dot buttons
#Speak(),playsound() images

#decipher debugging

#Setting default button widget, entry widget, frame widget
#Code duplicacy

#Folder

#multi-threading
#Efficiency of program
#Hanging when long message
#Stop sound playing

#Widgets javatpoint
#Borders
#All widgets functions attributes
#Layout function attributes


#Button focus colors

#Text to speech
#pyttsx3

#Layout
#TextBox

#image for speaker

#About menu

#readme.md, pip install pyttsx3
#Configuration for pyttsx3 https://www.youtube.com/watch?v=6RyCt2xWBcM
#Project reference dll
#Only for windows

#error handling

#translator code modification -gfg

#icon - red shaded png




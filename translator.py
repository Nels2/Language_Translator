from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
##initialized tkinter, window is created
root.geometry('1080x400')##sets window size

root.resizable(0,0)#allows fixed size by user
root.config(bg= 'ghost white')#set background color here

root.title("A Small project, by Nelson --- a Language Translator") # Name of window
Label(root, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", bg = 'white smoke').pack() #widget used to display one or more line of text that is read-only. root= name of window, text = display on label, font = in which the text is written, and pack = organized widget in a 'block'.

Label(root, text = "A Small project, by Nelson", font = "arial 15 bold", bg= 'white smoke', width = '20').pack(side = 'bottom')

Label(root, text = "Enter Text Here", font = 'arial 15 bold', bg = 'white smoke').place(x = 200, y = 60)

Input_text = Text(root, font = 'arial 10', height = 11, wrap = WORD, padx =5, pady = 5, width = 60)
Input_text.place(x = 30, y = 100)

Label(root,text = "Output", font = 'arial 13 bold', bg = 'white smoke').place(x = 780, y = 60)

Output_text = Text(root, font = 'arial 10', height = 11, wrap = WORD, padx = 5, pady = 5, width = 60)
Output_text.place(x = 600, y = 100)

#The above code creates two text widgets, one for entering what the user wants translated and the other for the translated text.
#Continuing, (1.) the above Text() is for the text in the widgets.
#(2.) wrap = WORD will stop the line after the last word that will fit.
#(3.) padx is for padding on the left and right sides of a widget, (4.)paddy is for the padding on the top and bottom of the window.

language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values= language, width = 22)
src_lang.place(x =20, y =60) 
src_lang.set('Please choose a input language.')

dest_lang = ttk.Combobox(root, values = language, width = 22)
dest_lang.place(x = 890, y =60)
dest_lang.set('Choose the output language.')

#Above code, the user will pick the languages they plan to translate to AND from. 
# 1. language gets all the values from the 'LANGUAGES' dictionary in the form of a list.
# 2. ttk.Combobox() is a widget that includes a class of ttk modules. It is a drop-down list, useful to select one option to many.
###########Translator Function###########################
def Translate():
    translator = Translator()
    translated=translator.translate(text = Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
    
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

    # the Translate function will translate the text and give a result in output.
    # src get the language selected as input.
    # dest gets the language to select to translate.
    # END means python will read the text until the end is reached.
    # Out_text.delete(1.0, END) delete all text from line one to end.
    # Output_text.insert(END, translated.text)
    #####Below is translator button!#################
transbtn = Button(root, text = 'Translate', font = 'arial 12 bold', pady = 5, command = Translate, bg = 'blue', activebackground = 'sky blue')
transbtn.place(x = 490, y = 180)

root.mainloop()
#When the translate button is pressed, it will call the translator function on Line (46).
# BUTTON() widget is used to display button on window
# command is called when we click translate.
# activebackground is a color change when button is active
# root.mainloop() is a method that is excuted when this script is run.

import random #Imports a random module for randomly generated pages
from tkinter import * #Imports a GUI to use

def LRU_Page_Replacement(Pages, Frame_Count, MaxPages, OutputTxt):
    S = set()
    Indexes = {}#To store the LRU to check
    Page_Faults = 0 #Imports a random module for randomly generated pages
    OutputTxt.delete("1.0", END)

    #Initialize a For loop to determine each page
    for Page in range(MaxPages):
        #If the set is less than the frame_count(3), it will add the current page into the set
        if len(S) < Frame_Count:
            #If the number is currently on the page then the statement will return as True
            if Pages[Page] not in S:
                S.add(Pages[Page])
                Page_Faults += 1
            Indexes[Pages[Page]]= Page
        #If the set is full, then it will calculate on what is the least recently used page
        #replace the least recently use one for the new one
        else:
            #If the number is currently on the page then the statement will return as True
            if Pages[Page] not in S:
                lru = float('inf')
                for Frame in S:
                    if Indexes[Frame] < lru:
                        lru= Indexes[Frame]
                        val = Frame
                S.remove(val)
                S.add(Pages[Page])
                Page_Faults += 1
            Indexes[Pages[Page]]= Page
        OutputTxt.insert(END, f"Page: {Pages[Page]} -> Frames: {list(S)}\n")

    OutputTxt.insert(END, f"\nTotal Page Faults: {Page_Faults}\n")

#Function to make the randomly Generated Pages
def GeneratePages(MaxPages, Pages): 
    
    for i in range(MaxPages): #The code will randomly generate 10 numbers in logical memory
        Pages.append(random.randint(0,9))
    return Pages

# main code
MaxPages=10
Pages = []
Frame_Count = 3

#Initialize the GUI
Window = Tk()
Window.title("Least Recently Used")
Window.geometry("500x500")

#Frame for the GUI
Frame1 = Frame(Window, width=300, height=300)
Frame1.grid(row=0, column=0)

#Text to show the output of the program
OutputTxt = Text(Window, width= 60, height=20)
OutputTxt.place(relx=0.5, rely=0.6, anchor=CENTER)

#Functions used to make the program
GeneratePages(MaxPages, Pages)
LRU_Page_Replacement(Pages, Frame_Count, MaxPages, OutputTxt)

#Label to show the pages contained in the memory
RandomNumLbl = Label(Window, text=f"Pages inside inside the memory: {Pages}")
RandomNumLbl.place(relx=0.5, rely=0.1, anchor=CENTER)

#To start the GUI
Window.mainloop()



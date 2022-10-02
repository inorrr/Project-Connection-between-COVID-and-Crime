"""
CSC110 FINAL PROJECT - The connection between COVID-19 and Crime
Main file

Authors: Yinuo Zhao, Xiangxuan Kong, Eric Li, and Allen Xu

This file contains the functions and codes necessary for creating graphical user interface for
all three parts of the project.
"""

import sys
import os
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from analysis_1 import create_one_plot
from analysis_2 import plot_together
from analysis_3 import final_plot
from PIL import ImageTk, Image


################################################################################
# Part 1 Analysis Functions
################################################################################
def plot() -> None:
    """
    This function calls create_one_plot() in analysis_1 with the modified year, month, type_list and area_list
    base on the user input. It inset the plot in to a tkinter window, with the tool bar on top of the window.
    """

    # Get the plot
    fig = create_one_plot(select_year(), select_month(), modify_type_list(), modify_area_list())

    # Creating the Tkinter canvas containing the Matplotlib figure
    plot = FigureCanvasTkAgg(fig, master=window)
    plot.draw()

    # Placing the canvas on the Tkinter window
    plot.get_tk_widget().pack(fill='y', expand=True)

    # Creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(plot, window)
    toolbar.update()

    # Placing the toolbar on the Tkinter window
    plot.get_tk_widget().pack(side='bottom')

    # Disable the plot button after a plot is created
    plot_button['state'] = tk.DISABLED


def select_year() -> int:
    """
    Returns the integer value of the year selected. Modifies the label of select year to be
    "You have selected (the year selected)"

    """
    year_label.configure(text='You have selected ' + year_str.get())
    return int(year_str.get())


def select_month() -> int:
    """
    Returns the integer value of the month selected. Modifies the label of select month to be
    "You have selected (the month selected)"
    """
    month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                  'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    month_label.configure(text='You have selected ' + month_str.get())

    return month_dict[month_str.get()]


def modify_type_list() -> list[str]:
    """
    Returns a list of selected types(of crime) to plot on the graph
    """
    selected_type = []
    type_list = ['Assaults', 'Sexual Assaults', 'Uttering threats', 'Robbery', 'Breaking and Entering',
                 'Impaired Driving', 'Calls for Service', 'Shoplifting', 'Fraud', 'COVID-19', 'Others']
    var_lst = [type_var1.get(), type_var2.get(), type_var3.get(), type_var4.get(), type_var5.get(),
               type_var6.get(), type_var7.get(), type_var8.get(), type_var9.get(), type_var10.get(),
               type_var11.get()]
    for i in range(11):
        if var_lst[i] == 1:
            selected_type.append(type_list[i])
    return selected_type


def modify_area_list() -> list[str]:
    """
    Returns a list of selected areas to plot on the graph
    """
    selected_area = []
    area_list = ['Newfoundland', 'New Brunswick', 'Ontario', 'Manitoba',
                 'Saskatchewan', 'Alberta', 'British Columbia', 'Quebec', 'Total(National)']
    var_lst = [area_var1.get(), area_var2.get(), area_var3.get(), area_var4.get(),
               area_var5.get(), area_var6.get(), area_var7.get(), area_var8.get(), area_var9.get()]
    for i in range(9):
        if var_lst[i] == 1:
            selected_area.append(area_list[i])
    return selected_area


def restart_program() -> None:
    """
    Restart the entire program. (all frames, labels and buttons will be restored)
    """
    python = sys.executable
    os.execl(python, python, * sys.argv)


def quit_p1() -> None:
    """
    Quit the first window
    """
    window.destroy()


################################################################################
# Part 2 Analysis Functions
################################################################################
def select_area() -> None:
    """
    Plot the graph of the selected area. (Analysis 2)

    """
    area_label.configure(text='You have selected ' + area_str.get())
    plot_together(area_str.get())


def quit_p2() -> None:
    """
    Plot the graph for the last part and quit the second window
    """
    window2.destroy()


################################################################################
# Part 2 Analysis Functions
################################################################################
def quit_p3() -> None:
    """
    Quit the last(third) window
    """
    window3.destroy()


################################################################################
# Analysis 1: The number of crime cases by type and area of any specific month
################################################################################
################################################################################
# Constructing the tkinter GUI window
################################################################################

# Creating the window
window = tk.Tk()
window.title('CSC110 Final Project - Connection between COVID-19 and Crime - Analysis 1')

# set the window width and height
window_width = 1400
window_height = 900

# get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# centre position of the window based on the dimension of the screen
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# geometry('widthxheight+-x+-y')
# x +50, left edge of the window be 50 pixels from the left edge of screen
# x -50, right edge of the window be 50 pixels from the left edge of screen
# y +50, top edge of the window be 50 pixels from the top edge of screen
# y -50, bottom edge of the window be 50 pixels from the bottom edge of screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# resizable(False, False will disable resizing of the window)
window.resizable(True, True)

# window.attributes('-alpha', 0.5)  # Transparency of the window: 0.0 (fully transparent) to 1.0 (fully opaque)

# background of the window
window.configure(bg='white')

################################################################################
# Creating the Generate Plot and Reset Button (in a frame)
################################################################################

# Create an empty space at the bottom of the window using an empty tk'Label
empty_label1 = tk.Label(master=window, bg='white', fg='black', height=1, width=1000, text='')
empty_label1.pack(side='bottom')

# Display the notes for the users
notes_label = tk.Label(master=window, bg='white', fg='black', width=1000,
                       text='Notes: Data is only available from March 2019 to August 2021, '
                            'tick all area(s) and type(s) of crime to display on the plot.')
notes_label.pack(side='bottom')

# Empty space between the notes and the buttons
display = tk.StringVar()
empty_label2 = tk.Label(master=window, bg='white', fg='black',
                        height=1, width=1000, textvariable=display, )
empty_label2.pack(side='bottom')

# Creating control frame
control_frame = tk.Frame(master=window, bg='white')
control_frame.pack(side='bottom')

# Creating the plot button
plot_button = tk.Button(master=control_frame, command=plot, bd=0, fg='white',
                        highlightbackground='grey', height=2, width=20, text='Generate Plot', relief='flat')
plot_button.pack(side='left')

# A space between the two buttons
space_label = tk.Label(master=control_frame, bg='white', fg='black', width=4)
space_label.pack(side='left')

# Creating the restart button
restart_button = tk.Button(master=control_frame, command=restart_program, bd=0, fg='white',
                           highlightbackground='grey', height=2, width=20, text="Reset", relief='flat')
restart_button.pack(side='left')

# A space between the two buttons
space_label2 = tk.Label(master=control_frame, bg='white', fg='black', width=4)
space_label2.pack(side='left')

next_button = tk.Button(master=control_frame, command=quit_p1, bd=0, fg='white', highlightbackground='grey',
                        height=2, width=20, text="Next Part", relief='flat')
next_button.pack(side='left')

# Empty space above the two buttons
empty_label3 = tk.Label(master=window, bg='white', fg='black', height=1, width=1000, text='')
empty_label3.pack(side='bottom')


################################################################################
# Creating select month radio button
################################################################################

# Creating the month frame
month_frame = tk.Frame(master=window, bg='white')
month_frame.pack(side='bottom')

# Creating the month label
month_str = tk.StringVar()
month_label = tk.Label(master=month_frame, bg='white', fg='black', width=20,
                       text='Select the Month:', anchor='e')
month_label.pack(side='left')

# Creating the month buttons
month_button_JAN = tk.Radiobutton(master=month_frame, text='Jan', bg='white', fg='black',
                                  variable=month_str, value='January', command=select_month)
month_button_FEB = tk.Radiobutton(master=month_frame, text='Feb', bg='white', fg='black',
                                  variable=month_str, value='February', command=select_month)
month_button_MAR = tk.Radiobutton(master=month_frame, text='Mar', bg='white', fg='black',
                                  variable=month_str, value='March', command=select_month)
month_button_APR = tk.Radiobutton(master=month_frame, text='Apr', bg='white', fg='black',
                                  variable=month_str, value='April', command=select_month)
month_button_MAY = tk.Radiobutton(master=month_frame, text='May', bg='white', fg='black',
                                  variable=month_str, value='May', command=select_month)
month_button_JUN = tk.Radiobutton(master=month_frame, text='Jun', bg='white', fg='black',
                                  variable=month_str, value='June', command=select_month)
month_button_JUL = tk.Radiobutton(master=month_frame, text='Jul', bg='white', fg='black',
                                  variable=month_str, value='July', command=select_month)
month_button_AUG = tk.Radiobutton(master=month_frame, text='Aug', bg='white', fg='black',
                                  variable=month_str, value='August', command=select_month)
month_button_SEP = tk.Radiobutton(master=month_frame, text='Sep', bg='white', fg='black',
                                  variable=month_str, value='September', command=select_month)
month_button_OCT = tk.Radiobutton(master=month_frame, text='Oct', bg='white', fg='black',
                                  variable=month_str, value='October', command=select_month)
month_button_NOV = tk.Radiobutton(master=month_frame, text='Nov', bg='white', fg='black',
                                  variable=month_str, value='November', command=select_month)
month_button_DEC = tk.Radiobutton(master=month_frame, text='Dec', bg='white', fg='black',
                                  variable=month_str, value='December', command=select_month)

# Packing the month buttons
month_button_JAN.pack(side='left')
month_button_FEB.pack(side='left')
month_button_MAR.pack(side='left')
month_button_APR.pack(side='left')
month_button_MAY.pack(side='left')
month_button_JUN.pack(side='left')
month_button_JUL.pack(side='left')
month_button_AUG.pack(side='left')
month_button_SEP.pack(side='left')
month_button_OCT.pack(side='left')
month_button_NOV.pack(side='left')
month_button_DEC.pack(side='left')

################################################################################
# Creating select year radio button
################################################################################

# Creating the year frame
year_frame = tk.Frame(master=window, bg='white')
year_frame.pack(side='bottom')

# Creating the year label
year_str = tk.StringVar()
year_label = tk.Label(year_frame, bg='white', fg='black', width=20, text='Select the Year: ',
                      relief='flat', anchor='e')
year_label.pack(side='left')

# Creating the year buttons
year_button2019 = tk.Radiobutton(master=year_frame, text='2019', bg='white', fg='black',
                                 variable=year_str, value='2019', command=select_year)
year_button2020 = tk.Radiobutton(master=year_frame, text='2020', bg='white', fg='black',
                                 variable=year_str, value='2020', command=select_year)
year_button2021 = tk.Radiobutton(master=year_frame, text='2021', bg='white', fg='black',
                                 variable=year_str, value='2021', command=select_year)

# Packing the year buttons
year_button2019.pack(side='left')
year_button2020.pack(side='left')
year_button2021.pack(side='left')

################################################################################
# Creating select type checker button
################################################################################

# Creating the type frame
# type_list = ['Assaults', 'Sexual Assaults', 'Uttering threats', 'Robbery', 'Breaking and Entering',
#              'Impaired Driving', 'Calls for Service', 'Shoplifting', 'Fraud', 'COVID-19', 'Others']
type_frame = tk.Frame(master=window, bg='white')
type_frame.pack(side='bottom')

# Creating the type label
type_label = tk.Label(type_frame, bg='white', fg='black', width=20, text='Select Type(s) of Crime: ',
                      relief='flat', anchor='e')
type_label.pack(side='left')

# Creating the type button int variable
type_var1 = tk.IntVar()
type_var2 = tk.IntVar()
type_var3 = tk.IntVar()
type_var4 = tk.IntVar()
type_var5 = tk.IntVar()
type_var6 = tk.IntVar()
type_var7 = tk.IntVar()
type_var8 = tk.IntVar()
type_var9 = tk.IntVar()
type_var10 = tk.IntVar()
type_var11 = tk.IntVar()

# Creating the type buttons
type_button1 = tk.Checkbutton(master=type_frame, text='Assaults', bg='white', fg='black',
                              variable=type_var1, onvalue=1, offvalue=0, command=modify_type_list)
type_button2 = tk.Checkbutton(master=type_frame, text='Sexual Assaults', bg='white', fg='black',
                              variable=type_var2, onvalue=1, offvalue=0, command=modify_type_list)
type_button3 = tk.Checkbutton(master=type_frame, text='Uttering threats', bg='white', fg='black',
                              variable=type_var3, onvalue=1, offvalue=0, command=modify_type_list)
type_button4 = tk.Checkbutton(master=type_frame, text='Robbery', bg='white', fg='black',
                              variable=type_var4, onvalue=1, offvalue=0, command=modify_type_list)
type_button5 = tk.Checkbutton(master=type_frame, text='Breaking and Entering', bg='white', fg='black',
                              variable=type_var5, onvalue=1, offvalue=0, command=modify_type_list)
type_button6 = tk.Checkbutton(master=type_frame, text='Impaired Driving', bg='white', fg='black',
                              variable=type_var6, onvalue=1, offvalue=0, command=modify_type_list)
type_button7 = tk.Checkbutton(master=type_frame, text='Calls for Service', bg='white', fg='black',
                              variable=type_var7, onvalue=1, offvalue=0, command=modify_type_list)
type_button8 = tk.Checkbutton(master=type_frame, text='Shoplifting', bg='white', fg='black',
                              variable=type_var8, onvalue=1, offvalue=0, command=modify_type_list)
type_button9 = tk.Checkbutton(master=type_frame, text='Fraud', bg='white', fg='black',
                              variable=type_var9, onvalue=1, offvalue=0, command=modify_type_list)
type_button10 = tk.Checkbutton(master=type_frame, text='COVID-19', bg='white', fg='black',
                               variable=type_var10, onvalue=1, offvalue=0, command=modify_type_list)
type_button11 = tk.Checkbutton(master=type_frame, text='Others', bg='white', fg='black',
                               variable=type_var11, onvalue=1, offvalue=0, command=modify_type_list)

# Packing the type button
type_button1.pack(side='left')
type_button2.pack(side='left')
type_button3.pack(side='left')
type_button4.pack(side='left')
type_button5.pack(side='left')
type_button6.pack(side='left')
type_button7.pack(side='left')
type_button8.pack(side='left')
type_button9.pack(side='left')
type_button10.pack(side='left')
type_button11.pack(side='left')

################################################################################
# Creating select area checker button
################################################################################

# Creating the area frame
# area_list = ['Newfoundland', 'New Brunswick', 'Ontario', 'Manitoba',
#             'Saskatchewan', 'Alberta', 'British Columbia', 'Quebec', 'Total(National)']
area_frame = tk.Frame(master=window, bg='white')
area_frame.pack(side='bottom')

# Creating the area label
area_label = tk.Label(area_frame, bg='white', fg='black', width=20, text='Select Area(s): ',
                      relief='flat', anchor='e')
area_label.pack(side='left')

# Creating the area button int variable
area_var1 = tk.IntVar()
area_var2 = tk.IntVar()
area_var3 = tk.IntVar()
area_var4 = tk.IntVar()
area_var5 = tk.IntVar()
area_var6 = tk.IntVar()
area_var7 = tk.IntVar()
area_var8 = tk.IntVar()
area_var9 = tk.IntVar()

# Creating the area buttons
area_button1 = tk.Checkbutton(master=area_frame, text='Newfoundland', bg='white', fg='black',
                              variable=area_var1, onvalue=1, offvalue=0, command=modify_area_list)
area_button2 = tk.Checkbutton(master=area_frame, text='New Brunswick', bg='white', fg='black',
                              variable=area_var2, onvalue=1, offvalue=0, command=modify_area_list)
area_button3 = tk.Checkbutton(master=area_frame, text='Ontario', bg='white', fg='black',
                              variable=area_var3, onvalue=1, offvalue=0, command=modify_area_list)
area_button4 = tk.Checkbutton(master=area_frame, text='Manitoba', bg='white', fg='black',
                              variable=area_var4, onvalue=1, offvalue=0, command=modify_area_list)
area_button5 = tk.Checkbutton(master=area_frame, text='Saskatchewan', bg='white', fg='black',
                              variable=area_var5, onvalue=1, offvalue=0, command=modify_area_list)
area_button6 = tk.Checkbutton(master=area_frame, text='Alberta', bg='white', fg='black',
                              variable=area_var6, onvalue=1, offvalue=0, command=modify_area_list)
area_button7 = tk.Checkbutton(master=area_frame, text='British Columbia', bg='white', fg='black',
                              variable=area_var7, onvalue=1, offvalue=0, command=modify_area_list)
area_button8 = tk.Checkbutton(master=area_frame, text='Quebec', bg='white', fg='black',
                              variable=area_var8, onvalue=1, offvalue=0, command=modify_area_list)
area_button9 = tk.Checkbutton(master=area_frame, text='Total(National)', bg='white', fg='black',
                              variable=area_var9, onvalue=1, offvalue=0, command=modify_area_list)

# Packing the area buttons
area_button1.pack(side='left')
area_button2.pack(side='left')
area_button3.pack(side='left')
area_button4.pack(side='left')
area_button5.pack(side='left')
area_button6.pack(side='left')
area_button7.pack(side='left')
area_button8.pack(side='left')
area_button9.pack(side='left')

# Empty space between the area buttons and the plot
empty_label4 = tk.Label(master=window, bg='white', fg='black', height=1, width=1000, text='')
empty_label4.pack(side='bottom')

# Mainloop of window 1

window.mainloop()

################################################################################
# Analysis 2: Compare the influence of covid-19 on different types of crimes, by area
################################################################################
################################################################################
# Constructing the tkinter GUI window2
################################################################################

# Creating the window2
window2 = tk.Tk()
window2.title('CSC110 Final Project - Connection between COVID-19 and Crime - Analysis 2')

empty_label2_1 = tk.Label(master=window2, bg='white', height=1, width=1000, text='')
empty_label2_1.pack(side='bottom')

empty_label2_2 = tk.Label(master=window2, bg='white', height=1, width=1000, text='')
empty_label2_2.pack(side='top')

img = Image.open('map.jpg')
resize_image = img.resize((840, 620))
bg = ImageTk.PhotoImage(resize_image)
bg_image = tk.Label(master=window2, bd=0, image=bg, justify='center')
bg_image.pack()

# geometry('widthxheight+-x+-y')
window2.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# resizable(False, False will disable resizing of the window2)
window2.resizable(True, True)

# background of the window2
window2.configure(bg='white')


################################################################################
# Creating the next analysis (Analysis 3) Button (in a frame)
################################################################################

# Creating control frame
control_frame = tk.Frame(master=window2, bg='white')
control_frame.pack(side='bottom')

# Creating the next part button
generate_plot = tk.Button(master=control_frame, command=quit_p2, bd=0, fg='white',
                          highlightbackground='grey', height=2, width=20, text="Next part", relief='flat')
generate_plot.pack(side='left')

# Empty space between the notes and the button
display = tk.StringVar()
empty_label2 = tk.Label(master=window2, bg='white', fg='black',
                        height=1, width=1000, textvariable=display, )
empty_label2.pack(side='bottom')

# Display the notes for the users
notes_label_2 = tk.Label(master=window2, bg='white', fg='black', width=1000,
                         text='Select an area to plot the graph. Each graph will be a separate page in the browser.')
notes_label_2.pack(side='bottom')

################################################################################
# Creating select area radio button
################################################################################

# Creating the area frame
area_frame = tk.Frame(master=window2, bg='white')
area_frame.pack(side='bottom')

# Creating the area label
area_str = tk.StringVar()
area_label = tk.Label(master=window2, bg='white', fg='black', width=50,
                      text='Select the Area')
area_label.pack(side='bottom')

# Creating the area buttons
area_button_1 = tk.Radiobutton(master=area_frame, text='Newfoundland and Labrador', bg='white', fg='black',
                               variable=area_str, value='Newfoundland and Labrador', command=select_area)
area_button_2 = tk.Radiobutton(master=area_frame, text='New Brunswick', bg='white', fg='black',
                               variable=area_str, value='New Brunswick', command=select_area)
area_button_3 = tk.Radiobutton(master=area_frame, text='Manitoba', bg='white', fg='black',
                               variable=area_str, value='Manitoba', command=select_area)
area_button_4 = tk.Radiobutton(master=area_frame, text='Saskatchewan', bg='white', fg='black',
                               variable=area_str, value='Saskatchewan', command=select_area)
area_button_5 = tk.Radiobutton(master=area_frame, text='Alberta', bg='white', fg='black',
                               variable=area_str, value='Alberta', command=select_area)
area_button_6 = tk.Radiobutton(master=area_frame, text='British Columbia', bg='white', fg='black',
                               variable=area_str, value='British Columbia', command=select_area)
area_button_7 = tk.Radiobutton(master=area_frame, text='Quebec', bg='white', fg='black',
                               variable=area_str, value='Quebec', command=select_area)
area_button_8 = tk.Radiobutton(master=area_frame, text='Ontario', bg='white', fg='black',
                               variable=area_str, value='Ontario', command=select_area)
area_button_9 = tk.Radiobutton(master=area_frame, text='Canada', bg='white', fg='black',
                               variable=area_str, value='Canada', command=select_area)

# Packing the area buttons
area_button_1.pack(side='left')
area_button_2.pack(side='left')
area_button_3.pack(side='left')
area_button_4.pack(side='left')
area_button_5.pack(side='left')
area_button_6.pack(side='left')
area_button_7.pack(side='left')
area_button_8.pack(side='left')

# Mainloop for window 2
window2.mainloop()


################################################################################
# Analysis 3: COVID-19 Policies effect on Crime
################################################################################
################################################################################
# Constructing the tkinter GUI window3
################################################################################

# Creating the window3
window3 = tk.Tk()
window3.title('CSC110 Final Project - Connection between COVID-19 and Crime - Analysis 3')

# geometry('widthxheight+-x+-y')
window3.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# resizable(False, False will disable resizing of the window2)
window3.resizable(True, True)

# background of the window3
window3.configure(bg='white')

empty_label3_1 = tk.Label(master=window3, bg='white', fg='black', height=1, width=1000, text='')
empty_label3_1.pack(side='bottom')

# Creating the quit button
quit = tk.Button(master=window3, command=quit_p3, bd=0, fg='white',
                 highlightbackground='grey', height=2, width=20, text="Quit", relief='flat')
quit.pack(side='bottom')

# Generating the plot for Analysis 3
fig = final_plot()
plot = FigureCanvasTkAgg(fig, master=window3)
plot.draw()
plot.get_tk_widget().pack(fill='y', expand=True)
toolbar = NavigationToolbar2Tk(plot, window3)
toolbar.update()
plot.get_tk_widget().pack(side='bottom')

# Main loop of the third window
window3.mainloop()
















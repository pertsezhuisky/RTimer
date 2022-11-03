###################################################################################################
# This program converts data from "data.oil" to three lists and making two plots using matplotlib #
###################################################################################################

import datetime
import matplotlib.pyplot as plt
from os.path import exists


def data_to_lists():
    """Transcribe data from file to three lists"""

    # creating file "data.oil" if it's not exist
    if not (exists("data.oil")):
        fl = open("data.oil", 'w')
        fl.write("\n")
        fl.close()

    with open("data.oil", 'r') as f:
        # set up the variables
        flag_1 = False  # indicate existence of empty lines in "data.oil"
        flag_2 = False  # indicate if time_twt was recorded
        flag_3 = False  # indicate if time_trt was recorded
        flag_date = False  # indicate if date was written for current block
        date = []
        time_twt = []
        time_trt = []
        f_list = list(f)
        # here is the loop that will split strings from file during the position of line
        for i in range(len(f_list)):
            new_list = f_list[i].split("\n")  # split file data by "\n"
            # for now new_list have two types of data. There is useful data such as date and time and useless such as ""
            # next algorithms choose the correct data and creating three list: date, time from twt and time from trt
            if flag_1 and not flag_date:  # if new line was found and date was not recorded
                date.append(new_list[0])
                flag_date = True
            if new_list[0] == "":  # if there isn't new lines
                flag_1 = True
            if i == 2 or (i + 4) % 2 == 0 and new_list[0] != "": # find lines with time_twt data
                flag_2 = True
                time_twt.append(new_list[0])
            if flag_1 and flag_2 and i != 2 and (i + 4) % 2: # find lines with time_trt data
                flag_3 = True
                time_trt.append(new_list[0])
            if flag_3: # reload variables
                flag_1 = False
                flag_2 = False
                flag_3 = False
                flag_date = False

        f.close()
        show_graphs_week(date, time_twt, time_trt)

def show_graphs_week(date, time_twt, time_trt):
    """ Creating a plot for the previous week """
    plt.style.use("seaborn") # use 'seaborn' style
    xs = [] # list that will show date on the "x" axis
    ys1 = [] # list that will show time_twt on the "y" axis
    ys2 = [] # list that will show time_trt on the "y" axis

    # creating lists for the last 7 days displaying on plots
    xs_week = []
    ys1_week = []
    ys2_week = []
    average_twt = 0
    average_trt = 0
    k = 0
    # converting 'str' date from file to datetime element
    date = [i for i in date if i]
    for i in date:
        lst = list(map(int, i.split('-')))
        xs.append(datetime.datetime(lst[0], lst[1], lst[2]))
    # converting 'str' time_twt from file to 'int' digit
    time_twt = [i for i in time_twt if i]
    for i in time_twt:
        lst = list(map(int, i.split(':')))
        if lst[2] > 0:
            lst[1] = lst[1] + 1
        ys1.append(lst[0] * 60 + lst[1])
        average_twt = average_twt + (lst[0] * 60) + lst[1]
    average_twt = average_twt / len(ys1)

    # converting 'str' time_trt from file to 'int' digit
    time_trt = [i for i in time_trt if i]
    for i in time_trt:
        lst = list(map(int, i.split(':')))
        if lst[2] > 0:
            lst[1] = lst[1] + 1
        ys2.append(lst[0] * 60 + lst[1])
        average_trt = average_trt + lst[0] * 60 + lst[1]
    average_trt = average_trt / len(ys2)
    # this block writes zeros if there is no data from time_twt or time_trt in the file
    while len(ys1) > len(ys2):
        ys2.append(0)
    while len(ys1) < len(ys2):
        ys1.append(0)
    # this block sum two times if they were written in one date, and delete useless data
    ind = 0
    while (len(xs) > 1) and (ind <= len(xs) - 2):
        if xs[ind] == xs[ind + 1]:
            del xs[ind]
            ys1[ind + 1] = ys1[ind] + ys1[ind + 1]
            del ys1[ind]

            ys2[ind + 1] = ys2[ind] + ys2[ind + 1]
            del ys2[ind]
        else:
            ind += 1
    # this block calculates last 7 or fewer days
    if len(xs) >= 7:
        k = len(xs) - 7
    if len(xs) <= 7:
        k = 0
    for i in range(k, len(xs)):
        xs_week.append(xs[i])
        ys1_week.append(ys1[i])
        ys2_week.append(ys2[i])

    # this block showing plots, data showing in minutes
    if len(xs) >= 30: # showing a plot for the previous 30 days if possible
        show_graphs_month(xs, ys1, ys2)
        plt.subplot(1, 2, 1)
    plt.plot(xs_week, ys1_week, '-og', label="Total working time")
    # setting up the position for the text with time
    for i in range(len(xs_week)):
        plt.text(xs_week[i], ys1_week[i] + 2, str(ys1_week[i]))
    plt.plot(xs_week, ys2_week, '-or', label="Total rest time")
    for i in range(len(xs_week)):
        plt.text(xs_week[i], ys2_week[i] + 2, str(ys2_week[i]))
    # writing your average working and rest time
    plt.xlabel("Average working time: " + str(
        round(average_twt, 0)) + " mins" + "                       Average rest time: " + str(
        round(average_trt, 0)) + " mins")
    plt.legend()
    plt.title('Your productivity')
    plt.show()


def show_graphs_month(xs, ys1, ys2):
    """ Creating a plot for the previous month """
    k = 0
    xs_month = []
    ys1_month = []
    ys2_month = []
    average_twt = 0
    average_trt = 0
    k = len(xs) - 30
    if len(xs) <= 30:
        k = 0
    for i in range(k, len(xs)):
        xs_month.append(xs[i])
        ys1_month.append(ys1[i])
        ys2_month.append(ys2[i])
        average_twt = (average_twt + int(ys1[i])) / 30
        average_twt = (average_twt + int(ys2[i])) / 30
    plt.subplot(1, 2, 2)
    plt.plot(xs_month, ys1_month, '-og', label="Total working time")
    for i in range(len(xs_month)):
        plt.text(xs_month[i], ys1_month[i] + 2, str(ys1_month[i]))
    plt.plot(xs_month, ys2_month, '-or', label="Total rest time")
    for i in range(len(xs_month)):
        plt.text(xs_month[i], ys2_month[i] + 2, str(ys2_month[i]))
    plt.xlabel("Average working time: " + str( round(average_twt, 0)) + " mins" + "                       Average rest time: " + str(round(average_trt, 0)) + " mins")
    plt.legend()
    plt.title('Your productivity for last 30 days')
    plt.show()


def main_graph():
    data_to_lists()


if __name__ == '__main__':
    main_graph()

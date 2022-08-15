import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import datetime

def data_to_lists():
    with open("data.txt", "r") as f:
        flag_1 = False
        flag_2 = False
        flag_3 = False
        flag_date = False
        date = []
        time_twt = []
        time_trt = []
        f_list = list(f)
        for i in range(len(f_list)):
            new_list = f_list[i].split("\n")
            if flag_1 == True and flag_date == False:
                date.append(new_list[0])
                flag_date = True
            if new_list[0] == "":
                flag_1 = True
            if i == 2 or (i + 4) % 2 == 0 and new_list[0] != "":
                flag_2 = True
                time_twt.append(new_list[0])
            if flag_1 == True and flag_2 == True and i != 2 and (i + 4) % 2:
                flag_3 = True
                time_trt.append(new_list[0])
            if flag_3 == True:
                flag_1 = False
                flag_2 = False
                flag_3 = False
                flag_date = False

        f.close()
        list_to_digits(date, time_twt, time_trt)

def list_to_digits(date, time_twt, time_trt):
    v = str
    print(date)
    print(time_twt)
    print(time_trt)
    show_graphs_week(date, time_twt, time_trt)
#should do month graphs
def show_graphs_week(date, time_twt, time_trt):
    plt.style.use("seaborn")  # added a new style
    xs = []
    ys1 = []
    ys2 = []
    xs_week = [] # Creating lists for last 7 days displaying on plots
    ys1_week = []
    ys2_week = []
    average_twt = 0
    average_trt = 0
    k = 0
#there is a problem if you type a "" in the file "data.txt". example: invalid literal for int() with base 10: ''. need to fix:D. commited with a problem
    for i in date:
        lst = list(map(int, i.split('-')))
        xs.append(datetime.datetime(lst[0], lst[1], lst[2]))

    for i in time_twt:
        lst = list(map(int, i.split(':')))
        ys1.append(lst[0] * 60 + lst[1])
        average_twt = average_twt + lst[0] * 60 + lst[1]
        average_twt = average_twt / len(ys1)

    for i in time_trt:
        lst = list(map(int, i.split(':')))
        ys2.append(lst[0] * 60 + lst[1])
        average_trt = average_trt + lst[0] * 60 + lst[1]
        average_trt = average_trt / len(ys2)
#calculate last 7 days or less days
    if len(date) >= 7:
        k = len(date) - 7
    if len(date) <= 7:
        k = len(date) - len(date)
    for i in range(len(date)-1,k-1,-1):
        xs_week.append(xs[i])
        ys1_week.append(ys1[i])
        ys2_week.append(ys2[i])
#displaying all stuff
    plt.plot(xs_week, ys1_week, '-og', label = "Total working time")
    for i in range(len(xs_week)):
        plt.text(xs_week[i], ys1_week[i]+10, str(ys1_week[i]))
    plt.plot(xs_week, ys2_week, '-or', label = "Total rest time")
    for i in range(len(xs_week)):
        plt.text(xs_week[i], ys2_week[i]-20, str(ys2_week[i]))
    plt.xlabel("Average working time: " + str(round(average_twt,0)) + " mins" + "                       Average rest time: " + str(round(average_trt,0)) + " mins" )
    plt.legend()
    plt.title('Your productivity')
    plt.show()
    allowing_show_graphs_month(xs,ys1,ys2)

def allowing_show_graphs_month(xs,ys1,ys2):
    if len(xs) == 30:
        show_graphs_month(xs, ys1, ys2)

def show_graphs_month(xs, ys1, ys2):
    pass


def main():
    data_to_lists()

if __name__ == '__main__':
    main()


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
    show_graphs(date, time_twt, time_trt)

def show_graphs(date, time_twt, time_trt):
    xs = []
    for i in date:
        lst = list(map(int, i.split('-')))
        xs.append(datetime.datetime(lst[0], lst[1], lst[2]))
    
    ys1 = []
    for i in time_twt:
        lst = list(map(int, i.split(':')))
        ys1.append(lst[0] * 60 + lst[1])
    print(xs)
    print(ys1)
    plt.plot_date(xs, ys1)
    plt.show()

def main():
    data_to_lists()

if __name__ == '__main__':
    main()
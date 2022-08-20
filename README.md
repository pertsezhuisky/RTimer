What is this code for?
 
RTimer is a program that can help you control your screen-time. GUI was written using PyQT5. Program records your working and resting time, and it can also show plots for last 7 or 30 days.

Main concepts

Project includes this files:
1. main.py - implements the project's logic. It defines all buttons, start and stop timers, allows to save data to the file.
2. plots.py - transforms data from data.oil (working and resting time) and then creates plots based on it.
3. data.oil - where program's data is stored. This file helps to construct plots. It is not recommended to change the data manually.
4. WorkToRest.py - defines the design properties of the project: size of buttons, position of timers, colors of the background, etc.
5. WorkToRest.ui - the design of RTimer. You can use it to customize the ui's appearance.

After launching main.py you would see this GUI:

![Снимок222](https://user-images.githubusercontent.com/111244605/185734399-65b3526f-ba9b-4713-9fc2-f6a8090ac7cf.JPG)

You can see a couple of start and a couple of stop buttons under the timers. Buttons on the left correspond to the Total Working Time, in the right - for the Total Rest Time. If you clicked at the "start" timer begin to raise up. The 'save data' button saves the current data to 'data.oil' file and also resets all of the timers. You can click at "show plots" button, which will show you plots with the data corresponding to the last week and month. 

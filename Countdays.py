from Tkinter import *


def splitInput(dateStart):
    dateList = dateStart.split('.')
    # print dateList
    yearStart = int(dateList[0])
    monthStart = int(dateList[1])
    dayStart = int(dateList[2])
    return yearStart, monthStart, dayStart


def leapORnot(year):
    if year % 4 == 0 and year % 100 != 0:
        leap = 1
    elif year % 400 == 0:
        leap = 1
    else:
        leap = 0
    return leap

# dateStart = '1000.07.05'
# dateEnd = '2015.08.01'
def countDays():
    dateStart = start_var.get()
    dateEnd = end_var.get()

    yearStart, monthStart, dayStart = splitInput(dateStart)
    yearEnd, monthEnd, dayEnd = splitInput(dateEnd)

    leapYear = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 0]
    nonleapYear = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 0]
    leapStart = leapORnot(yearStart)
    leapEnd = leapORnot(yearEnd)

    if yearStart == yearEnd:
        if leapStart == 1:
            if monthStart == 1:
                TotalDays = sum(leapYear[1:monthEnd + 1]) - dayStart - leapYear[monthEnd] + dayEnd
            elif monthStart == 2:
                TotalDays = sum(leapYear[2:monthEnd + 1]) - dayStart - leapYear[monthEnd] + dayEnd
            elif monthStart == 3:
                TotalDays = sum(leapYear[3:monthEnd + 1]) - dayStart - leapYear[monthEnd] + dayEnd
            elif monthStart == 4:
                TotalDays = sum(leapYear[4:monthEnd + 1]) - dayStart - leapYear[monthEnd] + dayEnd
            elif monthStart == 5:
                TotalDays = sum(leapYear[5:monthEnd + 1]) - dayStart - leapYear[monthEnd] + dayEnd
            elif monthStart == 6:
                TotalDays = sum(leapYear[6:monthEnd + 1]) - dayStart - leapYear[monthEnd] + dayEnd
            elif monthStart == 7:
                TotalDays = sum(leapYear[7:monthEnd + 1]) - dayStart - leapYear[monthEnd] + dayEnd
            elif monthStart == 8:
                TotalDays = sum(leapYear[8:monthEnd + 1]) - dayStart - leapYear[monthEnd] + dayEnd
            elif monthStart == 9:
                TotalDays = sum(leapYear[9:monthEnd + 1]) - dayStart - leapYear[monthEnd] + dayEnd
            elif monthStart == 10:
                TotalDays = sum(leapYear[10:monthEnd + 1]) - dayStart - leapYear[monthEnd] + dayEnd
            elif monthStart == 11:
                TotalDays = sum(leapYear[11:monthEnd + 1]) - dayStart - leapYear[monthEnd] + dayEnd
            elif monthStart == 12:
                TotalDays = sum(leapYear[12:monthEnd + 1]) - dayStart - leapYear[monthEnd] + dayEnd
        else:
            if monthStart == 1:
                TotalDays = sum(nonleapYear[1:monthEnd + 1]) - dayStart - nonleapYear[monthEnd] + dayEnd
            elif monthStart == 2:
                TotalDays = sum(nonleapYear[2:monthEnd + 1]) - dayStart - nonleapYear[monthEnd] + dayEnd
            elif monthStart == 3:
                TotalDays = sum(nonleapYear[3:monthEnd + 1]) - dayStart - nonleapYear[monthEnd] + dayEnd
            elif monthStart == 4:
                TotalDays = sum(nonleapYear[4:monthEnd + 1]) - dayStart - nonleapYear[monthEnd] + dayEnd
            elif monthStart == 5:
                TotalDays = sum(nonleapYear[5:monthEnd + 1]) - dayStart - nonleapYear[monthEnd] + dayEnd
            elif monthStart == 6:
                TotalDays = sum(nonleapYear[6:monthEnd + 1]) - dayStart - nonleapYear[monthEnd] + dayEnd
            elif monthStart == 7:
                TotalDays = sum(nonleapYear[7:monthEnd + 1]) - dayStart - nonleapYear[monthEnd] + dayEnd
            elif monthStart == 8:
                TotalDays = sum(nonleapYear[8:monthEnd + 1]) - dayStart - nonleapYear[monthEnd] + dayEnd
            elif monthStart == 9:
                TotalDays = sum(nonleapYear[9:monthEnd + 1]) - dayStart - nonleapYear[monthEnd] + dayEnd
            elif monthStart == 10:
                TotalDays = sum(nonleapYear[10:monthEnd + 1]) - dayStart - nonleapYear[monthEnd] + dayEnd
            elif monthStart == 11:
                TotalDays = sum(nonleapYear[11:monthEnd + 1]) - dayStart - nonleapYear[monthEnd] + dayEnd
            elif monthStart == 12:
                TotalDays = sum(nonleapYear[12:monthEnd + 1]) - dayStart - nonleapYear[monthEnd] + dayEnd
    elif yearStart < yearEnd:
        if leapStart == 1:
            yearStartDays = sum(leapYear[:])
            dayStartGone = sum(leapYear[1:monthStart]) + dayStart
        else:
            yearStartDays = sum(nonleapYear[:])
            dayStartGone = sum(nonleapYear[1:monthStart]) + dayStart
        if leapEnd == 1:
            yearEndDays = sum(leapYear[:])
            dayEndCome = sum(leapYear) - sum(leapYear[1:monthEnd]) - dayEnd
        else:
            yearEndDays = sum(nonleapYear[:])
            dayEndCome = sum(nonleapYear) - sum(nonleapYear[1:monthEnd]) - dayEnd
        distYear = yearEnd - yearStart
        i = 1
        allYearDays = yearStartDays
        while i <= distYear:
            if leapORnot(yearStart + i) == 1:
                allYearDays = allYearDays + sum(leapYear)
            else:
                allYearDays = allYearDays + sum(nonleapYear)
            i = i + 1
        TotalDays = allYearDays - dayStartGone - dayEndCome
    else:
        print 'wrong input because start year > end year'
    result_var.set(TotalDays)
    return TotalDays


# def main():
#     dateStart = raw_input('please input dateStart: ')
#     dateEnd = raw_input('please input dateEnd: ')
#     Total = countDays(dateStart, dateEnd)
#     print Total


# if __name__ == '__main__':
#     main()

label_width = 25
entry_width = 50
button_width = label_width + entry_width
root = Tk()
root.title('count days!')
info = Label(root, text='Hello, world!', width=button_width)
info.grid(row=0, column=0, columnspan=2)

start_info = Label(root, text='date start:', width=label_width)
start_info.grid(row=1, column=0)
start_var = StringVar()
start_var.set('2017.07.03')
start_Entry = Entry(root, width=entry_width, textvariable=start_var)
start_Entry.grid(row=1, column=1)

end_info = Label(root, text='date end:', width=label_width)
end_info.grid(row=2, column=0)
end_var = StringVar()
end_var.set('2019.09.03')
end_Entry = Entry(root, width=entry_width, textvariable=end_var)
end_Entry.grid(row=2, column=1)

submit_button = Button(text='count days', command=countDays, width=button_width)
submit_button.grid(row=3, column=0, columnspan=2)

res_info = Label(root, text='total days:', width=label_width)
res_info.grid(row=4, column=0)
result_var = StringVar()
result_Entry = Entry(root, width=entry_width, textvariable=result_var, state='disabled', highlightcolor='red')
result_Entry.grid(row=4, column=1)

root.mainloop()

date_string = input('Please enter a date of form mm/dd/yyyy: ')

month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

if len(date_string) == 10 and date_string[2] == '/' and date_string[5] == '/' :
    date_list = date_string.split('/')
    if date_list[0].isdigit() and date_list[1].isdigit() and date_list[2].isdigit():
        date_list[2] = int(date_list[2])
        date_list[1] = int(date_list[1])

        if (date_list[0] == '01' or date_list[0] == '03' or date_list[0] == '05' or date_list[0] == '07' or date_list[0] == '08' or date_list[0] == '10' or date_list[0] == '12') and date_list[1] > 0:
            if date_list[1] > 31:
                print('Invalid day for given month:', date_list[1])
            else:
                month = int(date_list[0]) -1
                print(month_list[month], ' ', date_list[1], ', ', date_list[2], sep='')
        elif (date_list[0] == '01' or date_list[0] == '03' or date_list[0] == '05' or date_list[0] == '07' or date_list[0] == '08' or date_list[0] == '10' or date_list[0] == '12') and date_list[1] == 0:
            print('Invalid day:', date_list[1])
        elif date_list[0] == '02' and date_list[1] > 0:
            if date_list[1] > 29:
                print('Invalid day for given month:', date_list[1])
            else:
                print(month_list[1], ' ', date_list[1], ', ', date_list[2], sep='')
        elif date_list[0] == '02' and date_list[1] == 0:
            print('Invalid day:', date_list[1])
        elif (date_list[0] == '04' or date_list[0] == '06' or date_list[0] == '09' or date_list[0] == '11') and date_list[1] > 0:
            if date_list[1] > 30:
                    print('Invalid day for given month:', date_list[1])
            else:
                    month = int(date_list[0]) -1
                    print(month_list[month], ' ', date_list[1], ', ', date_list[2], sep='')
        elif (date_list[0] == '04' or date_list[0] == '06' or date_list[0] == '09' or date_list[0] == '11') and date_list[1] == 0:
            print('Invalid day:', date_list[1])

    else:
        print('Invalid date format. Please enter numbers')
else:
    print('Invalid date format')

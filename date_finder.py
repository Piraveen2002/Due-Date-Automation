import re
import sys

def find_date(file):
    text = ""

    #change the current directory again where you will store all files and make sure to write \\ before the file name
    current = r"C:\\"
    file1 = open(current + file,"r", encoding="utf-8")
    lines = file1.read()
    
    x = re.findall("\d{1,4}\/\d{1,2}\/\d{1,4}", lines)
    z = re.findall("\d{1,4}-\d{1,2}-\d{1,4}", lines)
    y = re.finditer("Jan |Feb |Mar |Apr |May |June |July |Aug |Sept |Oct |Nov |Dec |January |February |March |April |August |September |October |November |December ", lines)
    ydd = re.finditer(r"\s[1-3]*[0-9][s,t,n,r][t,h,d],*\s", lines)
    yd = re.finditer(r"\s[1-3]*[0-9],*\s", lines)
    yy = re.finditer(r"\s20[1-9][1-9]\.*,*\s", lines)

    arr_ydd = []
    arr_yd = []
    arr_yy = []

    for i in ydd:
        arr_ydd.append(i.start())
    
    for i in yd:
        arr_yd.append(i.start())
    
    for i in yy:
        arr_yy.append(i.start())


    for match in y:
        mid = -1
        midy = -1
        mid_dd = -1
        mid_d = -1
        s = match.start()
        e = match.end()
        
        lo = 0
        hi = len(arr_yd) - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            if arr_yd[mid] < s:
                if mid == len(arr_yd) - 1:
                    mid = -1
                    break
                else:
                    lo = mid + 1
            elif arr_yd[mid] > s:
                if mid - 1 >= 0 and arr_yd[mid-1] < s:
                    break
                else:
                    hi = mid - 1
        
        lo = 0
        hi = len(arr_ydd) - 1
        while lo <= hi:
            mid_d = (hi + lo) // 2
            if arr_ydd[mid_d] < s:
                if mid_d == len(arr_ydd) - 1:
                    mid_d = -1
                    break
                else:
                    lo = mid_d + 1
            elif arr_ydd[mid_d] > s:
                if mid_d - 1 >= 0 and arr_ydd[mid_d-1] < s:
                    break
                else:
                    hi = mid_d - 1
        
        lo = 0
        hi = len(arr_yy) - 1
        while lo <= hi:
            midy = (hi + lo) // 2
            if arr_yy[midy] < s:
                if midy == len(arr_yy) - 1:
                    midy = -1
                    break
                else:
                    lo = midy + 1
            elif arr_yy[midy] > s:
                if midy - 1 >= 0 and arr_yy[midy-1] < s:
                    break
                else:
                    hi = midy - 1


        lo = 0
        hi = len(arr_ydd) - 1
        while lo <= hi:
            mid_dd = (hi + lo) // 2

            if arr_ydd[mid_dd] < s:
                if (mid_dd + 1 < len(arr_ydd) and arr_ydd[mid_dd+1] >= s) or mid_dd == len(arr_ydd)-1:
                    break
                else:
                    lo = mid_dd + 1
            
            elif arr_ydd[mid_dd] > s:
                if mid_dd == 0:
                    mid_dd = -1
                    break
                else:
                    hi = mid_dd - 1

        if arr_yd or arr_ydd:
            temp = e-1
            while lines[temp] != ' ':
                temp += 1
            month = lines[s:temp]
            
            if arr_yy:
                year = lines[arr_yy[midy]:arr_yy[midy]+5]
            else:
                year = ""
        
            if arr_ydd and not arr_yd and arr_yy:
                day = lines[arr_ydd[mid_dd]:arr_ydd[mid_dd]+6]
                temp_str = lines[arr_ydd[mid_dd]:s].split()

                if not ',' in day and temp_str[1] == "of":
                    text += day.strip() + " of " +  month + ", " + year.strip() + ",  "
                else:
                    day = lines[arr_ydd[mid_d]:arr_ydd[mid_d]+6]
                    text += month + " " + day.strip().strip(',') + ", " + year.strip() + ",  "

            elif not arr_ydd and arr_yd and arr_yy:
                if mid != -1 and arr_yd[mid] <= arr_yy[midy] and arr_yd[mid] >= temp:
                    day = lines[arr_yd[mid]:arr_yd[mid]+3]
                    text += month + " " + day.strip().strip(',') + ", " + year.strip() + ",  "

            elif arr_ydd and arr_yd:
                if mid != -1 and arr_yy[midy] >= arr_yd[mid] and arr_yd[mid] >= temp:
                    day = lines[arr_yd[mid]:arr_yd[mid]+3]
                    text += month + " " + day.strip().strip(',') + ", " + year.strip() + ",  "
                elif mid_d != -1 and arr_yy[midy] >= arr_ydd[mid_d] and arr_ydd[mid_d] >= temp:
                    day = lines[arr_ydd[mid_d]:arr_ydd[mid_d]+6]
                    text += month + " " + day.strip().strip(',') + ", " + year.strip() + ",  "
                elif mid_dd != -1:
                    day = lines[arr_ydd[mid_dd]:arr_ydd[mid_dd]+6]
                    temp_str = lines[arr_ydd[mid_dd]:s].split()
                    if not ',' in day and temp_str[1] == "of":
                        text += day.strip() + " of " +  month + ", " + year.strip() + ",  "

    file1.close()

    file1 = open(current, "a")

    if text != "":
        file1.write(file + ": " + text + "\n")
    else:
        file1.write(file + ": " + "No matches found!\n")
    
    file1.close()

    return file + ": Done!"

if __name__ == "__main__":
    file = sys.argv[1]
    find_date(file)
            


            

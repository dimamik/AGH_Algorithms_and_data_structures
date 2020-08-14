def timeConversion(s):
    #
    # Write your code here.
    #
    if (s[:2]=="12" ):
        if ( s[8:10]=="AM"):
            return "00" + s[2:8]
        else: return s[:8]
    if s[8:10]==("PM"):
        time = int(s[:2])
        time+=12
        s = str(time) + s[2:8]
        return s
    else:
        return s[:8]

print(timeConversion("12:05:45AM"))
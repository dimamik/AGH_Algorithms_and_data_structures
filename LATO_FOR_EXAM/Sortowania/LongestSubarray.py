def longestSubarray(arr):
    first_distinct = arr[0]
    i=0
    second_distinct = float("-inf")
    i_last = i
    i=0
    tmp_len = 0
    max_len = 0
    while (i<len(arr)):
        if (arr[i]==first_distinct):
            i+=1
            tmp_len+=1
            max_len = max(max_len,tmp_len)
        elif ((second_distinct==float("-inf") and abs(arr[i]-first_distinct)==1) or  (arr[i]==second_distinct and abs(second_distinct-first_distinct)==1)):
                if (second_distinct==float("-inf")):
                    second_distinct = arr[i]
                i+=1
                tmp_len+=1
                max_len = max(max_len,tmp_len)
        else:  
            first_distinct=arr[i]
            if (second_distinct!=float("-inf")):
                first_distinct = second_distinct
                
                tmp_len = 0
            tmp_i = i
            i_last = tmp_i
            second_distinct = float("-inf")
            tmp_len=0
            i = i_last
    return max_len

arr = [1,1,1,3,3,2,2]
print(longestSubarray(arr))

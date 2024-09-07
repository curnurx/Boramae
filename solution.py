def solution(diffs, times, limit):
    
    def calc(x):
        y = 0
        for i in range(len(diffs)):
            if i > 0:
                prev = times[i - 1]
            else:
                prev = 0
            diff = diffs[i]
            time = times[i]
            y += max(0, (diff - x)) * (prev + time) + time
        return y <= limit
    
    if calc(1):
        return 1
    left, right = 1, 100000
    while left + 1 != right:
        mid = (left + right) >> 1
        if calc(mid):
            right = mid
        else:
            left = mid
    
    
    return right

def solution(priorities, location):
    answer = []
    temp = priorities[location]
    count = 0
    while(len(priorities)!=0):
        if location==0:
            if priorities[0] < max(priorities):
                priorities.append(priorities.pop(0))
                location=len(priorities)-1
            else:
                return count+1
        else:
            if priorities[0]<max(priorities):
                priorities.append(priorities.pop(0))
                location-=1
            else:
                priorities.pop(0)
                location-=1
                count+=1
    
    return answer.index(temp)

solution([1,2,3,4,5,6], 3)

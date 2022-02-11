
def solution(jobs):
    jobs.sort()
    job_time = []
    start_time = []
    answer = 0
    job_scheduler = []
    count = 0
    
    for i in range(len(jobs)):
        job_time.append(jobs[i][1])
        start_time.append(jobs[i][0])
        
    while True:
        if len(start_time) == 1:
            job_scheduler.append(start_time[0])
            count = count + job_time[0] + abs(job_scheduler[0])
            job_scheduler.pop(0)
            job_time.pop(0)
            start_time.pop(0)
            print(count, "Schedlure : ", job_scheduler, "\n", "job_tiem : ", job_time, "\n", "start_time : ", start_time)    
            break
        elif start_time[0] <= 0:
            job_scheduler.append(start_time[0])
            count = count + job_time[0] + abs(job_scheduler[0])
            job_scheduler.pop(0)
            start_time[1] -= job_time[0]
            job_time.pop(0)
            start_time.pop(0)
            
            print(count, "Schedlure : ", job_scheduler, "\n", "job_tiem : ", job_time, "\n", "start_time : ", start_time)
    print(job_scheduler, count, job_time)
    answer = count/len(jobs)
    print(count, answer)

    
    return answer

solution([[0, 3], [1, 9], [2, 6]])
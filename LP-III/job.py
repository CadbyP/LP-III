class Job:
    def __init__(self, job_id, deadline, profit):
        self.id = job_id   #Store the value of job_id in this particular object's id attribute."
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs):
    # Step 1: Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    # Step 2: Find maximum deadline
    max_deadline = max(job.deadline for job in jobs)
    
    # Step 3: Create a slot array
    slots = [-1] * (max_deadline + 1)  # -1 means empty
    
    total_profit = 0
    job_order = []
    
    # Step 4: Assign jobs
    for job in jobs:
        # Find a free slot from deadline down to 1
        for t in range(job.deadline, 0, -1):
            if slots[t] == -1:  # if slot is empty
                slots[t] = job.id
                total_profit += job.profit
                job_order.append(job.id)
                break
    
    return job_order, total_profit


# Example usage
if __name__ == "__main__":
    jobs = [
        Job('J1', 2, 100),
        Job('J2', 1, 19),
        Job('J3', 2, 27),
        Job('J4', 1, 25),
        Job('J5', 3, 15),
    ]
    
    order, profit = job_sequencing(jobs)
    print("Scheduled Jobs:", order)
    print("Total Profit:", profit)

    #Greedy Rule Recap

#Sort all jobs by descending profit.

#Try to schedule each job in the latest available slot ≤ its deadline.

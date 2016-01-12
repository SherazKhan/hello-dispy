"""
Example of distributed computing on local network.
"""

def compute(n):
    import time, socket
    time.sleep(n)
    host = socket.gethostname()
    return (host, n)

if __name__ == '__main__':
    import sys
    import dispy

    nodes = sys.argv[1:]
    print('Using nodes: {}'.format(' '.join(nodes)))
    cluster = dispy.JobCluster(compute, nodes=nodes)

    jobs = list()
    for i in range(10):
        job = cluster.submit(1)
        job.id = i # optionally associate an ID to job (if needed later)
        jobs.append(job)

    #cluster.wait()
    for job in jobs:
        host, n = job() # waits for job to finish and returns results
        print('{} executed job {} at {} with {}'.format(host, job.id, job.start_time, n))
        #print(job.stdout, job.stderr, job.exception, job.ip_addr, job.start_time, job.end_time)

    cluster.stats()

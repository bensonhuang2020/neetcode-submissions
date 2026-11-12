class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pt_index_heap = []
        time_index_heap = []
        next_available = 1
        res = []
        # put all of the tasks into the heap with the (enqueue_time, index)
        for i in range(len(tasks)):
            heapq.heappush(time_index_heap, (tasks[i][0], i))
        time = 1
        next_available = time
        while len(res) != len(tasks):
            while time_index_heap and time_index_heap[0][0] <= time:
                curr_task = heapq.heappop(time_index_heap)
                # each pt_index_heap task is the (processing_time, index)
                heapq.heappush(pt_index_heap, (tasks[curr_task[1]][1], curr_task[1]))
            if next_available <= time and pt_index_heap:

                doing_task = heapq.heappop(pt_index_heap)
                res.append(doing_task[1])
                next_available = time + doing_task[0]
                time = next_available
            if time_index_heap and time < time_index_heap[0][0] and not pt_index_heap:
                time = time_index_heap[0][0]
        return res

        # the approach is that we have 2 minheaps, 1 for keeping track of which tasks get enqueued when (with index) and another that has the (processing time, index). the way the heaps work, if the first element is the same, tie is broken by going down the tuple length lexicographically. just have to ensure that we keep track of time and when the cpu is free again. there are also a few cases to think of 1) nice case is when our next free time we have more tasks to run 2) not as nice case, we have no tasks to run the next time we're free, so we'll have to advance time to that next occurrence. any time we want to grab from a minheap too, we should probably ensure that the heap has elements inside. all in all, this is O(nlogn) for the tasks since we have to go through every task and pop it out so it's n * logn. spacewise, this is O(n) as well sicne we'll store all the tasks in the time index heap.

        
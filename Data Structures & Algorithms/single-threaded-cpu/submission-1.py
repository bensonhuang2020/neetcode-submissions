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


        
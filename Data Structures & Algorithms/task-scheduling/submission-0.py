class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # i think we greedily attempt to complete the most common tasks. turn into a counter and then try to complete tasks with the most number
        curr_time = 0
        task_count = Counter(tasks)
        # we don't care about the actual letters themselves, moreso the count behavior
        maxHeap = [-cnt for cnt in task_count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        while q or maxHeap:
            curr_time += 1

            # if the maxHeap is empty, all of the letters are on the queue. we either have to wait for them to empty out so we just take the time or this is the final run before we don't add back on the queue.
            if not maxHeap:
                curr_time = q[0][1]
            else:
                # normal case, we continue with removing the most common letters
                curr = heapq.heappop(maxHeap)
                count = 1 + curr
                # if we're not on 0, then we need to add it back into the queue
                if count != 0:
                    q.append([count, curr_time + n])
            
            # if we are on the correct time, we add the queued up item back into the heap to be taken again.
            if q and q[0][1] == curr_time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return curr_time
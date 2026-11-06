class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        # essentially, we'd like to populate the stack with the flattened list. the hardest part is just flattening the list. we can use a helper that iterates over the current list and if it's an integer, we just append it to the stack, and if it's another list, we just get the list and recursively flatten the list. we reverse hte list because we want to be able to pop off the end to get the start numbers.
        self.stack = []
        self.dfs(nestedList)
        self.stack.reverse()

    def next(self) -> int:
        # since we reversed it, the start is now the end so we can just pop
        return self.stack.pop()

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def dfs(self, nested):
        for n in nested:
            if n.isInteger():
                self.stack.append(n.getInteger())
            else:
                self.dfs(n.getList())


class Solution:
    def simplifyPath(self, path: str) -> str:
        # let's switch it up. our stack only contains the directories. we'll give the rest of it later. for now, we only check to see entire values of directory. if the current directory is a string, we act as normal. if it's ".", we continue and do nothing. if it's "..", we pop off the top. do the join with "/" to give the separators and start with "/".
        stack = []
        cur_dir = []
        for i in range(len(path)):
            if path[i] == "/":
                if cur_dir:
                    directory = "".join(cur_dir)
                    cur_dir = []

                    if directory == ".":
                        continue

                    elif directory == "..":
                        if stack:
                            stack.pop()
                    else:
                        stack.append(directory)
                
            else:
                cur_dir.append(path[i])

        if cur_dir:
            directory = "".join(cur_dir)
            cur_dir = []

            if directory == ".":
                pass # do nothing

            elif directory == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(directory)

        return "/" + "/".join(stack)
        
                

            
            
             
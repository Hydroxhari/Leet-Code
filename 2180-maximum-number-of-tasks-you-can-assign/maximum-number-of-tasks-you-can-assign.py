import bisect

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        # Step 1: Sort the tasks and workers
        tasks.sort()  # Sort tasks in ascending order
        workers.sort()  # Sort workers in ascending order

        # Step 2: Define the function to check if k tasks can be assigned
        def can_assign(k):
            task_subset = tasks[:k]  # Get the first k tasks
            worker_subset = workers[-k:]  # Get the last k workers (strongest)

            pills_left = pills  # Track remaining pills
            task_idx = k - 1  # Largest task
            worker_idx = k - 1  # Strongest worker

            # Step 3: Try to assign tasks to workers
            while task_idx >= 0:
                if worker_subset[worker_idx] >= task_subset[task_idx]:  # Task assigned without a pill
                    worker_idx -= 1  
                    task_idx -= 1  
                else:
                    if pills_left == 0:  # No pills left, cannot assign the task
                        return False

                    # Step 4: Find the first worker who can do the task with a pill
                    idx = bisect.bisect_left(worker_subset, task_subset[task_idx] - strength, 0, worker_idx + 1)

                    if idx > worker_idx:  # No such worker available
                        return False
                    
                    # Remove the worker who was assigned the task
                    worker_subset.pop(idx)
                    
                    worker_idx -= 1  # Move to the next worker
                    task_idx -= 1  # Move to the next task
                    pills_left -= 1  # Decrease the pill count

            return True  # All tasks assigned successfully

        # Step 5: Use binary search to maximize the number of tasks
        left, right = 0, min(len(tasks), len(workers))
        while left < right:
            mid = (left + right + 1) // 2
            if can_assign(mid):
                left = mid  # We can assign `mid` tasks, try to assign more
            else:
                right = mid - 1  # We cannot assign `mid` tasks, try fewer tasks

        # Step 6: Return the maximum number of tasks that can be assigned
        return left
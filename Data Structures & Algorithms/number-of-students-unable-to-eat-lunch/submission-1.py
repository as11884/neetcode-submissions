class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        sandwich_index = 0
        rejected = 0

        while queue and rejected < len(queue):
            student = queue.popleft()
            sandwich = sandwiches[sandwich_index]

            if student == sandwich:
                sandwich_index += 1
                rejected = 0
            else:
                queue.append(student)
                rejected += 1

        return len(queue)
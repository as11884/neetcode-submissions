class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        count = 0
        while students and n != count:
            sand = sandwiches.pop(0)
            student = students.pop(0)
            if sand != student:
                students.append(student)
                sandwiches.insert(0, sand)
                count += 1
            else:
                n -= 1
                count = 0
        
        return n 
            
        
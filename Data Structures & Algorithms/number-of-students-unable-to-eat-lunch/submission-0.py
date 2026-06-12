class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while True:
            if len(sandwiches) == 0 or len(students) == 0:
                break
            elif sandwiches[0] == students[0]:
                del sandwiches[0]
                del students[0]
            elif sandwiches[0] not in students:
                break 
            else:
                x = students[0]
                del students[0]
                students.append(x)

        

        return len(students)
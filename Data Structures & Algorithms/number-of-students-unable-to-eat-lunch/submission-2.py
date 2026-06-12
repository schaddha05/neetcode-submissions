class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        demandOne = sum(students)
        demandZero = len(students) - demandOne

        for i in range(len(sandwiches)):
            curr = sandwiches[i]
            if curr and demandOne > 0:
                demandOne-= 1
            elif not curr and demandZero > 0:
                demandZero -= 1
            else:
                break 

        return demandOne + demandZero

       
class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = [] # keep track of numbers before '['
        str_stack = []
        cur_string = ''
        cur_count = 0
        i = 0 
        while i < len(s):
            if s[i] in '123456789': # if number, build it
                j = s.find('[', i)
                num = int(s[i:j])                
                cur_count = num
                i = j
            elif s[i] == '[':
                count_stack.append(cur_count)
                str_stack.append(cur_string)
                cur_string = ''
                cur_count = 0 
                i += 1
            elif s[i] == ']':
                prev_string = str_stack.pop()
                prev_count = count_stack.pop()
                cur_string = prev_string + (prev_count * cur_string)
                i +=1
            else:
                cur_string += s[i]
                i += 1

        return cur_string



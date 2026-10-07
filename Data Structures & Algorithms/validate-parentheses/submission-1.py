class Solution:
    def isValid(self, s: str) -> bool:
        track = []
        mapping = {'[':']', '{':'}', '(':')'}
        for char in s:
            if char in mapping:
                track.append(char)
            else:
                if len(track) == 0:
                    return False
                left_bracket = track.pop()
                if char != mapping[left_bracket]:
                    return False
        
        return len(track) == 0
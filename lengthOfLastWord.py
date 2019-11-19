def lengthOfLastWord(s: str) -> int:
        if len(s.split(" ")) == 1:
            return len(s)
        return len(s.split(" ")[-1])
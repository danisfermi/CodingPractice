class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            local, domain = email.split('@')
            key = ""
            for i in local.split('+')[0]:
                if i != ".":
                    key = key + i
            s.add(key+"@"+domain)
        return len(s)

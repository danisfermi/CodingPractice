class Codec:
    def __init__(self):
        self.count = 0
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = "http://tinyurl.com/"
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodeMap:
            self.count += 1
            idx = str(self.count)
            self.encodeMap[longUrl] = idx
            self.decodeMap[idx] = longUrl
        else:
            idx = self.encodeMap[longUrl]
        return idx
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodeMap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

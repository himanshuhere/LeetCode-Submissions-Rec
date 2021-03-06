#brute
# class Codec:
#     def __init__(self):
#         self.urls = []

#     def encode(self, longUrl):
#         self.urls.append(longUrl)
#         return 'http://tinyurl.com/' + str(len(self.urls) - 1)

#     def decode(self, shortUrl):
#         return self.urls[int(shortUrl.split('/')[-1])]
    
# Using increasing numbers as codes like that is simple but has some disadvantages, which the below solution fixes:

# If I'm asked to encode the same long URL several times, it will get several entries. That wastes codes and memory.

# People can find out how many URLs have already been encoded. Not sure I want them to know.

# People might try to get special numbers by spamming me with repeated requests shortly before their desired number comes up.

# Only using digits means the codes can grow unnecessarily large. Only offers a million codes with length 6 (or smaller). Using six digits or lower or upper case letters would offer (10+26*2)6 = 56,800,235,584 codes with length 6.

# The following solution doesn't have these problems. It produces short URLs like http://tinyurl.com/KtLa2U, using a random code of six digits or letters. If a long URL is already known, the existing short URL is used and no new entry is generated.

class Codec:

    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        code = ''
        while code in self.url2code:
            for i in range(6):
                code += random.choice(alphabet)
                
        self.url2code[code] = longUrl
        url  = 'http://tinyurl.com/'+code
        self.code2url[url] = longUrl
        return url

    def decode(self, shortUrl):
        return self.code2url[shortUrl]

    #It's possible that a randomly generated code has already been generated before. In that case, another random code is generated instead. Repeat until we have a code that's not already in use. How long can this take? Well, even if we get up to using half of the code space, which is a whopping 626/2 = 28,400,117,792 entries, then each code has a 50% chance of not having appeared yet. So the expected/average number of attempts is 2, and for example only one in a billion URLs takes more than 30 attempts. And if we ever get to an even larger number of entries and this does become a problem, then we can just use length 7. We'd need to anyway, as we'd be running out of available codes.
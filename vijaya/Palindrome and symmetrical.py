string = "amma"
half = int(len(string)/2)
if len(string) % 2 == 0:
    s1 = string[:half]
    s2 = string[half:]
else:
    s1 = string[:half]
    s2 = string[half+1:]
if s1 == s2:
    print(string, "is symmetrical")
else:
    print(string, "is not symmetrical")
if s1 == s2[::-1]:
    print(string, "is palindromeeee")
else:
    print(string, "is not palindrome")

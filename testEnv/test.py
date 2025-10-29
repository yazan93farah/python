from dotenv import load_dotenv
import os

load_dotenv()

username=os.environ.get("USER_NAME")
print("hello, {}".format(username))


a = "Developer"
b = "Akademie"
c = "."
d = "com"

print(a + b)           # DeveloperAkademie
print(a + b + c + d)   # DeveloperAkademie.com
print(a + b)           # You can’t subtract strings, so just print concatenation again
print(5 * c)           # .....
print(a + d)           # Developercom
print(a + b + d)       # DeveloperAkademiecom
# print(d**2)          # Invalid for strings → removed or replaced
print(2 * (c + d))     # .com.com
print(3 * c + 2 * d)   # ...comcom

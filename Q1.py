Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
int total_sum = 0
for i in range(1000):
    if (i%3 == 0 or i%5 == 0):
        total_sum = total_sum+i
print total_sum
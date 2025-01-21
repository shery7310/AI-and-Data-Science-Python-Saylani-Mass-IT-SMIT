# Write a Python function that accepts a dictionary and a key, and returns the value associated with the key.
# If the key doesn’t exist, return "Key not found".

def func(k, some_dict):
    if k in some_dict:
        return some_dict[k]
    else:
        return "Key not found"

student_info = {"Name": "Shehryar", "City": "Faisalabad", "Degree": "Bachelors (CS)", "Programming Languages": ["Python", "JavaScript"],
           "Influential Teachers":
               ("Sir Amran", "Sir Ahmad Jajja", "Sir Saqib", "Sir Waleed", "Sir Rao Umar", "Sir Ahmad Aftab", "Mam Farwa"),
           "Python Learning Channels He Recommends": {"Tech with Tim": "https://www.youtube.com/@TechWithTim", "b001": "https://www.youtube.com/@b001", "Nasir Hussain" : "https://www.youtube.com/@nasirhussain5919", "Corey Schafer": "https://www.youtube.com/@coreyms"}}

print(func("Influential Teachers", student_info))
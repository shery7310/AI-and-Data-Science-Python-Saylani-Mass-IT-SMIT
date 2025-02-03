from typing import Optional

from fastapi import FastAPI, HTTPException
from enum import Enum
from fastapi import FastAPI, Query
import re


from pydantic import BaseModel

studentID = 0
app = FastAPI()

@app.get("/")
def homepage():
    return {"Hello": "World"}

@app.get("/students/all")
def get_student():  # FastAPI automatically validates the type
    return "All Students Endpoint"

@app.get("/students/{student_id}")
def get_student(student_id): # Since we did not use annotations by default we are getting string
    global studentID
    studentID = student_id
    try:
        student_id = int(student_id)
    except: # General Exception Catching
        return "Enter Integers Only"

    try:
        if student_id >= 1000 and student_id < 9999:
            return f"Hey {student_id} how are you?"
        else:
            raise ValueError
    except ValueError:
        return "Enter an id between 1000 and 9999"

# @app.get("/students/{student_id}") #using pydantic constraints
# def get_student(student_id: int):  # FastAPI automatically validates the type
#     if 1000 <= student_id < 9999:
#         return {"message": f"Your id: {student_id} is valid"}
#     else:
#         return {"error": "Enter an ID between 1000 and 9999"}

def true_false_parser(condition: str):
    if condition.capitalize():
        return True
    elif not condition.capitalize():
        return False


@app.get("/students")
def grades_and_session( include_grades:str = False, semester: Optional[str] = None):
    if semester is not None:
        x = re.search("^(Fall|Spring|Summer|Winter)\d{4}$", semester) # returns None if not match is found

        if x is None:
            if str(include_grades) not in ['true', 'True', 'False', 'false']:
                raise HTTPException(status_code=422, detail="include_grades can only be a boolean value")
            else:
                include_grades = true_false_parser(include_grades)
                if include_grades:
                    student_dict = {"student_id": studentID, "grades": {'subject 1': 'empty by default'}}
                    return student_dict

                elif not include_grades:
                    student_dict = {"student_id": studentID}
                    return student_dict

        elif x.string == semester:
            if str(include_grades) not in ['true', 'True', 'False', 'false']:
                raise HTTPException(status_code=422, detail="include_grades can only be a boolean value")
            else:
                include_grades = true_false_parser(include_grades)
                print(include_grades)
                if include_grades:
                    print("true", include_grades)
                    student_dict = {"student_id": studentID, "grades": {'subject 1': 'empty by default'},
                                    'semester': semester}
                    return student_dict

                elif not include_grades:
                    student_dict = {"student_id": studentID, 'semester': semester}
                    return student_dict

    elif semester is None:
        if str(include_grades) not in ['true', 'True', 'False', 'false']:
            raise HTTPException(status_code=422, detail="include_grades can only be a boolean value")
        else:
            include_grades = bool(include_grades)
            if include_grades:
                student_dict = {"student_id": studentID, "grades": {'subject 1': 'empty by default'},
                                'semester': semester}
                return student_dict

            elif not include_grades:
                student_dict = {"student_id": studentID, 'semester': semester}
                return student_dict


'''
just the learning code
class Blog(Enum):
    short = "short"
    story = "story"
    howto = "howto"

@app.get("/blog/type/{blog_type}")
def get_blog_type(blog_type: Blog):
    return {"message": f"success {blog_type.value} blog fetched"}

@app.get("/search")
def show_results(search_query): # similar to https://www.google.com/search?q=what
    return {"showed": f"results for {search_query}"} # this type of http request is being sent
                                                    # http://127.0.0.1:8000/search?search_query=hello

'''


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


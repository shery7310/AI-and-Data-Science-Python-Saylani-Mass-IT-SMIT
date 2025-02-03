### **Assignment 1: University Registration Form API**

#### **Objective**:
Build a FastAPI application to simulate a university registration system. This API will validate user inputs (path, query, and body parameters) based on specific constraints and provide appropriate error messages if validations fail.

#### **Requirements**:
You are required to implement an API with the following endpoints and constraints:

---

### **Endpoints**

#### 1. **Get Student Information**
   - **Endpoint**: `GET /students/{student_id}`
   - **Path Parameter**:
     - `student_id`: An integer greater than `1000` and less than `9999`.
   - **Query Parameters**:
     - `include_grades`: A boolean (true/false) to specify if the grades should be included.
     - `semester`: An optional string of the format `Fall2024`, `Spring2025`, etc. (Pattern: `^(Fall|Spring|Summer)\d{4}$`).

---

#### 2. **Register Student**
   - **Endpoint**: `POST /students/register`
   - **Body Parameters**:
     - `name`: A string (1-50 characters), must contain only alphabets and spaces.
     - `email`: A valid email address.
     - `age`: An integer between 18 and 30.
     - `courses`: A list of strings with course names (minimum 1 course, maximum 5 courses).
   - **Constraints**:
     - Each course name should be between 5-30 characters.
     - Duplicate course names are not allowed.
   - **Example Request**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com",
       "age": 22,
       "courses": ["Mathematics", "Physics", "Chemistry"]
     }
     ```

---

#### 3. **Update Student Email**
   - **Endpoint**: `PUT /students/{student_id}/email`
   - **Path Parameter**:
     - `student_id`: An integer greater than `1000` and less than `9999`.
   - **Body Parameter**:
     - `email`: A valid email address.
   - **Example Request**:
     ```json
     {
       "email": "new.email@example.com"
     }
     ```

---

### **Validation Requirements**
1. **Path Parameters**:
   - Use Pydantic constraints to enforce the valid range for `student_id`.
   - Raise a 422 HTTP error with a message if the `student_id` is invalid.

2. **Query Parameters**:
   - Validate the semester format and ensure `include_grades` is a boolean.
   - If invalid, return a 422 HTTP error with an explanation.

3. **Body Parameters**:
   - Validate all fields using Pydantic models.
   - Return clear error messages for:
     - Missing fields.
     - Invalid email formats.
     - Names that contain non-alphabetic characters.
     - Ages that are out of the range.
     - Course lists that exceed the size limit or contain duplicates.

---

### **Deliverables**
1. FastAPI project folder containing:
   - `main.py`: Contains all endpoints and their logic.
   - Validation logic implemented using Pydantic models and FastAPI constraints.
   - Proper error messages for validation failures.
2. **Postman Collection**:
   - Export and share a Postman collection to test all endpoints.

---

### **Bonus Points**:
- Add a middleware to log incoming requests.
- Add documentation (using Swagger) with clear examples for each endpoint.
- Implement a feature to save data to an in-memory database (like a Python dictionary).

---

- Submit https://forms.gle/xJJpuVZW3kEesGcJ8
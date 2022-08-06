from fastapi import FastAPI

app = FastAPI()

students = list()

@app.get("/home/{stu_name}")
def write_home(stu_name: str):
    return {
        "Name": stu_name,
        "id" : 1
        }

@app.put("/username/{stu_name}")
def put_data(stu_name: str):
    students.append(stu_name)
    return {
        "name": stu_name
        }

@app.post("/post_data}")
def post_data(stu_name: str):
    students.append(stu_name)
    return {
        "names": students
        }

@app.api_route("/nothome", methods=['GET', 'POST', 'PUT'])
def homedata(stu_name: str):
    return{
        "name": stu_name
    } 
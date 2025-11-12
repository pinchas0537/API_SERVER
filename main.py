from fastapi import FastAPI
import uvicorn
import string_ops
app = FastAPI()
a = string_ops.uppercase("aaa")
print(a)
@app.get("/reverse/")
def get_reverse(q:str):
    return string_ops.reverse_str(q)

@app.get("/upercase/{text}")
def get_uppercase(text:str):
    return string_ops.uppercase(text)




if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port = 8000)
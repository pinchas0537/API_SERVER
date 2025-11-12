from fastapi import FastAPI
import uvicorn
import string_ops
app = FastAPI()

@app.get("/reverse/")
def get_reverse(q:str):
    return string_ops.reverse_str(q)

@app.get("/upercase/{text}")
def get_uppercase(text:str):
    return string_ops.uppercase(text)

@app.post("/remove-vowels")
def post_remove_vowels(word:dict):
    letters = word["word"]
    return string_ops.remove_vowels(letters)



if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port = 8000)
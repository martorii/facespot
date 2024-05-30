from fastapi import FastAPI, UploadFile
from utils.model import verify_faces, convert_bytes_to_numpy
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/face_verification/")
async def face_verification(img_1: UploadFile, img_2: UploadFile):
    # Get images
    img_1 = await img_1.read()
    img_2 = await img_2.read()

    # Convert to numpy
    img_1, img_2 = convert_bytes_to_numpy(img_1), convert_bytes_to_numpy(img_2)

    # Get score
    score = verify_faces(img_1, img_2)
    return {"same_person": score}


@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "up and running"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
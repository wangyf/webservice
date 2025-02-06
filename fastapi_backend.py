from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
#import my_python_module  # Replace with the actual import for your module

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"]
)

@app.get("/process")
def process_address(address: str = Query(..., description="Enter an address")):
    try:
        # Use your module to process data
        processed_data = my_python_module.process_data(address)  # Adjust based on your function
        return {"success": True, "data": processed_data}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

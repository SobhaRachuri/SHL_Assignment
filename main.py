import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Load the assessment catalog CSV
catalog_df = pd.read_csv("shl_assessment_catalog.csv")

# Define the request body model
class RecommendRequest(BaseModel):
    query: str

# Define the structure of each recommended assessment
class Assessment(BaseModel):
    url: str
    adaptive_support: str
    description: str
    duration: int
    remote_support: str
    test_type: List[str]

# Define the response model
class RecommendResponse(BaseModel):
    recommended_assessments: List[Assessment]

# ✅ FIXED: Match the required response exactly
@app.get("/health")
def health_check():
    return {"status": "healthy"}  # <-- Must return "healthy", not "ok"

@app.post("/recommend", response_model=RecommendResponse)
def recommend_assessments(request: RecommendRequest):
    query = request.query.lower()

    # Search for matching assessments
    matching = catalog_df[
        catalog_df["Assessment Name"].str.lower().str.contains(query)
    ]

    if matching.empty:
        return {"recommended_assessments": []}

    results = []
    for _, row in matching.iterrows():
        # Convert duration like '45 mins' to int
        try:
            duration_int = int(str(row["Duration"]).split()[0])
        except:
            duration_int = 0

        results.append(Assessment(  # ✅ FIXED: Use Pydantic model here
            url=row["Assessment URL"],
            adaptive_support=row["Adaptive/IRT Support"],
            description=row["Assessment Name"],
            duration=duration_int,
            remote_support=row["Remote Testing Support"],
            test_type=[row["Test Type"]],
        ))

    return {"recommended_assessments": results[:10]}  # limit to 10
import uvicorn
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)

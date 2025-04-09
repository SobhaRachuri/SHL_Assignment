import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Load the assessment catalog CSV
catalog_df = pd.read_csv("shl_assessment_catalog.csv")

# Request model
class RecommendRequest(BaseModel):
    query: str

# Individual assessment structure
class Assessment(BaseModel):
    url: str
    adaptive_support: str
    description: str
    duration: int
    remote_support: str
    test_type: List[str]

# Response model
class RecommendResponse(BaseModel):
    recommended_assessments: List[Assessment]

# Welcome/root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the SHL Assessment Recommender API!"}

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Recommend endpoint
@app.post("/recommend", response_model=RecommendResponse)
def recommend_assessments(request: RecommendRequest):
    query = request.query.lower()

    # Search the catalog
    matching = catalog_df[
        catalog_df["Assessment Name"].str.lower().str.contains(query)
    ]

    # If no results
    if matching.empty:
        return RecommendResponse(recommended_assessments=[])

    results = []
    for _, row in matching.iterrows():
        try:
            duration_int = int(str(row["Duration"]).split()[0])
        except:
            duration_int = 0

        results.append(Assessment(
            url=row["Assessment URL"],
            adaptive_support=row["Adaptive/IRT Support"],
            description=row["Assessment Name"],
            duration=duration_int,
            remote_support=row["Remote Testing Support"],
            test_type=[row["Test Type"]],
        ))

    return RecommendResponse(recommended_assessments=results[:10])

# Uvicorn setup for deployment
import uvicorn
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)

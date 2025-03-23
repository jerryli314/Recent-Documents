from fastapi import FastAPI, Depends
from strawberry.fastapi import GraphQLRouter
import strawberry
from typing import List
from datetime import datetime

# Mock function to simulate fetching data from Google Drive API
def fetch_recent_documents():
    return [
        {"title": "Project Plan", "url": "https://docs.google.com/doc1", "last_modified": "2024-03-18T10:30:00"},
        {"title": "Meeting Notes", "url": "https://docs.google.com/doc2", "last_modified": "2024-03-17T15:45:00"},
        {"title": "Design Specs", "url": "https://docs.google.com/doc3", "last_modified": "2024-03-16T08:20:00"},
        {"title": "Sprint Retrospective", "url": "https://docs.google.com/doc4", "last_modified": "2024-03-15T18:10:00"},
        {"title": "Marketing Strategy", "url": "https://docs.google.com/doc5", "last_modified": "2024-03-14T12:05:00"}
    ]

# Define GraphQL Type
@strawberry.type
class Document:
    title: str
    url: str
    last_modified: datetime

# Define GraphQL Query
@strawberry.type
class Query:
    @strawberry.field
    def recent_documents(self) -> List[Document]:
        docs = fetch_recent_documents()
        return [Document(**doc) for doc in docs]

# Create GraphQL Schema
schema = strawberry.Schema(query=Query)

# FastAPI App
app = FastAPI()
app.include_router(GraphQLRouter(schema), prefix="/graphql")

# Run server (if running standalone)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

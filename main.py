import pytz
from datetime import datetime
from fastapi import FastAPI, Query, HTTPException

app = FastAPI()

@app.get("/api")
async def root(slack_name: str = Query("Precious Damian", description="Slack Name"), track: str = Query("Backend", description="Track")):
    # Getting current day of the week
    current_day = datetime.now(pytz.timezone('Europe/Paris')).strftime('%A')

    # Getting current UTC time
    utc_time = datetime.utcnow().replace(tzinfo=pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub URL for the file being run
    github_file_url = "https://github.com/preciousdamian/hng-task-1-backend/blob/master/main.py"

    # GitHub URL for the full source code repository
    github_repo_url = "https://github.com/preciousdamian/hng-task-1-backend.git"
    
    Response = {
        "slack_name": slack_name,
        "track": track,
        "current_day": current_day,
        "utc_time": utc_time,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }
    
    return Response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
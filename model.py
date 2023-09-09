from pydantic import BaseModel

class InfoResponse(BaseModel):
    slack_name: str
    current_day: str
    utc_time: str
    track: str
    github_file_url: str
    github_repo_url: str
    status_code: int
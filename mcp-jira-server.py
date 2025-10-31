

#!/usr/bin/env python3

from mcp.server.fastmcp import FastMCP
import requests
import base64

# -----------------------------
# Configuration — EDIT THESE
# -----------------------------
JIRA_DOMAIN = ""   # e.g. "myteam.atlassian.net"
JIRA_EMAIL = ""       # Jira login email
JIRA_API_TOKEN = ""      # Read-only API token
# -----------------------------

# Prepare Basic Auth header

print(f"Connecting to https://{JIRA_DOMAIN} as {JIRA_EMAIL}")

auth_bytes = f"{JIRA_EMAIL}:{JIRA_API_TOKEN}".encode("utf-8")
auth_b64 = base64.b64encode(auth_bytes).decode("utf-8")
HEADERS = {
    "Authorization": f"Basic {auth_b64}",
    "Accept": "application/json"
   

}

# -----------------------------
# Initialize MCP server (no name/version args)
# -----------------------------
mcp = FastMCP()


# -----------------------------
# Define a tool with decorator
# -----------------------------
@mcp.tool()
def get_jira_issue(issue_id: str):
    """
    Fetch a Jira issue by its ID (e.g., KAN-4) and return full details.
    """
    url = f"https://{JIRA_DOMAIN}/rest/api/3/issue/{issue_id}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        issue = response.json()
        # Return all fields and metadata
        return issue
    else:
        return {
            "error": f"Failed to fetch issue {issue_id}",
            "status_code": response.status_code,
            "message": response.text
        }


# -----------------------------
# Run the server
# -----------------------------
if __name__ == "__main__":
    print("🚀 Starting MCP Jira Server ...")
    mcp.run()




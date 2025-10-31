# 🧰 MCP Jira Server and MCP Inspector Setup Guide (macOS)

## 🎯 Goal

Set up and test a Python-based MCP server that connects to a Jira Cloud
community instance using the MCP Inspector.

------------------------------------------------------------------------

## 🧩 Prerequisites

-   macOS (tested on macOS Sonoma or newer)
-   Python 3.11+
-   Node.js v22.7.5 or later
-   MCP Inspector v0.17.2
-   Jira Cloud Community Instance
-   API token from Atlassian

------------------------------------------------------------------------

## ⚙️ Step 1: Create a Jira Community Instance

1.  Go to [Atlassian Jira](https://www.atlassian.com/software/jira).
2.  Create or log in to your Jira Cloud community instance (e.g.,
    `myteam.atlassian.net`).
3.  Create at least one sample issue (e.g., `KAN-1`) for testing.

------------------------------------------------------------------------

## 🔑 Step 2: Generate a Jira API Token

1.  Visit [Atlassian API
    Tokens](https://id.atlassian.com/manage-profile/security/api-tokens).
2.  Click **Create API token** → name it (e.g., *MCP Server Token*).
3.  Copy the generated token --- you'll add it to the Python script.

------------------------------------------------------------------------

## 🐍 Step 3: Set Up and Run the Python MCP Server

``` bash
cd mcp_jira_server
python3 -m venv venv
source venv/bin/activate
pip install fastmcp requests
```

Edit `mcp_jira_server.py`:

``` python
JIRA_DOMAIN = "your-domain.atlassian.net"
JIRA_EMAIL = "your-email@example.com"
JIRA_API_TOKEN = "your-api-token"
```

Run the server:

``` bash
python mcp_jira_server.py
```

Expected output:

    🚀 Starting MCP Jira Server ...
    Connecting to https://your-domain.atlassian.net as your-email@example.com

------------------------------------------------------------------------

## 🧠 Step 4: Verify the Server is Running

Check that the server starts without errors.\
It should stay running and display connection logs.

------------------------------------------------------------------------

## 🧩 Step 5: Install and Launch MCP Inspector

``` bash
node -v
npm install -g @modelcontextprotocol/inspector
npx @modelcontextprotocol/inspector
```

Expected output:

    ⚙️ Proxy server listening on localhost:6277
    🔑 Session token: b94156657...
    🌐 MCP Inspector is up and running at:
       http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=b94156657...

------------------------------------------------------------------------

## 🖥️ Step 6: Open MCP Inspector UI

Click the provided localhost link --- the Inspector opens in your
browser.

------------------------------------------------------------------------

## 🧩 Step 7: Configure MCP Inspector Connection

### 7.1 Create STDiO Connection

1.  **Transport Type:** STDiO\
2.  **Command:** `python3`\
3.  **Arguments:**
    `/Users/<yourusername>/mcp-jira-server/mcp_jira_server.py`\
4.  Check environment variables (`HOME`, `PATH`, `SHELL`).\
5.  Click **Restart** → status should show **Connected**.


------------------------------------------------------------------------

### 7.2 Verify Connection & Run Tool

1.  Go to **Tools** tab → click **List Tools**.\
2.  Select `get_jira_issue` and enter a Jira issue ID (e.g., `KAN-4`).\
3.  Click **Run Tool**.\
4.  The JSON response from Jira should appear.

Example:

``` json
{
  "id": "KAN-4",
  "fields": {
    "summary": "Sample Jira Issue",
    "status": { "name": "To Do" }
  }
}
```

------------------------------------------------------------------------

### 7.3 Confirm Server Output

In the terminal where you started the MCP server:

    🚀 Starting MCP Jira Server ...
    Connecting to https://your-domain.atlassian.net as your-email@example.com

------------------------------------------------------------------------

## 🧯 Troubleshooting

  -----------------------------------------------------------------------
  Issue                    Possible Fix
  ------------------------ ----------------------------------------------
  401 Unauthorized         Verify `JIRA_EMAIL` and `JIRA_API_TOKEN` are
                           correct.

  ModuleNotFoundError:     Run `pip install fastmcp requests`.
  fastmcp                  
 
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## ✅ Confirmation

When: - MCP Inspector shows `Connected` - Tool list includes
`get_jira_issue` - JSON output returns Jira issue data

✅ Your MCP--Jira integration is successful! 🎉

------------------------------------------------------------------------

        

# MCP Server for FRED

A lightweight Model Context Protocol (MCP) server designed to access **Federal Reserve Economic Data (FRED)**.

## Requirements

- A FRED API key: [Get one here](https://fred.stlouisfed.org/docs/api/api_key.html)
- Save your API key in a `.env` file in the project root.

## Install
Clone the repo and add below to the config.json

```
"fred": {
    "command": "uv",
    "args": [
        "--directory",
        "/PATH/TO/CLONED/DIRECTORY/mcp-fred/",
        "run",
        "mcp_fred.py"
    ]
}
```

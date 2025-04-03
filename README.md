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


## Status

**Work in Progress** – Currently supports limited functionality.

## To-Do

- [x] Establish connection to the MCP client  
- [ ] Improve output formatting of fetched data  
- [ ] Add support for additional APIs

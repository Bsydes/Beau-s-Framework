# Ephor API Integration Complete

Set up unlimited Claude Opus access via Ephor API.

## Tools Created
- ~/.local/bin/ephor - Query any model (default: claude-opus-4-5)
- ~/.local/bin/ephor-models - List available models

## Usage
ephor "Your query here" [model] [project_id]

## Available Models (highlights)
- claude-opus-4-5, claude-sonnet-4-5-latest
- gpt-5, gpt-5.1, gpt-5.2, o3, o3-pro
- gemini-3-pro, deepseek-r1, grok-4

## Projects Available
- Claude Code: 3b0e10be-d3e0-41a6-ae18-40d11516e934 (default)
- n8n Builder: cf2a5356-9c42-4a4a-8f35-fdc429d4c152
- And 39 more projects

## Auth Format
Header: Authorization: <api_key> (no Bearer prefix)
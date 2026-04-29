# Travel Assistant - Multi-Agent AI System

## 📌 Description

This project implements a multi-agent system for travel planning.

## 🧠 Architecture

* LangGraph: orchestration
* OpenAi: agents
* FastMCP: external data integration

## 🤖 Agents

* Research Agent
* Itinerary Agent
* Budget Agent
* Verification Agent

## 🔌 MCP Servers

* Weather Server
* Cost Server

## 🔄 Patterns Used

* Orchestrator-Workers
* Prompt Chaining
* Evaluator-Optimizer

## 👤 Human-in-the-Loop

User validation before final result

## ▶️ Run the Project

In the first teminal: 
```bash
cd Code
python -m uvicorn MCP_servers.weather_api:app --port 8001
```
In the second teminal: 
```bash
cd Code
python -m uvicorn MCP_servers.cost_api:app --port 8002
```
In the fird terminal:
```bash
pip install -r requirements.txt
python main.py
```
## Link for the video:
[https://youtu.be/yiYr6DJ8uY0](url)

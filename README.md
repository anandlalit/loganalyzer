# LogAnalyzer

An **intelligent, agentic log analysis system** that autonomously parses, structures, and analyzes HTTP server logs to uncover operational insights. Built with AI agents in mind, LogAnalyzer transforms raw log files into queryable intelligence, enabling automated incident detection, performance monitoring, and anomaly identification.

## Why LogAnalyzer?

**For AI Agents**: LogAnalyzer provides a structured, database-backed interface for agents to autonomously:
- Ingest and parse unstructured HTTP log streams
- Identify traffic patterns, anomalies, and potential issues
- Generate intelligent reports and recommendations
- Power automated incident response and monitoring systems

**For DevOps Teams**: Extract actionable insights from application logs without manual parsing:
- Quickly identify problematic IPs, endpoints, or error codes
- Track HTTP method distributions and API usage patterns
- Spot error spikes and unusual traffic
- Support data-driven debugging and optimization

**Architecture**: Built with a clean layered design (Models → Services → Repository) that seamlessly integrates with agentic workflows and AI-driven analysis pipelines.

## Installation

```bash
#install build tool
pip install build

#install dependnecies and build package
python3 -m build

#install build module 
pip install dist/loganalyzer-0.1.0-py3-none-any.whl

# install project in edit mode
pip install -e .
```

## Usage

```python
import loganalyzer
```

## License

MIT

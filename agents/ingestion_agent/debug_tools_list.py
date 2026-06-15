import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from agents.ingestion_agent.agent import agent

print(agent)
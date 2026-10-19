"""Claude Code hook: tells the live office who is working.

Called by .claude/settings.json on UserPromptSubmit, PreToolUse/PostToolUse (Agent/Task) and
SubagentStop / Stop. Reads the hook JSON from stdin and updates office/dashboard/data/live.js,
which the dashboard re-reads every few seconds. Never blocks Claude: any error exits 0 silently.
"""
import datetime, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIVE_JSON = ROOT / "office" / "dashboard" / "data" / "live.json"
LIVE_JS = ROOT / "office" / "dashboard" / "data" / "live.js"
FEED_MAX = 40


def now():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def load():
    try:
        return json.loads(LIVE_JSON.read_text(encoding="utf-8"))
    except Exception:
        return {"agents": {}, "feed": [], "parth": {"status": "idle", "task": ""}}


def save(state):
    state["updated"] = now()
    state["feed"] = state["feed"][-FEED_MAX:]
    LIVE_JSON.write_text(json.dumps(state, indent=1, ensure_ascii=False), encoding="utf-8")
    LIVE_JS.write_text("window.LP_LIVE = " + json.dumps(state, ensure_ascii=False) + ";\n", encoding="utf-8")


def feed(state, who, text):
    state["feed"].append({"time": now(), "who": who, "text": text[:160]})


def main():
    event = json.load(sys.stdin)
    name = event.get("hook_event_name", "")
    state = load()
    agents = state.setdefault("agents", {})

    if name == "UserPromptSubmit":
        task = (event.get("prompt") or "").strip().splitlines()[0][:140] if event.get("prompt") else ""
        state["parth"] = {"status": "giving task", "task": task}
        feed(state, "parth", "New task: " + task)
    elif name in ("PreToolUse", "PostToolUse") and event.get("tool_name") in ("Agent", "Task"):
        ti = event.get("tool_input") or {}
        agent = ti.get("subagent_type") or "general-purpose"
        task = ti.get("description") or (ti.get("prompt") or "")[:80]
        if name == "PreToolUse":
            agents[agent] = {"status": "working", "task": task, "since": now()}
            feed(state, agent, "Started: " + task)
        else:
            resp = json.dumps(event.get("tool_response") or "")
            if "background" in resp.lower() and "completed" not in resp.lower():
                return  # still running in the background; SubagentStop will close it
            agents[agent] = {"status": "done", "task": task, "since": now()}
            feed(state, agent, "Finished: " + task)
    elif name == "SubagentStop":
        agent = event.get("agent_type") or ""
        if agent in agents and agents[agent]["status"] == "working":
            agents[agent].update(status="done", since=now())
            feed(state, agent, "Finished: " + agents[agent]["task"])
    elif name == "Stop":
        state["parth"] = {"status": "reviewing", "task": "Results ready for your review"}
        for a in agents.values():
            if a["status"] == "done":
                a["status"] = "idle"
    else:
        return
    save(state)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)

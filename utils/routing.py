from agents import (
    idea_intake,
    research_agent,
    discovery_agent,
    mvp_architect,
    execution_planner,
    build_agent,
)

def route_next(step: str, payload: dict):
    """
    Simple linear chain:
    idea_intake -> research -> discovery -> mvp -> execution -> build
    """
    if step == "idea_intake":
        # payload = raw idea string
        return research_agent.run(payload)

    if step == "research":
        # payload = idea_card dict
        return discovery_agent.run(payload)

    if step == "discovery":
        # payload = discovery_pack dict
        return mvp_architect.run(payload)

    if step == "mvp":
        # payload = mvp_spec dict
        return execution_planner.run(payload)

    if step == "execution":
        # payload = execution_plan dict
        return build_agent.run(payload)

    return None

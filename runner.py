import sys
from agents import idea_intake
from utils.routing import route_next

def run_full_chain(raw_idea: str):
    # 1. Idea Intake
    idea_card = idea_intake.run(raw_idea)
    if not idea_card:
        return

    # 2. Research
    research_brief = route_next("idea_intake", idea_card)
    if not research_brief:
        return

    # 3. Discovery
    discovery_pack = route_next("research", research_brief)
    if not discovery_pack:
        return

    # 4. MVP
    mvp_spec = route_next("discovery", discovery_pack)
    if not mvp_spec:
        return

    # 5. Execution
    execution_plan = route_next("mvp", mvp_spec)
    if not execution_plan:
        return

    # 6. Build
    build_pack = route_next("execution", execution_plan)
    if not build_pack:
        return

    print("Full chain completed for idea.")

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python runner.py idea_intake \"raw idea\"")
        print("  python runner.py full \"raw idea\"")
        return

    mode = sys.argv[1]
    content = sys.argv[2]

    if mode == "idea_intake":
        idea_intake.run(content)

    elif mode == "full":
        run_full_chain(content)

if __name__ == "__main__":
    main()

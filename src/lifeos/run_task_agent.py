from dotenv import load_dotenv
from agents.run import Runner
from lifeos.lifeos_agents.task_agent import build_task_agent

load_dotenv()

task_agent = build_task_agent()

def main():
    print("=== Adding a task ===")
    result_add = Runner.run_sync(
        starting_agent=task_agent,
        input="Cook chicken for dinner."
    )
    print("Final answer:", result_add.final_output)

    print("\n=== Listing tasks ===")
    result_list = Runner.run_sync(
        starting_agent=task_agent,
        input="Show me all my tasks."
    )
    print("Final answer:", result_list.final_output)

if __name__ == "__main__":
    main()
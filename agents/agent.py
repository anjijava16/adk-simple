# quick demo for Google ADK agents example

from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()


def main():
    agent = Agent(
        name="Simple_Hello_ADK_Agent",
        description="A hello world agent",
        model="gemini-1.5-flash-latest",
        instruction=("You are simple Agent"),
    )
    print(f" agent = {agent}")


if __name__ == "__main__":
    main()

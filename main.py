from crewai import Crew
from pydantic import BaseModel

from agents import p_j_a_Agents
from tasks import wp_wj_wa_Tasks

class WritingCrew(BaseModel):
    subject: str

    def run(self):
        # Defining Agents and Tasks
        agents = p_j_a_Agents()
        tasks = wp_wj_wa_Tasks()

        expert_poem_agent = agents.expert_poem_agent()
        joke_expert_agent = agents.joke_expert_agent()
        article_master_agent = agents.article_master_agent()

        write_poem = tasks.write_poem(
            expert_poem_agent,
            subject=self.subject
        )

        write_joke = tasks.write_joke(
            joke_expert_agent,
            subject=self.subject
        )

        write_article = tasks.write_article(
            article_master_agent,
            subject=self.subject
        )

        crew = Crew(
            agents=[
                expert_poem_agent,
                joke_expert_agent,
                article_master_agent
                ],
            tasks=[
                write_poem,
                write_joke,
                write_article
            ],
            verbose = True
        )

        result = crew.kickoff()
        return result
    
if __name__ == "__main__":
    print("## Welcome to Write Poem, Joke and Article Crew")
    print('-------------------------------------')
    Subject = input("What is the subject you are looking for? ")

writing_crew = WritingCrew(subject=Subject)
result = writing_crew.run()
print("\n\n########################")
print(f"## Here is your Poem, Joke and Article on the given {Subject}")
print("############################")
print(result)





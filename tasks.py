from crewai import Task
from pydantic import BaseModel

class wp_wj_wa_Tasks(BaseModel):

    def __tip_section(self):
        return "if you do BEST WORK, I'll give you a $10,000 commission!"
    
    def write_poem(self, Agent: str, subject: str):
        return Task(
            description=f"""
                **Task**: Develop a engaging Poem
                **Description**: Write an engaging poem based on the given input should possess a keen 
                understanding of poetic devices and techniques. They should have a talent for weaving imagery 
                and emotion into their verses, creating vivid and evocative imagery that resonates with 
                readers. The agent should be adept at capturing the essence of the provided input, 
                whether it be a theme, a concept, or a specific set of emotions, and translating it into 
                lyrical language. Additionally, they should be able to adapt their writing style to suit 
                the tone and mood desired for the poem, whether it's playful and whimsical or profound 
                and introspective. Ultimately, the agent's goal is to craft a poem that captivates the 
                reader's imagination, evokes deep emotions, and leaves a lasting impression.
        
                **Parameters**:
                - Subject: {subject}

                **Note**: {self.__tip_section}
                """,
            agent=Agent,
            expected_output="Develop an engaging Poem"
        )
    
    def write_joke(self, Agent: str, subject: str):
        return Task(
            description=f"""
                **Task**: Develop a Tremendous Laughable Joke. 
                **Description**: Write a joke based on the given input should possess a sharp wit and a 
                knack for humor. They should have a keen understanding of comedic timing, delivery, and 
                wordplay. The agent should be able to take the provided input, whether it's a situation, 
                a theme, or a set of characters, and creatively twist it into a humorous punchline or 
                setup. Additionally, they should consider the audience's sensibilities and tailor the 
                joke to suit the desired tone and style, whether it's light-hearted and playful or clever 
                and satirical. The agent's goal is to elicit laughter and amusement from the audience, 
                creating a moment of shared joy and levity.
        
                **Parameters**:
                - Subject: {subject}

                **Note**: {self.__tip_section}
                """,
            agent=Agent,
            expected_output="Develop a Tremendous Laughable Joke."
        )
    
    def write_article(self, Agent: str, subject: str):
        return Task(
            description=f"""
            **Task**: Gather In-depth Information of the input given and Write an article for that topic. 
            **Description**: As the designated agent tasked with crafting an article based on the provided 
            input, your role is to transform the given information into a compelling and informative piece 
            of writing. Drawing upon your expertise in research and writing, you will meticulously gather 
            relevant data, facts, and insights to support your article's premise. Your writing should be 
            engaging, clear, and well-structured, catering to the target audience's interests and needs. 
            Additionally, you will need to ensure accuracy and credibility by citing credible sources and 
            providing thorough analysis. Your ultimate goal is to deliver an article that informs, educates, 
            and inspires readers, leaving a lasting impact with its depth and clarity.
        
            **Parameters**:
            - Subject: {subject}

            **Note**: {self.__tip_section}
            """,
            agent=Agent,
            expected_output="Write an article"
        )
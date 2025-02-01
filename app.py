from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool

from dotenv import load_dotenv


load_dotenv()

topic = "Medical Industry using Generative AI"


#Tool 1
llm  = LLM(model="gpt-3.5-turbo")

#Tool 2
search_tool = SerperDevTool(n=3)


#Agent 1
senior_research_analyst = Agent(
    role = "Senior Research Analyst",
    goal = f"Research, analyze, and synthesize comprehensive information on {topic} from reliable web sources",
    backstory = "You're an  expert research analyst with advanced web research skills. "
                "You excel at finding, analyzing, and synthesizing information from "
                "across the internet using search tools. You're skilled at "
                "distinguishing reliable sources from unreliable ones, "
                "fact-checking, cross-referencing information, and "
                "identifying key patterns and insights. You provide "
                "well-organized research briefs with proper citations "
                "and source verification. Your analysis includes both "
                "raw data and interpreted insights, making complex "
                "information accessible and actionable.",
    allow_delegation = False,
    verbose = True,
    tools = [search_tool],
    llm = llm


)


#Agent 2

content_writer = Agent(

    role = "Content-Writer",
    goal = "transform research findings into engaging blog posts while maintaining accuracy ",
    backstory = "You're a skilled content writer specialized in creating "
                "engaging, accessible content from technical research. "
                "You work closely with the Senior Research Analyst and excel at maintaining the perfect "
                "balance between informative and entertaining writing, "
                "while ensuring all facts and citations from the research "
                "are properly incorporated. You have a talent for making "
                "complex topics approachable without oversimplifying them.",
    allow_delegation = False,
    verbose = True,
    llm = llm
)


#Research Tasks (Task1)

research_tasks = Task(
    description = ("""
            1. Conduct comprehensive research on {topic} including:
                -Recent developments and news
                -Key industry trends and innovations
                -Expert opinions and analysis
                -Statistical data and market insights
            2. Evaluate source credibility and fact-check all information
            3. Organize findings into a structured research brief
            4. Include all relevant citations and sources
        """),
    expected_output = """A detailed research report containing:
            -Executive summary of key findings
            -Comprehensive analysis of current trends and developments
            -List of verfied facts and statistics
            -All citations and links to original sources
            -Clear categotization of main themes and patterns
            Please format with clear sections and bullet points for easy reference.""",

    agent = senior_research_analyst
                      
)

#Content Writing (Task2)    

writing_task = Task(
    description = ("""
        Using the reserach brief provided, create an engaging blog post that:
        1. Transforms technical information into accessible content 
        2. Maintains all factual accuracy and citations from the research
        3. Includes:
            -Attention-grabbing introduction
            -Well-structured body sections with clear headings
            -Compelling conclusion
        4. Preserves all source citations in [source: URL] format
        5. Includes a references section at the end
    """),
    expected_output= """A polished blog post in markdown format that:
        - Engages readers while maintaining accuracy
        - Contains properly structured sections
        - Includes Inline citations hyperlinked to the original source url
        - Presents information in an accessible yet informative way
        - Follows proper markdown formatting, use H1 for the title and H3 for the sub-sections""",

    agent = content_writer

) 

crew = Crew(
    agents= [senior_research_analyst,content_writer],
    tasks = [research_tasks,writing_task],
    verbose= True

)

result = crew.kickoff(inputs={"topic" : topic})    

print(result)

print(type(result))


            

    



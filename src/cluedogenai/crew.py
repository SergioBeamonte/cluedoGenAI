from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Cluedogenai():
    """Cluedogenai crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def narrative_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['narrative_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def character_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['character_agent'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def dialogue_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['dialogue_agent'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def vision_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['vision_agent'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def audio_agent(self) -> Agent: # Delete if we delete this agent
        return Agent(
            config=self.agents_config['audio_agent'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def director_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['character_agent'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def create_scene_blueprint(self) -> Task:
        return Task(
            config=self.tasks_config['create_scene_blueprint'], # type: ignore[index]
        )

    @task
    def define_characters(self) -> Task:
        return Task(
            config=self.tasks_config['define_characters'], # type: ignore[index]
            output_file='report.md'
        )
    
    @task
    def generate_suspect_dialogue(self) -> Task:
        return Task(
            config=self.tasks_config['generate_suspect_dialogue'], # type: ignore[index]
            output_file='report.md'
        )
    
    @task
    def design_scene_visuals(self) -> Task:
        return Task(
            config=self.tasks_config['design_scene_visuals'], # type: ignore[index]
            output_file='report.md'
        )
    
    @task
    def curate_scene_audio(self) -> Task: # Delete if we delete this agent
        return Task(
            config=self.tasks_config['curate_scene_audio'], # type: ignore[index]
            output_file='report.md'
        )
    
    @task
    def game_play_director_step(self) -> Task:
        return Task(
            config=self.tasks_config['game_play_director_step'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Cluedogenai crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

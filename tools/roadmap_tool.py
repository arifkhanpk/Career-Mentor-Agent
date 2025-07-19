from agents.base_agent import BaseAgent

class RoadmapTool(BaseAgent):
    def generate_roadmap(self, career, months=6):
        response = self.client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[{
                "role": "system",
                "content": f"Generate a {months}-month skill development roadmap."
            }, {
                "role": "user",
                "content": career
            }]
        )
        return response.choices[0].message.content
from .base_agent import BaseAgent

class JobAgent(BaseAgent):
    def get_jobs(self, career):
        job_db = {
            "Software Engineer": ["Frontend Developer", "Backend Engineer"],
            "Doctor": ["General Physician", "Surgeon"]
        }
        return job_db.get(career, ["Entry-level Position"])

    def get_market_info(self, career):
        try:
            response = self.client.chat.completions.create(
                model=self.models["default"],
                messages=[{
                    "role": "system",
                    "content": f"Provide current job market insights for {career}."
                }, {
                    "role": "user",
                    "content": career
                }],
                extra_headers=self.headers
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"⚠️ Error generating market info: {str(e)}")
            return self.get_default_market_info(career)

    def get_default_market_info(self, career):
        return f"Default market info for {career}: Job market data is currently unavailable. Please check back later."
from dotenv import load_dotenv
from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent
from utils.display import display_menu, show_header, show_career_details

def main():
    load_dotenv()
    show_header()
    
    career_agent = CareerAgent()
    skill_agent = SkillAgent()
    job_agent = JobAgent()

    # Step 1: Select category
    categories = career_agent.get_categories()
    cat_idx = display_menu(categories, "---Select a career category:")
    selected_category = categories[cat_idx]

    # Step 2: Select career
    careers = career_agent.get_career_options(selected_category)
    career_idx = display_menu([c.name for c in careers], "---Available careers:")
    selected_career = careers[career_idx]

    # Show career details
    show_career_details(selected_career)

    # Step 3: Show skills
    skills = skill_agent.get_skills(selected_career.name)
    print("\n🛠 Required Skills:")
    for skill in skills:
        print(f"- {skill}")

    # Step 4: Show roadmap
    roadmap = skill_agent.get_roadmap(selected_career.name)
    print("\n📅 6-Month Skill Development Roadmap:")
    print(roadmap)

    # Step 5: Show job roles
    jobs = job_agent.get_jobs(selected_career.name)
    print("\n💼 Potential Job Roles:")
    for job in jobs:
        print(f"- {job}")

    # Step 6: Market insights
    market_info = job_agent.get_market_info(selected_career.name)
    print("\n📊 Current Market Insights:")
    print(market_info)

if __name__ == "__main__":
    main()
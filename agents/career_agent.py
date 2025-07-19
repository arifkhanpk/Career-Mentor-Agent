from .base_agent import BaseAgent, CareerOption

class CareerAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.categories = {
            "Technology": [
                CareerOption("Software Engineer", "Design and develop software systems", "25% growth", "$120,000"),
                CareerOption("Data Scientist", "Analyze complex data to find insights", "36% growth", "$130,000"),
                CareerOption("Cybersecurity Analyst", "Protect systems from digital attacks", "33% growth", "$110,000"),
                CareerOption("AI/ML Engineer", "Develop intelligent systems and algorithms", "32% growth", "$140,000"),
                CareerOption("Cloud Architect", "Design cloud computing strategies", "28% growth", "$135,000")
            ],
            "Healthcare": [
                CareerOption("Doctor", "Diagnose and treat patients", "7% growth", "$208,000"),
                CareerOption("Nurse", "Provide patient care and support", "9% growth", "$77,000"),
                CareerOption("Pharmacist", "Dispense medications and advise patients", "6% growth", "$128,000"),
                CareerOption("Medical Researcher", "Conduct clinical trials and studies", "13% growth", "$95,000"),
                CareerOption("Physical Therapist", "Help patients recover mobility", "18% growth", "$91,000")
            ],
            "Business": [
                CareerOption("Financial Analyst", "Assess financial data and trends", "11% growth", "$96,000"),
                CareerOption("Marketing Manager", "Develop marketing strategies", "10% growth", "$135,000"),
                CareerOption("HR Specialist", "Manage employee relations", "8% growth", "$62,000"),
                CareerOption("Management Consultant", "Advise organizations on efficiency", "14% growth", "$93,000"),
                CareerOption("Entrepreneur", "Start and grow new businesses", "Varies", "$Varies")
            ],
            "Engineering": [
                CareerOption("Civil Engineer", "Design infrastructure projects", "8% growth", "$88,000"),
                CareerOption("Mechanical Engineer", "Design mechanical systems", "7% growth", "$90,000"),
                CareerOption("Electrical Engineer", "Develop electrical equipment", "9% growth", "$100,000"),
                CareerOption("Aerospace Engineer", "Design aircraft and spacecraft", "8% growth", "$122,000"),
                CareerOption("Biomedical Engineer", "Combine engineering and medicine", "10% growth", "$92,000")
            ],
            "Creative Arts": [
                CareerOption("Graphic Designer", "Create visual content", "5% growth", "$58,000"),
                CareerOption("Video Editor", "Edit and produce video content", "12% growth", "$63,000"),
                CareerOption("Game Developer", "Design and program video games", "16% growth", "$85,000"),
                CareerOption("Animator", "Create animated content", "8% growth", "$72,000"),
                CareerOption("UI/UX Designer", "Design user interfaces and experiences", "18% growth", "$95,000")
            ]
        }

    def get_categories(self):
        return list(self.categories.keys())

    def get_career_options(self, category):
        return self.categories.get(category, [])
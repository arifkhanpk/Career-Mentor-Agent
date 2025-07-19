from .base_agent import BaseAgent

class SkillAgent(BaseAgent):
    def get_skills(self, career):
        skills_db = {
            # Technology Skills
            "Software Engineer": ["Python/Java", "Data Structures", "System Design", "Version Control (Git)", "Agile Methodologies"],
            "Data Scientist": ["Python/R", "Machine Learning", "Data Visualization", "SQL", "Statistical Analysis"],
            "Cybersecurity Analyst": ["Network Security", "Ethical Hacking", "Risk Assessment", "Incident Response", "Security Tools"],
            "AI/ML Engineer": ["Python", "TensorFlow/PyTorch", "Neural Networks", "NLP", "Computer Vision"],
            "Cloud Architect": ["AWS/Azure", "Cloud Security", "Containerization", "Networking", "DevOps"],
            
            # Healthcare Skills
            "Doctor": ["Medical Knowledge", "Diagnosis", "Patient Care", "Communication", "Emergency Response"],
            "Nurse": ["Patient Assessment", "Medication Administration", "Wound Care", "Empathy", "Teamwork"],
            "Pharmacist": ["Medication Knowledge", "Dosage Calculation", "Drug Interactions", "Patient Counseling", "Inventory Management"],
            "Medical Researcher": ["Research Methodology", "Data Analysis", "Clinical Trials", "Scientific Writing", "Biostatistics"],
            "Physical Therapist": ["Anatomy Knowledge", "Rehabilitation Techniques", "Patient Evaluation", "Manual Therapy", "Exercise Prescription"],
            
            # Business Skills
            "Financial Analyst": ["Financial Modeling", "Excel", "Data Analysis", "Accounting", "Market Research"],
            "Marketing Manager": ["Digital Marketing", "SEO/SEM", "Content Strategy", "Market Research", "Brand Management"],
            "HR Specialist": ["Recruitment", "Employee Relations", "Labor Laws", "Conflict Resolution", "Training & Development"],
            "Management Consultant": ["Problem Solving", "Strategic Planning", "Data Analysis", "Communication", "Process Improvement"],
            "Entrepreneur": ["Business Planning", "Fundraising", "Marketing", "Financial Management", "Leadership"],
            
            # Engineering Skills
            "Civil Engineer": ["AutoCAD", "Structural Analysis", "Project Management", "Construction Methods", "Geotechnical Engineering"],
            "Mechanical Engineer": ["CAD/CAM", "Thermodynamics", "Material Science", "Robotics", "Fluid Mechanics"],
            "Electrical Engineer": ["Circuit Design", "Power Systems", "Control Systems", "Embedded Systems", "Signal Processing"],
            "Aerospace Engineer": ["Aerodynamics", "Flight Mechanics", "Propulsion Systems", "Avionics", "Structural Design"],
            "Biomedical Engineer": ["Medical Devices", "Biomechanics", "Tissue Engineering", "Medical Imaging", "Regulatory Affairs"],
            
            # Creative Arts Skills
            "Graphic Designer": ["Adobe Creative Suite", "Typography", "Color Theory", "Branding", "Layout Design"],
            "Video Editor": ["Premiere Pro", "After Effects", "Color Grading", "Sound Editing", "Storytelling"],
            "Game Developer": ["Unity/Unreal", "C#/C++", "3D Modeling", "Game Physics", "AI Programming"],
            "Animator": ["2D/3D Animation", "Character Design", "Rigging", "Motion Graphics", "Storyboarding"],
            "UI/UX Designer": ["Figma/Adobe XD", "User Research", "Wireframing", "Prototyping", "Interaction Design"]
        }
        return skills_db.get(career, ["Communication", "Problem-solving", "Teamwork", "Adaptability", "Time Management"])

    def get_roadmap(self, career):
        try:
            response = self.client.chat.completions.create(
                model=self.models["default"],
                messages=[{
                    "role": "system",
                    "content": f"Generate a detailed 6-month roadmap for becoming a {career} with monthly milestones."
                }, {
                    "role": "user",
                    "content": career
                }],
                extra_headers=self.headers
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"⚠️ Error generating roadmap: {str(e)}")
            return self.get_default_roadmap(career)

    def get_default_roadmap(self, career):
        return f"""Default 6-Month Roadmap for {career}:
        
Month 1-2: Learn core concepts and fundamentals
Month 3-4: Build practical projects and portfolio
Month 5: Network and connect with professionals
Month 6: Apply for jobs and prepare for interviews"""
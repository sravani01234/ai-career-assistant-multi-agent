
from agents.resume_agent import analyze_resume
from agents.job_match_agent import match_job
from agents.skill_gap_agent import find_skill_gaps
from agents.interview_agent import generate_questions

def route_query(query):

    q = query.lower()

    if "resume" in q:
        return analyze_resume(query)

    elif "job" in q or "match" in q:
        return match_job(query)

    elif "skill" in q:
        return find_skill_gaps(query)

    elif "interview" in q:
        return generate_questions(query)

    else:
        return "Please ask about resume analysis, job matching, skills, or interview preparation."

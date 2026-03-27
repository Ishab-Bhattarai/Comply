import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

def save_assessment(company_name, email, framework, answers, result):
data = {
"company_name": company_name,
"contact_email": email,
"framework": framework,
"answers": answers,
"result": result,
"status": "complete"
}
return supabase.table("assessments").insert(data).execute()

def get_assessments(company_name):
return supabase.table("assessments")\
.select("*")\
.eq("company_name", company_name)\
.execute()
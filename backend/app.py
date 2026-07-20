from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Develop Thought Compass', version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https://[a-z0-9-]+\.vercel\.app",
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)
PRODUCT = {"project_id": "80aca94c-9feb-4dce-b4e7-559bdbf39ed0", "product_name": "Develop Thought Compass", "idea": "Develop thought-reading headphones for individuals with severe motor disabilities, such as ALS patients, to enhance their communication capabilities", "problem": "Clinical and care-operations teams need a safer, faster way to turn fragmented patient and workflow signals into a reviewable next action. The opportunity should be tested through one repeatable decision workflow.", "elevator_pitch": "Develop Thought Compass helps clinical and care-operations teams turn scattered evidence into a human-approved next action and prove whether the workflow improves a measurable outcome.", "target_users": ["clinical and care-operations teams", "domain specialists", "a clinical operations or service-line leader"], "features": ["Structured case or workflow intake", "Evidence-backed recommendation with confidence and rationale", "Human approval and override with an audit trail", "Pilot dashboard for time, quality, and adoption outcomes"], "market_gap": "A narrow healthcare workflow that links evidence, a human approval, and a measurable outcome remains more defensible than another general AI chat surface."}

@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "generated-mvp-api"}

@app.get("/api/overview")
def overview() -> dict:
    return {
        "product_name": PRODUCT["product_name"],
        "pitch": PRODUCT["elevator_pitch"],
        "problem": PRODUCT["problem"],
        "target_users": PRODUCT["target_users"],
        "features": PRODUCT["features"],
        "demo_data": True,
    }

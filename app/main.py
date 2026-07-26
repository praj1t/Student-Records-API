from fastapi import FastAPI
from app.api.students import router as students_router
from app.api.subjects import router as subjects_router
from app.api.marks import router as marks_router
from app.api.audit_logs import router as audit_logs_router
from app.api.reports import router as reports_router
from fastapi_mcp import FastApiMCP

app = FastAPI()

app.include_router(students_router)
app.include_router(subjects_router)
app.include_router(marks_router)
app.include_router(audit_logs_router)
app.include_router(reports_router)

@app.get(
    "/",
    operation_id="healthcheck",
    summary="Check API health",
)
def healthcheck():
    return {"message": "Student records api is currently running"}

mcp = FastApiMCP(
    app,
    name="Student Records API",
    description="Tools for managing students, subjects, marks, reports, and audit logs.",
)

mcp.mount_http()

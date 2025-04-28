from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/certificate")
async def get_certificate(cert_id: str):
    """
    Get certificate PDF by ID
    
    Args:
        cert_id (str): The certificate ID to retrieve
        
    Returns:
        RedirectResponse: Redirects to the GitHub raw PDF URL
        
    Raises:
        HTTPException: If certificate ID not provided
    """
    if not cert_id:
        raise HTTPException(status_code=400, detail="No certificate ID provided")
    
    # Construct the GitHub raw URL
    github_url = f"https://raw.githubusercontent.com/YashDuhan/nptel-fake-certificate-assets-dir/5889b86a2ef6ed87bf96e8796cbfc87129165f8a/assets/{cert_id}.pdf"
    
    # Redirect to the GitHub raw URL
    response = RedirectResponse(url=github_url)
    response.headers["Content-Disposition"] = f"attachment; filename={cert_id}.pdf"
    return response
    

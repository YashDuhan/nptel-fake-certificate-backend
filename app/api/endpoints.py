from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import httpx

app = FastAPI()

@app.get("/certificate")
async def get_certificate(cert_id: str):
    """
    Get certificate PDF by ID
    
    Args:
        cert_id (str): The certificate ID to retrieve
        
    Returns:
        StreamingResponse: Streams the PDF file with the correct filename
        
    Raises:
        HTTPException: If certificate ID not provided or file not found
    """
    if not cert_id:
        raise HTTPException(status_code=400, detail="No certificate ID provided")
    
    github_url = f"https://raw.githubusercontent.com/YashDuhan/nptel-fake-certificate-assets-dir/ebdc56753722f1edc765e4c59e26d9e184e9f593/assets/{cert_id}.pdf"
    async with httpx.AsyncClient() as client:
        r = await client.get(github_url)
        if r.status_code != 200:
            raise HTTPException(status_code=404, detail="Certificate not found on GitHub")
        return StreamingResponse(
            iter([r.content]),
            media_type="application/pdf",
            headers={
                "Content-Disposition": f"attachment; filename={cert_id}.pdf"
            }
        )

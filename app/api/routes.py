from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
from pathlib import Path

router = APIRouter()

# Get the base directory - handle both local and Vercel environments
BASE_DIR = Path(__file__).resolve().parent.parent.parent
if "VERCEL" in os.environ:
    # In Vercel, we need to use the absolute path
    BASE_DIR = Path("/var/task")

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/certificate")
async def get_certificate(cert_id: str):
    """
    Get certificate PDF by ID
    
    Args:
        cert_id (str): The certificate ID to retrieve
        
    Returns:
        FileResponse: The PDF file if found
        
    Raises:
        HTTPException: If certificate not found or ID not provided
    """
    if not cert_id:
        raise HTTPException(status_code=400, detail="No certificate ID provided")
    
    try:
        # Construct the full path to the PDF file
        pdf_path = BASE_DIR / 'assets' / f'{cert_id}.pdf'
        
        if not pdf_path.exists():
            raise HTTPException(status_code=404, detail="Certificate not found")
        
        return FileResponse(
            pdf_path,
            filename=f"{cert_id}.pdf",
            media_type='application/pdf',
            headers={"Content-Disposition": f"attachment; filename={cert_id}.pdf"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
from pathlib import Path
import logging

router = APIRouter()

# Get the base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent
logger.debug(f"Base directory: {BASE_DIR}")

# Health check endpoint
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
    
    # Construct the full path to the PDF file
    pdf_path = BASE_DIR / 'assets' / f'{cert_id}.pdf'
    logger.debug(f"Looking for PDF at: {pdf_path}")
    logger.debug(f"Directory contents: {os.listdir(BASE_DIR / 'assets')}")
    
    if not pdf_path.exists():
        logger.error(f"File not found at: {pdf_path}")
        raise HTTPException(status_code=404, detail="Certificate not found")
    
    return FileResponse(pdf_path, filename=f"{cert_id}.pdf", media_type='application/pdf')


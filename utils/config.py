import os


class Config:
    
    BASE_URL = "https://www.lcell.bnu.edu.cn/"

    # Test Account
    USERNAME = "admin"
    PASSWORD = "admin123"

    # Browser
    BROWSER = "chrome"

    # Timeout
    IMPLICIT_WAIT = 5
    EXPLICIT_WAIT = 10

    # Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    REPORT_PATH = os.path.join(BASE_DIR, "reports")

  

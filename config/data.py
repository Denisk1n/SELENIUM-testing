import os
from dotenv import load_dotenv

load_dotenv()

class StaticData:
   
   LOGIN = os.getenv("LOGIN")
   PASSWORD = os.getenv("PASSWORD")
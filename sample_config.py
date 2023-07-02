import os

class Config(object):
  API_ID = os.environ.get("API_ID", None)  
  API_HASH = os.environ.get("API_HASH", None) 
  BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
  MONGO_URL = os.environ.get("MONGO_URL", None)
  DATABASE_NAME = os.environ.get("DATABASE_NAME") 
  BOT_USERNAME = os.environ.get("BOT_USERNAME") 
  UPDATE_CHNL = os.environ.get("UPDATE_CHNL")
  OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
  SUPPORT_GRP = os.environ.get("SUPPORT_GRP")
  BOT_NAME = os.environ.get("BOT_NAME")
  ADMINS = os.environ.get("ADMINS")
  START_IMG = os.environ.get("START_IMG")
  STKR = os.environ.get("STKR")
  

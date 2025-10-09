# create_tables.py
from app.database import Base, engine
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Creating tables (create_all)...")
    Base.metadata.create_all(bind=engine)
    logger.info("Done creating tables")

if __name__ == "__main__":
    main()

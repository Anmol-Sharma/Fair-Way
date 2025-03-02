import sqlite3
from contextlib import contextmanager
import logging
from resp_models import Feedback, Survey
from config import get_env_settings

env_settings = get_env_settings()
logger = logging.getLogger("fastapi")


@contextmanager
def get_db():
    """Context manager for database connections."""
    conn = sqlite3.connect(env_settings.feedback_db_path)
    try:
        yield conn
    finally:
        conn.close()


def init_db():
    """Initialize database tables."""
    with get_db() as conn:
        cursor = conn.cursor()
        # Create feedback table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(128) NOT NULL,
                email VARCHAR(128) NULL,
                feedback TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
        )
        # Create survey table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Survey (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                EASE_OF_USE VARCHAR(64) NOT NULL,
                OVERALL_RECOMMENDATION VARCHAR(64) NOT NULL,
                FAIR_FAMILIARITY VARCHAR(64) NOT NULL,
                PRIOR_TOOL_USAGE VARCHAR(64) NOT NULL,
                USED_OTHER_TOOLS VARCHAR(64),
                PROFESSIONAL_STATUS VARCHAR(128) NOT NULL,
                ACADEMIC_BG VARCHAR(128) NOT NULL,
                ACADEMIC_BG_OTHER VARCHAR(128),
                FAIR_USEFULL VARCHAR(128) NOT NULL,
                FAIR_RATING SHORT NOT NULL,
                USEFUL_ASPECTS VARCHAR(128) NOT NULL,
                FUTURE_USAGE VARCHAR(128) NOT NULL,
                COMMENTS TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
        )
        conn.commit()


def save_feedback(feedback: Feedback) -> bool:
    """Save user feedback to database."""
    with get_db() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)""",
                (feedback.name, feedback.email, feedback.feedback),
            )
            conn.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error saving feedback: {e}")
            return False


def save_survey(survey: Survey) -> bool:
    """Save user survey to database."""
    with get_db() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO Survey (EASE_OF_USE, OVERALL_RECOMMENDATION, FAIR_FAMILIARITY,
                PRIOR_TOOL_USAGE, USED_OTHER_TOOLS, PROFESSIONAL_STATUS, ACADEMIC_BG,
                ACADEMIC_BG_OTHER, FAIR_USEFULL, FAIR_RATING, USEFUL_ASPECTS,
                FUTURE_USAGE, COMMENTS) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    survey.easeOfUse,
                    survey.recommendation,
                    survey.fairFamiliarity,
                    survey.priorUsage,
                    survey.priorTools,
                    survey.professionalStatus,
                    survey.academicBG,
                    survey.academicBgOther,
                    survey.usefulness,
                    survey.fairRating,
                    survey.usefulAspects,
                    survey.futureUsage,
                    survey.comments,
                ),
            )
            conn.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error saving survey: {e}")
            return False

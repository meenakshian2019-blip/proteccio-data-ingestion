from apscheduler.schedulers.background import BackgroundScheduler
from modules.history import add_history


def scheduled_job():
    add_history(
        source="Scheduler",
        status="SUCCESS",
        details="Automatic scheduled ingestion executed"
    )


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        scheduled_job,
        "interval",
        minutes=30
    )
    scheduler.start()
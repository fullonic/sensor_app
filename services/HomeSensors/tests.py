"""Basic tests for main app and other services."""

from app.main import tasks


def test_tasks():
    """Tests if celery and broker are working properly."""
    return tasks.log.apply_async(["This is a test"], countdown=1)


if __name__ == "__main__":
    test_tasks()

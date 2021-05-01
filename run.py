from Crawler import app, scheduler
from Crawler.scheduled import scheduled_task


if __name__ == '__main__':
    scheduler.add_job(id='crawl youtube periodically', func=scheduled_task, trigger='interval', minutes=5)
    scheduler.start()
    app.run(debug=True, use_reloader=False)

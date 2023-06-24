from reactivex.scheduler.mainloop import PyGameScheduler
from reactivex.subject import Subject


class Rx:
    _scheduler: PyGameScheduler | None = None
    frame = Subject()
    keydown = Subject()
    keyup = Subject()

    @staticmethod
    def get_scheduler():
        return Rx._scheduler

    @staticmethod
    def set_scheduler(scheduler: PyGameScheduler):
        Rx._scheduler = scheduler

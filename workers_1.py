class Worker:

    def work(self):
        print("I'm working!!")


class Manager:

    def __init__(self):
        self.worker = None

    # def set_worker(self, worker):
    #     assert isinstance(worker, Worker), '`worker` must be of type {}'.format(Worker)

    def set_worker(self, worker):
        if "Worker" in [e.__name__ for e in worker.__class__.__mro__]:
            self.worker = worker
        else:
            raise AssertionError ('`worker` must be of type {}'.format(Worker))

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class SuperWorker(Worker):

    def work(self):
        print("I work very hard!!!")


class LazyWorker(Worker):

    def work(self):
        print("I don't work very hard!!!")


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

lazy_worker = LazyWorker()
try:
    manager.set_worker(lazy_worker)
    manager.manage ()
except AssertionError:
    print("manager fails to support super_worker....")


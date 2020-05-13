import panel as pn
import param
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


class FileEvent(param.Parameterized):
    path = param.String(constant=True)
    event_type = param.String(constant=True)


class FileObserverService(param.Parameterized):
    file_event = param.ClassSelector(class_=FileEvent)
    file_observers = param.List()

    def on_created(self, event):
        print(f"hey, {event.src_path} has been created!")
        self.file_event = FileEvent(path=event.src_path, event_type="created")

    def on_deleted(self, event):
        print(f"what the f**k! Someone deleted {event.src_path}!")
        self.file_event = FileEvent(path=event.src_path, event_type="deleted")

    def on_modified(self, event):
        print(f"hey buddy, {event.src_path} has been modified")
        self.file_event = FileEvent(path=event.src_path, event_type="modified")

    def on_moved(self, event):
        print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")
        self.file_event = FileEvent(path=event.src_path, event_type="moved")

    def stop(self):
        for file_observer in self.file_observers:
            file_observer.stop()

    def view(self):
        return pn.Param(self)


class FileObserver(param.Parameterized):
    path = param.String(constant=True)
    file_observer_service = param.ClassSelector(class_=FileObserverService, constant=True)

    def __init__(self, path, file_observer_service):
        super().__init__(path=path, file_observer_service=file_observer_service)

        patterns = "*"
        ignore_patterns = ""
        ignore_directories = False
        case_sensitive = True

        my_event_handler = PatternMatchingEventHandler(
            patterns, ignore_patterns, ignore_directories, case_sensitive
        )
        my_event_handler.on_created = file_observer_service.on_created
        my_event_handler.on_deleted = file_observer_service.on_deleted
        my_event_handler.on_modified = file_observer_service.on_modified
        my_event_handler.on_moved = file_observer_service.on_moved

        go_recursively = False
        self.observer = Observer()
        self.observer.schedule(my_event_handler, path, recursive=go_recursively)
        self.observer.start()

        if file_observer_service.file_observers is None:
            file_observer_service.file_observers = {}
        file_observer_service.file_observers.append(self)

    def stop(self):
        self.observer.stop()
        self.observer.join()


if __name__.startswith("__main__"):
    file_observer_service = FileObserverService()
    file_observer = FileObserver(path=".", file_observer_service=file_observer_service)

    file_observer_service.view().show()

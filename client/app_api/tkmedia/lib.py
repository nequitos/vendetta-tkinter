
import time


class Timer:
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0
        self.time_played = 0
        self.stop_flag = True

    def start(self):
        if self.stop_flag:
            self.start_time = time.time()
            self.stop_flag = False

    def stop(self):
        if self.stop_flag:
            pass
        else:
            self.time_played += time.time() - self.start_time
            self.stop_flag = True

    def clear(self):
        self.time_played = 0
        self.stop_time = 0
        self.stop_flag = True

    def get_time_played(self):
        if self.stop_flag:
            return self.time_played
        else:
            return self.time_played + (time.time() - self.start_time)

    def set_time(self, t):
        try:
            self.stop()
        except Exception as exc:
            pass

        self.time_played = t

        if not self.stop_flag:
            self.start()
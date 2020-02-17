import threading

class InjectionSlave():

    def __init__(self):
        print("constructor ")

    def initiate_fault(self,dns,fault):
        fault_thread = threading.Thread(target=self.orchastrate_injection , args=[dns,fault])
        fault_thread.start()

    def orchestrate_injection(self,dns,fault):
        target_info , fault_info = self.get_info()
        built_script = self.build_script()
        injection_logs = self.inject_script()
        self.send_result(injection_logs)

    def get_info(self,dns,fault):
        pass

    def build_script(self):
        pass

    def inject_script(self):
        pass

    def send_result(self):
        pass



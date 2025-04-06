from locust import HttpUser, TaskSet, task, between

class SimpleTasks(TaskSet):
    @task(1)
    def home(self):
        # Test the home route
        self.client.get("/")

    @task(2)
    def fast(self):
        # Test the fast route
        self.client.get("/fast")

    @task(3)
    def medium(self):
        # Test the medium route
        self.client.get("/medium")

    @task(4)
    def heavy(self):
        # Test the heavy route
        self.client.get("/heavy")

    @task(1)
    def echo(self):
        # Test the echo route
        payload = {"message": "Hello, Locust!"}
        self.client.post("/echo", json=payload)

class HeavyTasks(TaskSet):
    @task(1)
    def home(self):
        self.client.get("/")
        
    @task(1)
    def fast(self):
        self.client.get("/fast")
        self.client.get("/fast")
        self.client.get("/fast")
        
    @task(2)
    def medium(self):
        self.client.get("/medium")
        self.client.get("/medium")
        self.client.get("/medium")
        
    @task(10)
    def heavy(self):
        self.client.get("/heavy")
        self.client.get("/heavy")
        self.client.get("/heavy")
        
    @task(2)
    def echo(self):
        payload = {"message": "Hello, Locust! " * 10, 
                   "message2": "Locust, hello! " * 10}
        self.client.post("/echo", json=payload)

class SimpleUser(HttpUser):
    tasks = [SimpleTasks]
    wait_time = between(1, 5)  # Simulate a wait time between requests
    weight = 0.02

class HeavyUser(HttpUser):
    tasks = [HeavyTasks]
    wait_time = between(10, 20)
    weight = 0.98
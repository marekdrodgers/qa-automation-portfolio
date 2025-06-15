"""
locustfile.py

A basic load test script using Locust to simulate users hitting the /posts endpoint.
"""

from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    """
    Simulated user that performs GET and POST requests against the target host.
    """
    wait_time = between(1, 3)

    @task(3)  # Weight 3 times more likely to run
    def get_posts(self):
        """Send GET request to /posts."""
        self.client.get("/posts")

    @task(1)  # Weight less frequent POST request
    def create_post(self):
        """Send POST request to /posts."""
        self.client.post("/posts", json={
            "title": "foo",
            "body": "bar",
            "userId": 1
        })

from locust import HttpUser, task, between


class NodeRegistryUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def health_check(self):
        self.client.get("/health")

    @task(2)
    def list_nodes(self):
        self.client.get("/api/nodes")
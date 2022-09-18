from locust import FastHttpUser, task, between


class PerformanceTest(FastHttpUser):
    wait_time = between(1,2)

    @task(1)
    def testingPerformance(self):
        self.client.get('http://127.0.0.1:5000/Prediction_API/25;1;1;0;0;0;0;0;84')



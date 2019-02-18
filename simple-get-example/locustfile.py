from locust import HttpLocust, TaskSet, task
import sys
import urllib
import random
import time

class UserBehavior(TaskSet):
        
    @task(1)
    def email_benchmark(self):
        resp = self.client.get("/", name="nginx-tuning-best-performance")
        print(resp.text)
        
class WebsiteUser(HttpLocust):    
    task_set = UserBehavior
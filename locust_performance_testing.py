
# flake8: noqa
"""md
README
CMD
```
locust -f locust_performance_testing.py -u 100 -r 100 -t 1m
```

This **Locust** command runs a performance test with the following parameters:

- **`-f locust_performance_testing.py`** → Specifies the Locust test script.  
- **`-u 100`** → Simulates **100 concurrent users**.  
- **`-r 100`** → Spawns **100 users per second** until reaching 100 users.  
- **`-t 1m`** → Runs the test for **1 minute**.  

It helps analyze how well your system handles 100 users under load for 1 minute. 🚀
"""
import random
import logging
from locust import task, constant
from locust.contrib.fasthttp import FastHttpUser


log = logging.getLogger("rest-api-short-urls")
todo_ids = range(1, 1000)


class LocustClient(FastHttpUser):
    wait_time = constant(0)
    host = "http://127.0.0.1:8000/todo"


    def __init__(self, environment):
        """ Class constructor."""
        super().__init__(environment)


    @task
    def test_get_todos(self):

        try:
            url = random.choice(todo_ids)
            with self.client.get(f'/{url}', name='get todo id') as resp_of_api:
                if resp_of_api.status_code == 200:
                    log.info("API call resulted in success.")

                else:
                    log.error("API call resulted in failed.")
             
        except Exception as e:
            log.error(f"Exception occurred! details are {e}")
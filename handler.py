#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import requests
class OperateDagobah(object):
    def __init__ (self, passwd):
        self.delete_job_url = "http://localhost:9000/api/delete_job"
        self.edit_job_url = "http://localhost:9000/api/edit_job"
        self.delete_task_url = "http://localhost:9000/api/delete_task"
        self.edit_task_url = "http://localhost:9000/api/edit_task"
        self.login_url = "http://localhost:9000/do-login"
        self.password = passwd

    def register(self):
        s.post(delete_url, {}

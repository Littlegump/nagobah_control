#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import pymongo
import pprint

class MongoDBHelper(object):
    def __init__(self):
        pass

    def jobs_iter(self):
        client = pymongo.MongoClient('mongodb://localhost', 27017)
        db = client['dagobah']
        collect = db['dagobah']
        for item in collect.find():
            return item['jobs']

    def present_all_job(self):
        iter_ = self.jobs_iter()
        print "Total:", len(iter_), "jobs included"
        print "<name>", "\t\t", "<num of tasks>", "\t\t", "<notes>"

        for jobs in iter_:
            print jobs['name'], "\t",
            print len(jobs['tasks']), "\t\t\t",
            print jobs['notes'].strip(), "\t"

    def present_a_job(self, job_name):
        pp = pprint.PrettyPrinter(indent=4)
        iter_ = self.jobs_iter()
        for jobs in iter_:
            if jobs['name'] == job_name:
                for key in ['job_id', 'parent_id']:
                    del jobs[key]
                # 这里使用pprint
                pp.pprint(jobs)

    def present_a_task(self, job_name, task_name):
        pp = pprint.PrettyPrinter(indent=4)
        iter_ = self.jobs_iter()
        for jobs in iter_:
            if jobs['name'] == job_name:
                print "jobname:", job_name
                for j in jobs['tasks']:
                    if j['name'] == task_name:
                        pp.pprint(j)

    def delete_all():
    def delete_a_job()






"""Send content representing a completed IDIS job to the test receiver
"""

import json
import requests

content = {'job_id': 1,
           'date': '2018-09-17T14:49:34',
           'user_name': 'testuser',
           'status': 'DONE',
           'error': None,
           'description': 'Mock job for testing webhooks',
           'project_name': 'test-project',
           'priority': 0,
           'files_downloaded': 100,
           'files_processed': 90,
           'destination_id': None,
           'destination_name': None,
           'destination_path': '\\\\servername\\sharename\\folder\\Incoming',
           'destination_network': None,
           'destination_status': 'NEW',
           'destination_type': 'PATH',
           'source_id': None,
           'source_instance_id': None,
           'source_status': 'NEW',
           'source_type': 'WADO',
           'source_anonymizedpatientid': 'patient_1',
           'source_anonymizedpatientname': 'patient-1',
           'source_anonymizedaccessionnumber': '123.456.78.9123',
           'source_anonymizedstudyid': '123567.12345678',
           'source_pims_keyfile_id': '123',
           'source_name': None,
           'source_path': None,
           'source_protocol': None,
           'source_subject': None,
           'source_ignore_opt_out': None,
           'source_ignore_opt_out_reason': None}


if __name__ == '__main__':
    url = "http://127.0.0.1:8080/webhook"
    print(f"Sending POST content to {url}")
    requests.post(url=url, json=content)
    print("Done")

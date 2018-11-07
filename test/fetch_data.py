from typing import Any

import jenkins
import json


def dump_data(file_name: str, data: Any) -> None:
    print(f"Writing: {file_name}")

    with open(file_name, "wt", encoding="utf-8") as f:
        f.write(json.dumps(data,
                           sort_keys=True,
                           indent=2,
                           separators=(',', ': ')))


server = jenkins.Jenkins("http://localhost:8080",
                         username="test",
                         password="test")


# result = server.get_job_info("jenkins-demo", depth="2")
result = server.get_all_jobs()

dump_data("model/remote/jenkins/all_jobs.json", result)

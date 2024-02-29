import subprocess
import json
import googleapiclient.discovery

# Run gcloud command to fetch compute instance information

def list_vm():
    output = subprocess.run(['gcloud', 'asset', 'search-all-resources', '--scope=projects/practical-proxy-413809', '--asset-types=compute.googleapis.com/Instance', '--read-mask=name,project,location,state'], capture_output=True, text=True)
    # Parse the output
    instances = []
    for item in output.stdout.strip().split('---\n'):
        if item.strip():
            instance = {}
            for line in item.strip().split('\n'):
                key, value = line.split(': ', 1)
                instance[key] = value
            instances.append(instance)

    return instances

def stop_vm(proj,location,vmname):
    compute = googleapiclient.discovery.build('compute', 'v1')
    result = compute.instances().stop(project=proj, zone=location, instance=vmname).execute()
    return result

if __name__=="__main__":
    instances = list_vm()
    for i in instances:
        if i["state"]=="RUNNING":
            string = i["name"]
            split_string = string.split("/")
            project_id = split_string[4]
            instance_id = split_string[-1]

            stop_vm(project_id,i["location"],instance_id)
            #print(project_id,instance_id)

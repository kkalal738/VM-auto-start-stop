import subprocess
import json
import googleapiclient.discovery

# Run gcloud command to fetch compute instance information

def list_vm():
    output = subprocess.run(['gcloud', 'asset', 'search-all-resources', '--scope=projects/'+proj, '--asset-types=compute.googleapis.com/Instance', '--read-mask=name,project,location,state','--query=labels.autostartstop:yes'], capture_output=True, text=True)
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

def start_vm(proj,location,vmname):
    compute = googleapiclient.discovery.build('compute', 'v1')
    result = compute.instances().start(project=proj, zone=location, instance=vmname).execute()
    print(vmname , "VM is started !!")
    return result


if __name__=="__main__":
    
    #projects=["kartik-test-project-415817","practical-proxy-413809"]
    for i in instances:
        if i["state"]=="TERMINATED":
            string = i["name"]
            split_string = string.split("/")
            project_id = split_string[4]
            instance_id = split_string[-1]

            start_vm(project_id,i["location"],instance_id)
                #print(project_id,instance_id)


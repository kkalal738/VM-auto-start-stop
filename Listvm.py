
import subprocess

def list_vm():
    proj = "your-project-id"
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

    # Print the instances
    for instance in instances:
        print(instance)

# Run the function
list_vm()

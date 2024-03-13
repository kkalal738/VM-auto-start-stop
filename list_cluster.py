
import subprocess
import json

def list_vm():
    #proj = "your-project-id"
    output = subprocess.run(['gcloud', 'asset', 'search-all-resources', '--scope=projects/kartik-test-project-415817', '--asset-types=container.googleapis.com/Cluster', '--read-mask=name,project,location,state' ,'--query=labels.autostartstop:yes'], capture_output=True, text=True)
    
    # Check if the command was successful
    if output.returncode != 0:
        print("Error executing command:")
        print(output.stderr)
        return
    
    # Parse the output
    clusters = []
    for item in output.stdout.strip().split('---\n'):
        if item.strip():
            cluster = {}
            for line in item.strip().split('\n'):
                key, value = line.split(': ', 1)
                cluster[key] = value
            clusters.append(cluster)

    # Print the instances
    for cluster in clusters:
        print(cluster)

# Run the function
list_vm()

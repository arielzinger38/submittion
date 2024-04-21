Submittion for SignalPet 

Compromises:
State Management:
For simplicity, we'll store images and queue data in-memory within each respective service.
This compromise sacrifices resilience for simplicity and time efficiency.
Single Service for Producer and Consumer:
To simplify the setup, both producing and consuming of queue tasks will be handled within the same service and deployment.
This simplifies the architecture but might not be ideal for scalability and separation of concerns in a real-world scenario.
Basic Web Server Implementation:
Due to time constraints, we'll implement a basic Python web server for the API endpoint.
This sacrifices features and robustness for speed of implementation.

ive chosen flask - as the web server 
Redis - as the queue manager 
and python for implementation

architecture - there are 3 images each one for its own service all tagged latest and pushed to docker hub
there are 4 manifests that consist of storage claim , single job queue , and 2 deployments for the 2 services one for the webserver and one for the consumer service 
both deployed on the same cluster 

This cluster Consists of 3 working nodes deployed with minikube using docker images pulled from dockerhub
built tagged and pushed images are publicly pulled from dockerhub e.g: arielzinger12/web-server-image:latest
kubernetes cluster installed using kubeadm/minikube 
to run locally:
install docker client
install kubeadm/minikube 
download the files needed (submittion directory) 
git clone https://github.com/arielzinger38/submittion.git 
verify cloned repo downloaded
run and verify docker client and dockerhub connection valid (docker login)
run minikube start
apply all manifest files there are 4 e.g: kubectl apply -f web-server-deplyment.yaml
verify all pods are running (kubectl get pods -o wide)

did only half of the bonus the entire state of the system is resilient to restarts by having a persistent storage
didnt get to Helm and terraform could not decide on supplier and usage

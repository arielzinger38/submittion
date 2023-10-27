# submittion
Devops task DCOYA
-----------------

Dependencies:<br />
 ```
  Docker
  minikube
  kubectl
  Python
  Selenium
```

Login Pull & Build Docker Image if needed:
```
   docker login <your-registry> 
   docker pull arielzinger12/ariel-image-1:latest
   docker build -t arielzinger12/ariel-image-1:latest .
```
  
(you can also just login to docker hub if you dont want to build the image locally in order for the kubernetes to pull the image from the repo)

Deploy Kubernetes Application:
 ```
 pull from git
  install minikube - https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
  minikube start
  kubectl apply -f deployment.yaml
  kubectl apply -f service.yaml
  minikube service submittion-service (keep terminal open)
  minikube tunnel (keep terminal open)
```

Access: 
```
you can NOW access the page by http://localhost no need for port
```

Run Selenium Tests:
```
The tests are running using selenium on Mozilla-FireFox

Install Python dependencies and selenium + Mozilla-FireFox Browser (if needed!!!)
  python tesenium.py
```

WARNING!!!
the last test checks computer time presented in the HTML so the format may vary from device to device. the last test might fail because of that

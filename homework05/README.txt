********************************* HOMEWORK 5 **********************************
                              Gabrielle Toutin
                                   gt6422
*******************************************************************************


--- A ---

1. Include the yaml file used and the command issued to create the pod.
   - yaml file: gctoutin-hw5-pod.yml
   - command: kubectl create -f gctoutin-hw5-pod.yml

2. Issue a command to get the pod using an appropriate selector. Copy and paste the command used and the output.
   - command: kubectl get pods --selector "greeting=personalized"
   - output: 
NAME        READY   STATUS    RESTARTS   AGE
hw5-hello   1/1     Running   0          5m23s



3. Check the logs of the pod. What is the output? Is that what you expected?

[gctoutin@isp02 homework05]$ kubectl logs hw5-hello
Hello,

Not what I expected, there is no name.



4. Delete the pod. What command did you use?

[gctoutin@isp02 homework05]$ kubectl delete pods hw5-hello
pod "hw5-hello" deleted



--- B ---

1. Include the yaml file used and the command issued to create the pod.
   - yaml file: gctoutin-hw5-pod-b.yml
   - command: kubectl create -f gctoutin-hw5-pod-b.yml



2. Check the logs of the pod. What is the output? Copy and paste the command used and the output.

[gctoutin@isp02 homework05]$ kubectl logs hw5-hello
Hello, Gabrielle



3. Delete the pod. What command did you use?

[gctoutin@isp02 homework05]$ kubectl delete pods hw5-hello
pod "hw5-hello" deleted



--- C ---

1. Include the yaml file used to create a deployment with 3 replica pods, and include the command issued to create the deployment.
- yaml file: gctoutin-hw5-pod-c.yml
-command: kubectl create -f gctoutin-hw5-pod-c.yml



2. First, use kubectl to get all the pods in the deployment and their IP address. Copy and paste the command used and the output.

[gctoutin@isp02 homework05]$ kubectl get pods -o wide --selector "greeting=personalized"
NAME                                    READY   STATUS             RESTARTS   AGE     IP             NODE   NOMINATED NODE   READINESS GATES
hw5-hello-deployment-5957574cbd-7dzfk   0/1     CrashLoopBackOff   4          2m32s   10.244.5.121   c04    <none>           <none>
hw5-hello-deployment-5957574cbd-gvd47   0/1     CrashLoopBackOff   4          114s    10.244.3.118   c01    <none>           <none>
hw5-hello-deployment-5957574cbd-ngfxq   0/1     CrashLoopBackOff   4          2m13s   10.244.7.114   c05    <none>           <none>



3. Now, check the logs associated with each pod in the deployment. Does it match what you got in 2? Copy and paste the commands and the output.

[gctoutin@isp02 homework05]$ kubectl logs --selector "greeting=personalized"
Hello, Gabrielle from IP 10.244.5.121
Hello, Gabrielle from IP 10.244.3.118
Hello, Gabrielle from IP 10.244.7.114


Yes it does match the IP addresses from 2.

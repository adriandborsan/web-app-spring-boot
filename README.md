# web-app-spring-boot
Web app using spring boot

## Introduction

A full stack complete web application that has 2 backends using spring boot and java and 2 frontends using angular and typescript, one for the client and one the admin.

## Setup Locally

1. Create a directory named web-app-spring-boot
    ```
    mkdir web-app-spring-boot
    ```
2. Go into it
   ```
   cd web-app-spring-boot
   ```
3. Clone the main branch of the repository
   ```
   git clone --single-branch --branch main git@github.com:adriandborsan/web-app-spring-boot.git main
   ```
4. Run the `clone_application.py` script by following the below command:
    ```
    python3 clone_application.py
    ```

Alternatively you can use the command from step 3 to only clone a specific microservice branch. the list of branches that contain microservices projects are inside **config.json**


## Deployment

In order to deploy the application from a single point of entry, the `deploy_application.py` script needs to be executed. 
Run the script with the following command:
```
python3 deploy_application.py
```

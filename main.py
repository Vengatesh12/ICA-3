
To complete your assignment effectively, here’s a structured plan detailing the steps involved:



yaml
Copy code
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-proxy
spec:
  replicas: 1
  selector:
    matchLabels:
      id: <your-college-id>
      app: nginx-proxy
      env: dev
  template:
    metadata:
      labels:
        id: <your-college-id>
        app: nginx-proxy
        env: dev
    spec:
      containers:
      - name: nginx-proxy
        image: nginx:latest
        volumeMounts:
          - name: nginx-config
            mountPath: /etc/nginx/nginx.conf
            subPath: nginx.conf
Example nginx-proxy/templates/service.yaml:

yaml
Copy code
apiVersion: v1
kind: Service
metadata:
  name: nginx-proxy-service
spec:
  selector:
    app: nginx-proxy
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer
WordPress App Helm Chart:

Use the official wordpress:latest Docker image.
Deployment: Set up a wordpress deployment.
Service: The service should not be exposed externally (ClusterIP).
ConfigMap: Store WordPress-related configuration such as wp-config.php (optional).
Secrets: Store sensitive values like database password.
Example wordpress-app/templates/deployment.yaml:

yaml
Copy code
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress
spec:
  replicas: 1
  selector:
    matchLabels:
      id: <your-college-id>
      app: wordpress
      env: dev
  template:
    metadata:
      labels:
        id: <your-college-id>
        app: wordpress
        env: dev
    spec:
      containers:
      - name: wordpress
        image: wordpress:latest
        env:
          - name: WORDPRESS_DB_HOST
            value: "mariadb-service"
          - name: WORDPRESS_DB_NAME
            value: "wordpress"
          - name: WORDPRESS_DB_USER
            valueFrom:
              secretKeyRef:
                name: wordpress-db-credentials
                key: username
          - name: WORDPRESS_DB_PASSWORD
            valueFrom:
              secretKeyRef:
                name: wordpress-db-credentials
                key: password
Example wordpress-app/templates/service.yaml:

yaml
Copy code
apiVersion: v1
kind: Service
metadata:
  name: wordpress-service
spec:
  selector:
    app: wordpress
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: ClusterIP
Database Helm Chart:

Use the official mariadb:10.6.4-focal Docker image.
Deployment: Define the MariaDB deployment.
Service: The service should not be exposed externally (ClusterIP).
Secrets: Store database credentials (username, password).
Example database/templates/deployment.yaml:

yaml
Copy code
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mariadb
spec:
  replicas: 1
  selector:
    matchLabels:
      id: <your-college-id>
      app: mariadb
      env: dev
  template:
    metadata:
      labels:
        id: <your-college-id>
        app: mariadb
        env: dev
    spec:
      containers:
      - name: mariadb
        image: mariadb:10.6.4-focal
        env:
          - name: MYSQL_ROOT_PASSWORD
            valueFrom:
              secretKeyRef:
                name: mariadb-credentials
                key: root-password
Example database/templates/service.yaml:

yaml
Copy code
apiVersion: v1
kind: Service
metadata:
  name: mariadb-service
spec:
  selector:
    app: mariadb
  ports:
    - protocol: TCP
      port: 3306
      targetPort: 3306
  type: ClusterIP
Step 3: GitOps with Argo CD
Install Argo CD:

Install Argo CD in your Kubernetes cluster to manage continuous deployment.
Follow Argo CD installation documentation.
Connect GitHub Repository to Argo CD:

In Argo CD, connect the repository containing your Helm charts.
Create an application that points to the directory in the repository containing your Helm charts for nginx-proxy, wordpress-app, and database.
Automate Deployment:

Define the Helm chart in Argo CD.
Set the namespace for each component (nginx-proxy, wordpress, and database).
Step 4: Create Dockerfiles for Custom Components
If you need to create custom images for any component, here’s how you can set up the Dockerfiles:

Nginx Dockerfile (if you want to customize Nginx configuration):

dockerfile
Copy code
FROM nginx:latest
COPY nginx.conf /etc/nginx/nginx.conf
WordPress Dockerfile:

dockerfile
Copy code
FROM wordpress:latest
# Any additional configuration or plugins
Database Dockerfile:

dockerfile
Copy code
FROM mariadb:10.6.4-focal
# Additional configurations or setup if needed
Step 5: Test and Verify the Deployment
Commit changes to GitHub:

Push all your Helm charts and Kubernetes manifests to the GitHub repository.
Verify Deployment with Argo CD:

After pushing to GitHub, Argo CD should automatically detect changes and apply the new configuration.
Check the Argo CD dashboard to verify that all components are deployed successfully.
Demonstrate Automatic Deployment:

Modify one of your deployments (e.g., change the image tag of the WordPress container) and commit it to GitHub.
Verify that Argo CD automatically updates the Kubernetes resources with the new configuration.
Step 6: Documentation & Submission
Write a Word Document:
Include the steps you followed to complete the assignment.
Provide screenshots to demonstrate each phase of your setup.
Highlight any challenges faced and how you solved them.
Mention any improvements or learning outcomes.
Additional Considerations:
Security: Make sure to encrypt sensitive data before pushing to GitHub (e.g., using Kubernetes secrets or tools like Sealed Secrets).
Cluster Setup: Avoid using Minikube or Docker Desktop; use a managed Kubernetes service (like AWS EKS, Google GKE, or Azure AKS) for better scalability and performance.
By following these steps, you will not only meet the requirements of the assignment but also gain hands-on experience with Kubernetes, Helm, and GitOps practices.
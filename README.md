# fetch-rewards Exercise

Program to check the health of a set of HTTP endpoints

<br>


<br>

# Table of Contents
1. [Getting Started](#getting-started)
    * [Using Docker](#running-docker)
    * [Using python locally](#running-locally)
2. [Time Complexity](time-complexity)
3. [Space Complexity](space-complexity)
2. [Scenarios to deploy](#scenarios-to-deploy)
    * [AWS Deployment Scenario](#aws-deployment-scenario)
    * [Notification requirements](#notification-requirements)

<br>

<a name="get"></a>

## Getting Started

These instructions will guide you on how to run the Python script in a Docker container.

<a name="usage"></a>

###   1. Add input file 
    Add required input file containing all the urls in the main directory as "input.yaml"

###   2. Build the Docker Image

&nbsp; Navigate to the project directory and run the following command to build the Docker image:


    docker build -t fetch .

###   3. Run the Docker Container or run locally
Once the image is built, run the Docker container:

### Running Docker
```bash
docker run fetch
```
### Running locally

```bash
python app.py
```

<br>



### Time Complexity:

1. Reading YAML file and processing entries in main function:

    The time complexity for reading the YAML file and processing each entry is O(n), where n is the number of entries in the YAML file.

2. HTTP requests in calculate_latency function:

    The time complexity of making an HTTP request is generally O(1) for simple requests. However, the actual time may vary depending on the response time from the server.

3. Updating url_dict in main function:

    The time complexity of updating the url_dict using Counter.update is O(k), where k is the number of latencies for a specific URL in a single entry.

4. Printing availability in print_availability function:

    The time complexity for printing the availability is O(m), where m is the number of unique URLs.

5. Overall, the time complexity is dominated by the number of entries in the YAML file and the number of unique URLs.

<br>

### Space Complexity:
1. url_dict dictionary:

    The space complexity of the url_dict is O(m * k), where m is the number of unique URLs, and k is the average number of latencies for a specific URL.

2. Local variables and data structures:

    The space complexity of other local variables and data structures is O(1) as they don't depend on the input size.


<br>


## Scenarios to deploy  


### AWS Deployment Scenario
When deploying a health check service to AWS with SNS (Simple Notification Service) for notifications, there are several considerations and steps to follow. Here's a guide with information on how to set up such a deployment:

1. Architecture Overview:
AWS ECS (Elastic Container Service) can be used to deploy the health check service in a Docker container.
Implement a health check mechanism within the service to periodically check the URLs.
Integrate AWS SNS for sending notifications when health check failures occur.
2. AWS Resources:
ECS Cluster:
Create an ECS cluster to manage the deployment of containers.
Task Definition:
Define an ECS task definition specifying the Docker image, resource requirements, and environment variables.
Service:
Create an ECS service to run and maintain a specified number of task instances.
To deploy in Kubernetes use EKS and run it as sidecar to the main application
3. Integration with AWS SNS:
Create SNS Topic:
Create an SNS topic to which notifications will be published.
Subscribe Endpoints:
Subscribe relevant endpoints (email addresses, SMS numbers, etc.) to the SNS topic.
4. Service Configuration:
Environment Variables:
Set environment variables in the ECS task definition for configuring the health check service.
SNS_TOPIC_ARN: ARN of the SNS topic.
AWS_REGION: AWS region for the SNS topic.
Other environment-specific variables.
5. Health Check Service Implementation:
Monitoring URLs:
Implement logic within the health check service to periodically monitor the health of specified URLs.
SNS Notification Logic:
When a health check fails, publish a notification to the configured SNS topic.
Include relevant details such as the affected URL, error messages, and timestamps.
6. Notification Content:
Email Notifications:
For email notifications, include details in the email body or subject line.
SMS Notifications:
Keep SMS notifications concise due to character limitations.
Payload Format:
Use a standardized payload format for all notification types.
For Slack notification:
For Slack notifications, include details similar to email
7. Monitoring and Logging:
CloudWatch Metrics:
Set up CloudWatch metrics to monitor ECS service metrics, such as CPU utilization and task count.
Logging:
Implement logging within the health check service for detailed diagnostic information.
8. Security Considerations:
IAM Roles:
Create IAM roles with the necessary permissions for ECS tasks to publish to the SNS topic.
Secure Configuration:
Avoid hardcoding sensitive information in the code. Use AWS Secrets Manager or Parameter Store for secure configuration storage.
9. Testing:
End-to-End Testing:
Perform end-to-end testing to ensure that health checks trigger notifications correctly.
Simulate Failures:
Simulate URL failures to verify that notifications are sent as expected.
10. Documentation:
Deployment Documentation:
Maintain comprehensive documentation for deploying the health check service and configuring SNS notifications.
Troubleshooting Guide:
Include a troubleshooting guide for common issues and resolutions.
11. Cost Management:
Optimize Resource Usage:
Regularly review and optimize ECS resource usage to manage costs efficiently.
12. Alerting Policies:
CloudWatch Alarms:
Set up CloudWatch alarms for key ECS metrics to proactively alert on potential issues.
13. Scaling Considerations:
ECS Auto Scaling:
Consider implementing ECS Auto Scaling based on metrics like CPU or memory utilization.
14. Backup and Recovery:
ECS State Persistence:
Ensure data persistence and implement backup and recovery mechanisms if the health check service has stateful components.
15. Continuous Improvement:
Feedback Loop:
Establish a feedback loop to continuously improve the health check service based on incidents and feedback.
![Architecture](./files/Screenshot%202023-12-03%20at%2012.07.27%20PM.png)
<br>

### Notification requirements

Notifying developers when health checks are down is crucial for maintaining the reliability and availability of a system. Here are some considerations and information to include in notifications:

1. Notification Content:
a. Error Details:
Provide information about the error or issue encountered during the health check.
Include error codes, error messages, or a brief description of the problem.
b. Affected URL:
Clearly mention the URL or endpoint that is experiencing issues.
Include the environment (e.g., production, staging) to help identify the context.
c. Timestamp:
Include the timestamp of when the health check failed.
Use a standardized timestamp format for consistency.
d. Duration of Downtime:
Indicate how long the health check has been failing.
Include a duration that helps developers understand the impact.
2. Communication Channels:
a. Email:
Send detailed emails with the information mentioned above.
Use a subject line that clearly indicates a health check failure.
b. Slack or Chat Integration:
Integrate with communication channels like Slack for real-time alerts.
Post notifications to a dedicated channel for infrastructure or health monitoring.
c. SMS Alerts:
Consider sending critical alerts via SMS for immediate attention.
Use SMS selectively for high-priority issues to avoid notification fatigue.
3. Alert Severity Levels:
a. Critical Alerts:
Use critical alerts for severe issues affecting the entire system or critical functionalities.
Require immediate attention and intervention.
b. Warning Alerts:
Send warning alerts for issues that might impact certain functionalities but don't pose an immediate threat.
Allow developers to investigate and address during regular working hours.
4. Instructions for Developers:
a. Investigation Steps:
Provide steps or guidance on how developers can investigate the issue further.
Include relevant log locations, debugging tools, or monitoring dashboards.
b. Resolution Steps:
If known, suggest steps developers can take to resolve the issue.
Include links to documentation or runbooks for troubleshooting.
5. Escalation Policy:
a. Define Roles and Responsibilities:
Clearly define who is responsible for addressing health check failures.
Specify escalation paths if the primary contact is unavailable.
b. On-Call Rotation:
Implement an on-call rotation for developers to ensure 24/7 coverage.
Include contact details for the on-call developer.
6. Integration with Monitoring Tools:
    a. Link to Monitoring Dashboards:
        Include links to relevant monitoring dashboards or tools.
        Developers can quickly access additional information for troubleshooting.
7. Continuous Improvement:
    a. Post-Incident Review:
        Conduct post-incident reviews to analyze the root cause of health check failures.
        Use findings to improve the monitoring system and prevent future issues.


Example Notification:

```
    Subject: [CRITICAL] Health Check Failure - Production Environment

    Dear [Team/Developer Name],

    The health check for the URL [Affected URL] in the production environment has failed.

    Error Details: [Provide detailed error information]
    Timestamp: [Include timestamp in UTC]
    Duration of Downtime: [Specify duration]
    Action Required:

    Investigation Steps: [Provide steps for investigation]
    Resolution Steps: [If known, suggest steps for resolution]
    Monitoring Dashboard: [Include a link to the monitoring dashboard]

    For immediate attention, please contact the on-call developer [On-Call Developer Name] at [Contact Details].

    Thank you,
    [Your Team or System Name]
```

<br>

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
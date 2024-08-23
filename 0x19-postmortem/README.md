ssue Summary
Duration: August 22, 2024, 2:00 PM to 3:30 PM (UTC)
Impact: The outage affected the web servers hosting the AirBnB clone project, rendering the site inaccessible to approximately 80% of users. Users could not access the site, leading to lost bookings and a significant drop in traffic during the outage.
Root Cause: The root cause was a configuration issue in the Nginx server, which was not optimized to handle a sudden spike in traffic. This led to server overload and ultimately caused the service to become unresponsive.
Timeline
2:00 PM: The issue was detected by the monitoring system, which reported a high number of 502 Bad Gateway errors.
2:05 PM: An engineer began investigating the issue, initially suspecting a problem with the application code.
2:15 PM: The team investigated the database for any potential bottlenecks, but no issues were found.
2:30 PM: Misleading path: The investigation shifted to examining recent code deployments for potential bugs, but no relevant issues were identified.
2:45 PM: The incident was escalated to the DevOps team for further analysis.
3:00 PM: The DevOps team identified the root cause as an Nginx server configuration that failed to handle the high traffic volume.
3:15 PM: The Nginx server configuration was optimized, and additional server resources were allocated to handle the load.
3:30 PM: The service was fully restored, and normal traffic levels were observed.
Root Cause and Resolution
Root Cause: The Nginx server was configured with insufficient worker processes and connection limits, which led to server overload when traffic spiked. The server was unable to process incoming requests efficiently, resulting in 502 errors and making the service unavailable to users.
Resolution: The issue was resolved by adjusting the Nginx configuration to increase the number of worker processes and connection limits. Additionally, auto-scaling was configured to automatically allocate more resources during traffic spikes. These changes allowed the server to handle the increased traffic load, restoring normal operation.
Corrective and Preventative Measures
To prevent this issue from reoccurring, the following measures will be implemented:
Optimize Nginx Configuration: Review and optimize the Nginx configuration for all servers, ensuring they are capable of handling peak traffic loads.
Implement Auto-Scaling: Set up auto-scaling for web servers to automatically allocate additional resources when traffic spikes are detected.
Enhanced Monitoring: Add more granular monitoring for server load and response times to detect potential overload conditions before they impact users.
Load Testing: Conduct regular load testing to simulate traffic spikes and ensure the infrastructure can handle high demand.
Review Incident Response Protocols: Update the incident response protocols to include a checklist for investigating server configuration issues during similar outages.
These steps will help ensure that the web servers are better prepared to handle traffic spikes, minimizing the risk of future outages and improving overall reliability.



# Tech Assessment

## Table of Contents
- Section 1: Data Pipelines
- Section 2:Databases
- Section 3: System Design
- Section 4: Charts & APIs
- Section 5: Machine Learning


## Section 3: System Design

### Things to clarify
- 

### Assumptions Checklist:
- [ ] AWS is the cloud service provider
- [ ]  Users are all based in Singapore
- [ ] Image processing is meant by photoshop, filtering, or photo enhacement services
- [ ] Kafka stream is an external entity and only interacts with the cloud environment is uploading images to the cloud environment
- [ ] Code written by engineers are in Java
- [ ] Asumming code written are in short segments, run time for each function does not exceed 10 minutes
- [ ] Data produced for BI includes encrypted customer information, service survey response
- [ ] Business intelligence would use data for financial and market research purposes
- [ ] If system crashes, there has to be a backup ready
- [ ] Service has to be available 24/7


### System Requirements/Considerations:

#### Source data management
Requirements:
- Ingest uploaded images to cloud from Kafka streams
- Ingest uploaded images to cloud from users of a web application using an API

Considerations:
- Kafka Streams (considering AWS MSK): Noted needed cause we don't have to host a whole kafka cluster on AWS
- Kinesis: Pros (supports Java via Flink, auto scaling, pay as you use) Cons (Mainly for analytics, limitations )


#### Code managment on Cloud

Considerations:
- Amazon API Gateway: creates REST APIs, prevents exposure of AWS credentials between client and cloud infra
- AWS Lambda: Pros: (No server management, execution time up to 15 min, run on demand, scaling is automated, supports Java)

#### Storage
- S3 access points (have diff policies for different types of users: biz analysts, finance analysts)

#### Business Intelligence on Cloud
- 

### System Design Overview

![alt text](https://github.com/RoadRach/DETechAssessment-RachelAng/blob/main/Section-3-System-Design/System_Overview.png "System Design Overview")

<p align="center" width="100%">
    <img width="33%" src="https://github.com/RoadRach/DETechAssessment-RachelAng/blob/main/Section-3-System-Design/System_Overview.png">
</p>

## Section 5: Machine Learning

Classification, Regression or Clustering?:
    Classification and Clustering so far
    Clustering is grouping unlabledexamples/data.  So we will go with classification.

Why did I choose this ML model:
 ML models that are NOT suitable: linear regression, logistic regression
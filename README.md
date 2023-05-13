# Tech Assessment

## How to Navigate

This repository is split into 2 parts: Documentation and Sources

### Documentation
This README file documents all 5 sections of the challenge and serves as a single point of information.

### Sources
Each challenge section will be contained in one single folder:
- Section-1-Data-Pipelines
- Section-2-Databases
- Section-3-System-Design
- Section-4-Charts-and-APIs
- Section-5-Machine-Learning

## Table of Contents
- Section 1: Data Pipelines
- Section 2:Databases
- Section 3: System Design
- Section 4: Charts & APIs
- Section 5: Machine Learning


## Section 3: System Design

### Assumptions Checklist:
- [x] AWS is the cloud service provider
- [ ] Users are all based in Singapore
- [x] Users of web application using API to upload images are the company's clientele
- [ ] Image processing is meant by processing image to identify objects (ex. Plant species, types of dogs, etc)
- [x] Kafka stream is an external entity and only interacts with the cloud environment is uploading images to the cloud environment
- [x] Code written by engineers are in Java
- [x] Asumming code written are in short segments, run time for each function does not exceed 10 minutes
- [x] Processed data for analytics production should be automated
- [x] Business intelligence resource to be accessed by multiple analytical teams (Sales, Fiannce, Analytics)
- [x] SQL is the main language for BI

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
<p align="center" width="75%">
    <img width="75%" src="https://github.com/RoadRach/DETechAssessment-RachelAng/blob/main/Section-3-System-Design/System_Overview.png">
</p>

### S3 Bucket Design
<p align="center" width="75%">
    <img width="75%" src="https://github.com/RoadRach/DETechAssessment-RachelAng/blob/main/Section-3-System-Design/S3_Overview.png">
</p>


## Section 5: Machine Learning

Classification, Regression or Clustering?:
    Classification and Clustering so far
    Clustering is grouping unlabledexamples/data.  So we will go with classification.

Why did I choose this ML model:
 ML models that are NOT suitable: linear regression, logistic regression
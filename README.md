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
- Section 2: Databases
- Section 3: System Design
- Section 4: Charts & APIs
- Section 5: Machine Learning

## Section 1: Data Pipelines

**Requirements Checklist:**
- [x] Process data from users **hourly**
- [x] Required to set up a pipeline to ingest, clean, perform validity checks, and create membership IDs for successful applications
- [x] Split name into first_name and last_name 
- [x] Format birthday field into YYYYMMDD
- [x] Remove any rows which do not have a name field (treat this as unsuccessful applications) 
- [x] Create a new field named above_18 based on the applicant's birthday
- [x] Membership IDs for successful applications should be the user's last name, followed by a SHA256 hash of the applicant's birthday, truncated to first 5 digits of hash (i.e <last_name>_<hash(YYYYMMDD)>) 
- [x] You are required to consolidate these datasets and output the successful applications into a folder, which will be picked up by downstream engineers
- [x] Unsuccessful applications should be condolidated and dropped into a separate folder.

**Specificaitons:**
- Mobile number is 8 digits
- Applicant is over 18 years old as of 1 Jan 2022
- Has a valid email if email ends with @emailprovider.com or @emailprovider.net

### Evidence of Cron job
<p align="center" width="75%">
    <img width="75%" src="https://github.com/RoadRach/DETechAssessment-RachelAng/blob/main/Section-1-Data_Pipelines/cron.png">
</p>

To run the script hourly, run the following:
```
crontab -e

i

0 * * * * ~/local directory/DETechAssignment-RachelAng/Section-1-Data-Pipelines/cron_job/cron_application.py

:wq
```

Main code: Section-1-Data-Pipelines > cron_job > cron_application.py

Output : Section-1-Data-Pipelines > cron_job > output

## Section 2: Databases
### Assumption:
- In each transaction, quantity of each items bought is 1
- For items boughts it could be a list of product_ids

### Requirements:
- [ ] Set up a PostgreSQL db using the docker image provided
- [ ] Have a dockerfile which will stand up db with the DDL statemnents to create the necessary tables
- [x] Produce entity relationship diagrams
- [x] Need to write SQL statement for the following: (1) Which are the top 10 members by spending (2) Which are the top 3 items that are frequently brought by members

### Entity relationship diagram
<p align="center" width="75%">
    <img width="75%" src="https://github.com/RoadRach/DETechAssessment-RachelAng/blob/main/Section-2-Databases/Entity_Diagram.png">
</p>


### SQL queries:
- Which are the top 10 members by spending
```
SELECT TOP 10 membership_id
FROM order_details od
LEFT JOIN customer c
ON od.cust_id = c.cust_id
GROUP BY cust_id
ORDER BY SUM(od.total_items_price) DESC
```

- Which are the top 3 items that are frequently brought (I am assuming it is supposed to be bought) by members
```
SELECT TOP 3 prod_name
FROM order_details od
LEFT JOIN products p
ON od.prod_id = p.prod_id
ORDER BY count(order_id) DESC
```

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
**Requirements:**
- Ingest uploaded images to cloud from Kafka streams
- Ingest uploaded images to cloud from users of a web application using an API

**Considerations:**
- Kafka Streams (considering AWS MSK): Noted needed cause we don't have to host a whole kafka cluster on AWS
- Kinesis: Pros (supports Java via Flink, auto scaling, pay as you use) Cons (Mainly for analytics)

#### Code managment on Cloud
**Requirements:**
- Code must be hosted on cloud

**Considerations:**
- Amazon API Gateway: creates REST APIs, prevents exposure of AWS credentials between client and cloud infra
- AWS Lambda: Pros: (No server management, execution time up to 15 min, run on demand, scaling is automated, supports Java)

#### Storage
**Requirements**
- Images and its metadata needs to be deleted after 7 days
- Ingested data needs to be prepared for analytics

**Considerations**
- S3 using access points (have diff policies for different types of users: biz analysts, finance analysts)

#### Business Intelligence on Cloud
**Requirements**
- Have to be hosted on cloud

**Consideration**
- QuickSight: UI similar to tableau and PowerBI

### System Design Overview
<p align="center" width="75%">
    <img width="75%" src="https://github.com/RoadRach/DETechAssessment-RachelAng/blob/main/Section-3-System-Design/System_Overview.png">
</p>

### S3 Bucket Design
<p align="center" width="75%">
    <img width="75%" src="https://github.com/RoadRach/DETechAssessment-RachelAng/blob/main/Section-3-System-Design/S3_Overview.png">
</p>


## Section 4: Charts & APIs

### 503 Message
<p align="center" width="75%">
    <img width="75%" src="https://github.com/RoadRach/DETechAssessment-RachelAng/blob/main/Section-4-Charts-and-APIs/Screenshot%202023-05-14%20at%205.32.03%20PM.png">
</p>

** Was working and wanted to have a touch up but the server on their end is down **

This section I have plotted two graphs:
- Number of COVID-19 cases in Singapore yearly
- Number of COVID-19 cases in Singapore each month per year

## Section 5: Machine Learning

**Classification, Regression or Clustering?:**
- Classification and Clustering so far
-  Clustering is grouping unlabledexamples/data. so classification would be more suitable, and regression models would be used as the training model.  From there we can compare which is a better model and then determine which is the best by coming up with the score.

**Why did I choose this ML model:**
Since we have multiple variables and known target to work with, regression is chosen for this task.
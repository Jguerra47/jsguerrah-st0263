# Lab 3.3 - Sophisticated Data Warehouse Implementation with AWS RedShift and RedShift Spectrum

## Overview
This comprehensive guide delineates the procedure for an advanced data warehouse setup leveraging Amazon RedShift and RedShift Spectrum. This assumes a foundational setup AWS S3, AWS Glue, and Amazon Athena. Our focus will now shift to the intricate aspects of configuring and optimizing the warehouse for enhanced performance and scalability.

## Detailed Implementation Steps

### Step 1: IAM Role Configuration and Optimization

#### 1.1 Initiation of Role Definition
- **Accessing IAM Service**: Initiate by navigating to the IAM (Identity and Access Management) service, as depicted below.

  ![IAM Service Access](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/b8a84b11-0cde-405a-ab62-ce4445acf33b)

- **Role Section Navigation**: Proceed to Access Management >> Roles.

  ![Roles Section](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/9e25c64e-bdf6-41e0-94c4-1e4166817c5f)

- **Role Creation**: Select 'Create Role'.

  ![Create Role](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/aefa7865-eedd-4a00-b372-52bb88f063e7)

#### 1.2 Role Configuration for AWS Service
- **Role Setup**: Configure the role for 'AWS Service'.

  ![Role Setup](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/37491c83-3554-47d8-93c2-41724fe0d878)

- **Service Selection**: Choose the 'Redshift' service.

  ![Select Redshift](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/39db7f22-96f9-4922-b5f6-2cc3e6c41803)

- **Role Type Specification**: Opt for 'Redshift - Customizable'.

#### 1.3 Permission Policy Allocation
- **Policy Definition**: Define the Permission Policies from the following:

  ![Permission Policies](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/d1d60228-3be8-411e-a17f-82c6b899b6ea)

- **Policy Selection**: Carefully select the required permissions.

  ![Select Permissions](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/0b5856f4-6203-4fef-88f0-0a7305960dd1)

#### 1.4 Role Naming and Confirmation
- **Role Naming**: Assign a descriptive name to the role.

  ![Naming Role](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/c2143100-495d-4b0c-9aab-f229c7b2a6e3)

- **Final Validation**: Confirm the details and create the role.

  ![Confirm details](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/27482657-0f3e-497e-9bc6-feda58525577)
  ![Create Role](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/51f7478b-0e2f-407d-ac6c-69aa70d4d9aa)

#### 1.5 ARN Retrieval
- **Role Verification**: After role creation, verify the role in the Roles section.

  ![Verify Role](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/9b2d9b71-bf75-4274-897a-d5ff2d258d53)

- **ARN Extraction**: Extract the 'ARN' from the Summary for later use.

  ![ARN Extraction](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/b012aa65-abd4-4498-b497-a499895a390f)

---

### 2. Advanced Utilization of RedShift's Query Editor Service

#### 2.1 Seamless Integration with RedShift's Query Editor
- **Accessing RedShift**: Start by accessing the AWS RedShift service.

  ![Access RedShift](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/6559d3ab-fbb3-459b-8ca4-ac022705e478)

- **Cluster Selection**: Choose your specific cluster for operations.

  ![Select Cluster](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/b9775199-f69c-4335-a11a-b9b2d423a741)

- **Query Data Section**: Navigate to the 'Query data' section and select 'Query in query editor v2'.

  ![Query Editor Access](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/46868aea-d556-46fa-bae5-ad953f6fdd51)

- **Database Connection Configuration**: Establish a connection by entering your cluster's database credentials.

  ![Configure Connection](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/68ea1b5f-bd96-4723-8ee2-61d494dfa89d)

#### 2.2 Establishment of an External Database
- **Database Creation**: Inside the editor, execute the SQL command to create an external schema. This leverages the AWS data catalog and specifies the IAM role for authorization.

  ```SQL
  create external schema myspectrum_schema
  from data catalog
  database '{database_name}'
  iam_role '{role_arn}'
  create external database if not exists;
  ```

  ![Create External Schema](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/f99d9482-98fd-429b-8dc6-d6f7a3b7da8c)

- **Confirmation**: Execute the script to initialize the database and await the confirmation message.

  ![Database Creation Confirmation](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/421e5fa2-6166-46d6-a9b6-2516644b48c3)

#### 2.3 Integration of External Data into Database

##### 2.3.1 Data Preparation
- **Data Requirements**: Ensure the S3 bucket is configured with necessary datasets as outlined in the previous lab.

##### 2.3.2 Script-Driven Table Creation
- **Table Creation**: Implement the SQL script to create an external table within `myspectrum_schema`, pointing to the data stored in S3.

  ```SQL
  create external table myspectrum_schema.sales(
    salesid integer,
    listid integer,
    sellerid integer,
    buyerid integer,
    eventid integer,
    dateid smallint,
    qtysold smallint,
    pricepaid decimal(8,2),
    commission decimal(8,2),
    saletime timestamp)
    row format delimited
    fields terminated by '\t'
    stored as textfile
    location '{s3_URI}'
    table properties ('numRows'='172000');
  ```

  ![Creating External Table](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/bc88bb0d-6d8b-4060-b64e-b271631d86bb)
  ![Show Table](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/b6caa6f9-4723-45e9-9162-099466041eb9)

- **Record Verification**: Validate the table creation by executing a count query.

  ![Count Records](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/44fcaf0d-6258-4425-b62f-93a27c5c59ff)

### 2.4 Data Manipulation and Analysis

##### 2.4.1 Constructing Native Tables
- **Native Table Creation**: Develop a native Redshift table to integrate with the external table.

  ```SQL
  create table my_table(
    eventid integer not null distkey,
    venueid smallint not null,
    catid smallint not null,
    dateid smallint not null sortkey,
    eventname varchar(200),
    starttime timestamp
    );
  ```

  ![Create Native Table](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/967c2971-64e4-4dcc-8f11-f9f4ac4e422c)

##### 2.4.2 Data Import into Native Tables
- **Data Loading**: Populate the native table with data sourced from an S3 'events' folder.

  ```SQL
  COPY my_table FROM '{s3_URI}'
    iam_role '{iam_ARN}'
    delimiter '|' timeformat 'YYYY-MM-DD HH:MI:SS' region 'us-east-1';
  ```

  ![Load Data](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/029a2fbe-d16c-4ce9-a5d3-3053a63facd6)

##### 2.4.3 Advanced Table Operations
- **Data Analysis**: Run advanced SQL queries to analyze and correlate data across the native and external tables.

  ```SQL
  select top 10 myspectrum_schema.sales.eventid,
    sum(myspectrum_schema.sales.pricepaid)
    from myspectrum_schema.sales, my_table
    where myspectrum_schema.sales.eventid = my_table.eventid
    and myspectrum_schema.sales.pricepaid > 30
    group by myspectrum_schema.sales.eventid
    order by 2 desc;
  ```

  ![Data Analysis](https://github.com/jdprietom03/jdprietom-st0263/assets/80794157/8d71667e-3d42-42a2-b880-89d18415df39)

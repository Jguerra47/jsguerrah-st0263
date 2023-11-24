# LAB 3-2: Data Catalog with Glue and Athena

## Course Details

| Information |  |
| --- | --- |
| Course name | Tópicos especiales en Telemática |
| Course ID | ST0263 |
| Name | Juan Sebastian Guerra Hernandez (jsguerrah@eafit.edu.co) |
| Teacher | Edwin Nelson Montoya Munera (emontoya@eafit.edu.co) |

# 1. Main goal

Catalog data from the course dataset and be able to send serverless queries

---

# 2. Issues solved and not solved

- [x] Creation of an AWS S3 bucket to store the data.
- [x] Create a crawler from Glue to catalog the dataset.
- [x] Query from Athena over the tables.
- [x] Store the query results in S3.

---

# 3. Execution environment

## Guide

The following guide will provide the steps to follow for a correct catalog of the data.

---

### Section 1: AWS S3 bucket creation

We will have to create an AWS S3 bucket to store the data.

1. Log in to the AWS console and search for the S3 service.
2. Select the `Create bucket` button.
3. Enter a name for the bucket; then in the section **Object Ownership** select the option `ACLs enabled` and check the box `Object writer`. 
    
    Then in the **Block Public Access settings for this bucket** section remove the check from the 'Block all public access' option and select the checkbox ‘I acknowledge that the current settings might result in this bucket and the objects within becoming public.’:
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/fafb9c14-5727-47dc-8d33-6d40bff53f40">
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/77c59dc4-3055-4de7-918b-77c10767bb20">
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/f7476ef1-feac-47fc-ab96-ec84e5f2f6a7">

4. Leave the following options as default and select the `Create Bucket` button.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/38a1357c-f752-49a2-8df6-5d493268946a">
    
5. Go to the [datasets](https://github.com/st0263eafit/st0263-232/tree/main/bigdata/datasets) and download them.

6. Return to the main bucket interface, select the name of the previously created bucket and drag the downloaded datasets into it, then select the `Upload` button.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/cd2b2857-558c-4666-ad06-235b3915344b">

---

### Section 2: Catalog data with AWS Glue

1. Go to the AWS web console and search for the Glue service
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/487c4eea-eaa0-4739-a2f7-1049040f05bd">

2. On the control sidebar, go to  **Crawlers** section.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/874e6083-e14f-48da-af07-43fc96730979">
    
3. Click on `Create crawler`.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/1b37015a-a287-45c0-bb1a-d4993afd3ac7">

4. Set a name for your crawler, then click on `Next`.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/44ef0dba-cbfe-45e6-80e5-78871072151e">

5. In **Choose data sources and classifiers** section, click on `Add a data source`
   
   <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/fe7348e9-f269-41b2-82ba-b23797940ec2">

6. Navigate through to find the folder you want to catalog.
   
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/26631b59-9e47-496b-8416-ff70e3a32ac2">

7. Once selected, click on `Add an S3 data source`
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/b1b2f45d-5f30-4c37-af64-74b57801db1d">

8. The preview of the data source should look like this. Then, click on `Next`

    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/02bd2848-9c4a-45c7-ba8b-e696c213371a">

9. In the **Configure security settings** section, set the LabRole.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/04b324db-26d0-4092-8389-fc85209577f4">

10. Set the default target database. Keep `On demand` schedule to catalog the data manually.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/291c667f-65c2-401c-beb6-b69b6508f014">

11. After the previous steps, the crawler should be created successfully.

    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/84cf9e92-1bc5-4b33-8809-eab518b6d7cc">

12. Now you must start to catalog. Select your crawler and then click on `Run` to start the job.

    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/3596f7a8-a313-4775-af4b-1a9781593f17">

13. Once the job has finished, in the control sidebar go to **Tables** section.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/13a228be-cffe-4f8f-964a-2d09db1b0291">

14. The new table must be there, with a location from your S3 bucket.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/4a3fa26f-4c76-4086-b275-2c3cac622330">
    
---

### Section 3: Query with Athena

1. Go to the AWS web console and search for the Athena service.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/935e9050-29a0-47c8-8bf7-d842b94e236d">
    
2. On the control sidebar, select the **Query editor** section.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/12d929d2-eec3-4c2f-a55f-ba0354c156a0">
    
3. We must set a location to store our results. Go to **Settings**. Then, click on `Manage`.

    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/72a97801-b421-474e-af30-e0981e7b4e81">

4. In the _Location of query result_ set a path over your bucket where you want to store.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/fc7da52a-a8a7-4572-b1d9-2611499129cf"> 

5. Then, click on `Save`. Your settings overview should look like this.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/1a7a1312-b349-45a9-a82d-5afaa2ff2c29">

7. Go back to **Editor** section. Select the table created with your crawler.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/9f54df6f-9fb7-45e6-ac05-cf91ae939193">

✅ You're done! You can now query over your catalog dataset with Athena.
    
**Examples**
- Query example:
```sql
  SELECT * FROM “default”.”<YOUR_TABLE>” WHERE lifeex > 80 ORDER BY lifeex desc;
```

<img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/a420ea17-65bd-4969-8d7d-21451187e4a8">


---

### Section 4: Save outputs from queries

1. Log into the AWS web console and search for the S3 service.
2. Select your bucket.
3. Search in the path you selected in Section 3, step 4. This path is defined to store output of your queries.

<img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/6cedacf9-e9fe-46c9-830f-8b5ecad1e2b6">


✅ You're done! You can store the output of your queries from Athena in S3 buckets.

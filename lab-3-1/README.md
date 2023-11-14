# LAB 3-1: File Management in HDFS and S3

## Course Details

| Information |  |
| --- | --- |
| Course name | Tópicos especiales en Telemática |
| Course ID | ST0263 |
| Name | Juan Sebastian Guerra Hernandez (jsguerrah@eafit.edu.co) |
| Teacher | Edwin Nelson Montoya Munera (emontoya@eafit.edu.co) |

# 1. Main goal

Manage all available files from [datasets](https://github.com/st0263eafit/st0263-232/tree/main/bigdata/datasets) in both HDFS (temporary storage) and S3 (permanent storage) services.

---

# 2. Issues solved and not solved

- [x] Creation of an AWS S3 public bucket.
- [x] File management in HDFS using terminal.
- [x] File management in HDFS using HUE.
- [x] File management in S3 using HUE.

---

# 3. Execution environment

## Usage guide

### Section 1: Creation of an AWS S3 public bucket

1. Log in to the AWS console and search for the S3 service.
2. Select the `Create bucket` button.
3. Enter a name for the bucket; then in the section **Object Ownership** select the option `ACLs enabled` and check the box `Object writer`. 
    
    Then in the **Block Public Access settings for this bucket** section remove the check from the 'Block all public access' option and select the checkbox ‘I acknowledge that the current settings might result in this bucket and the objects within becoming public.’:
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/fafb9c14-5727-47dc-8d33-6d40bff53f40">
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/77c59dc4-3055-4de7-918b-77c10767bb20">
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/f7476ef1-feac-47fc-ab96-ec84e5f2f6a7">

4. Leave the following options as default and select the `Create Bucket` button:
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/38a1357c-f752-49a2-8df6-5d493268946a">
    
5. Once in the S3 menu, select the name of the previously created bucket:
6. Select the **Permissions** section and look for the **Access control list (ACL)** subsection, once there, select the `Edit` button.
7. Check the 'List' and 'Read' boxes for 'Everyone (public access)' and 'Authenticated users group (anyone with an AWS account)'; then check the option 'I understand the effects of these changes on my objects and buckets.'; finally select the `Save changes` button:
   
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/d915724e-33a8-4113-acb6-43dd270ce45f">
    
8. Go to the [example file](https://github.com/st0263eafit/st0263-232/blob/main/bigdata/datasets/airlines.csv) and select the `Download raw file` button:
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/6f2ff9b1-2c8f-4f82-b2e3-d07136e6cb4a">

9. Return to the main bucket interface, select the name of the previously created bucket and drag the downloaded file into it, then select the `Upload` button.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/cd2b2857-558c-4666-ad06-235b3915344b">

    
10. Select the name of the previously uploaded file and then, in the **Properties** section under ****Object overview**** copy the 'Object URL'.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/afd7fcd4-059d-4a5d-ace1-7ab3fc95b7b3">
    
11. In a browser window paste the previously copied URL leaving aside '/airlines.csv'.
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/4233241e-c0da-48d5-b8bc-4987f287f28d">

✅ You're done! You now have an AWS S3 public bucket.

Note: In order to read the files from the public bucket created above through the AWS CLI you can use the following command:

```bash
aws s3 ls s3://<YOUR_BUCKET_NAME>
```
Command to read the previously created bucket

```bash
aws s3 ls s3://jsguerrahs3
```
  <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/e52c2b93-b04a-4777-bcdf-847e31619075">

---

### Section 2: File management in HDFS using terminal

1. We will have to create an AWS EMR cluster, visit the following guide '[Creating an EMR Cluster](https://github.com/Jguerra47/jsguerrah-st0263/tree/main/lab-3-0)' for this purpose.
2. Once the cluster specified above has been created we must connect to it via SSH; how to connect to the cluster via SSH can be found [here](https://github.com/Jguerra47/jsguerrah-st0263/tree/main/lab-3-0#section-4-access-to-primary-node).
3. After establishing a connection to the primary node we will create a folder called 'gutenberg-small' inside the path '/user/hadoop/datasets' using the following commands:

    1. Create the directory 'datasets' inside the path 'user/hadoop/'.
   
    ```bash
    hdfs dfs -mkdir /user/hadoop/datasets
    ```

    2. Create the directory 'gutenber-small' inside the path 'user/hadoop/datasets/'.
   
    ```bash
    hdfs dfs -mkdir /user/hadoop/datasets/gutenberg-small
    ```

    3. List directories and files present in /user/hadoop/ path
   
    ```bash
    hdfs dfs -ls /user/hadoop/datasets
    ```
    
7. Put the contents of a local to the directory '/user/hadoop/datasets/gutenberg-small' using the following command. For this purpouse you could clone the repository that has example datasets
    
    ```bash
    hdfs dfs -put <YOUR_LOCAL_FOLDER> /user/hadoop/datasets/gutenberg-small/

✅ You are done! You can now manage files to HDFS from the EMR cluster using the terminal.

---

### Section 3: File management in HDFS using HUE

1. Go to AWS console and search for the EMR service.
2. Select the 'Cluster ID' that has the status 'Waiting'; then select the **Applications** option.
3. Select the URL of the **Hue** field and enter the 'hadoop' user and a password.
4. Select the **Files** section:
   
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/a0ef39ee-0773-4d16-8baf-3d96ea237677">

6. If you have been following the previous steps right, you must found the folder **datasets**. Otherwise, create the folder in `New` button:
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/b41c4eb2-df2f-4c83-bf1b-1f30fb1e73c6">
    
7. Select the `Upload` button:
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/895a21a4-4d45-435c-be9d-0492ad517efc">

✅ Done! You can now upload files to HDFS of the EMR cluster via HUE.

---

### Section 4: File management in S3 using HUE

1. Log into the AWS console and search for the EMR service.
2. Select the 'Cluster ID' that has the status 'Waiting'; then select the '**Applications**' option.
3. Select the URL of the 'HUE' field and enter the 'hadoop' user and a password of your choice.
4. Select the **S3** section:
    
    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/70ca831c-62ce-4a67-a46f-15e4b78a3209">

5. All your buckets must be found there.

    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/62c87cfc-1cd0-4683-81c2-b39790e9593a">

6. Select a bucket. Then, click on `Upload` button, `Select Files`; and finally choose the files you want to upload.

    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/e55baa1c-3eb2-4ed9-9834-3b9781078fda">

7. Verify the file is accesible through other ways like AWS CLI. Execute the next command to list the file over your bucket:

    ```bash
    aws s3 ls s3://jsguerrahs3
    ```

    Should show the file you uploaded before.

    <img width="820" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/59aa1ab6-7111-42da-b467-7b2a3ed5781e">

✅ Done! You can now upload files to an S3 bucket via HUE.

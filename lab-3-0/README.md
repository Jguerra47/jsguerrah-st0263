# LAB 3-0: EMR Cluster Creation

## Course Details

| Information |  |
| --- | --- |
| Course name | Tópicos especiales en Telemática |
| Course ID | ST0263 |
| Name | Juan Sebastian Guerra Hernandez (jsguerrah@eafit.edu.co) |
| Teacher | Edwin Nelson Montoya Munera (emontoya@eafit.edu.co) |

# 1. Main goal

Creation of an AWS EMR Cluster in Amazon to work with all the labs.

---

# 2. Issues solved and not solved

- [x] Creation of an AWS S3 bucket to store the notebooks that we will create in the AWS EMR cluster.
- [x] Creating an AWS EMR Cluster version 6.13.0
- [x] SSH connection to the master node.
- [x] Functional Hue service.
- [x] JupyterHub service functional.

---

# 3. Execution environment

## Usage guide

The following guide will provide the steps to follow for a correct creation of the AWS EMR Cluster.

---

### Section 1: AWS S3 bucket creation

We will have to create an AWS S3 bucket to store the notebooks that we will create in the AWS EMR cluster.

1.  Log in to the AWS web console and search for the S3 service:
    
3. Click on `Create bucket`:
   
    <img width="581" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/66d70a44-a226-42c2-8de2-885796e6bf91">

    
4. Enter a name for the bucket, leave the subsequent options as default and select the `Create Bucket` button.

   <img width="621" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/625d188c-6bc5-4f68-8a15-7c35f3344234">
   <img width="623" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/07bf6956-dab0-4fa6-b963-c834f4184581">
    
---

### Section 2: AWS EMR cluster creation

1. Go to the AWS web console and search for the EMR service.
    
    <img width="684" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/1ddb76cf-1af7-4bb5-94c7-264f31346247">
    
2. Click on `Create cluster`.
    
    <img width="1336" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/d754e8dd-1eab-4d58-9004-40d7d7f8e906">

3. Enter a name for the cluster, select the version `emr-6.14.0` and select `Custom` in the **Application Bundle** section. Then, select the following applications and enable `Use for Hive table metadata` and `Use for Spark table metadata`.
    
    <img width="622" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/a0e26ce1-549e-4d9d-a724-59b176076eb8">
    
4. Edit the **Cluster termination** section and assign termination after a three (3) hour idle time.
    
    <img width="621" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/8136031e-c371-46a9-8714-a02a8e2fd342">

    
5. Leave the subsequent options as default and go to the **Software settings** section.
6. Select the `Enter configuration` option and paste the following configuration:
    
    ```json
    [
      {
        "Classification": "jupyter-s3-conf",
        "Properties": {
          "s3.persistence.enabled": "true",
          "s3.persistence.bucket": "<YOUR_BUCKET_NAME>"
        }
      }
    ]
    ```
    Like this:
   
    <img width="622" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/ed6fcc8b-72e4-4ab2-a106-7fb56f403441">
    
8. Go to the section **Security configuration and EC2 key pair** and in the option **Amazon EC2 key pair for SSH to the cluster**. Now, choose the vockey used for labs (or you could select a custom one).
    
    <img width="617" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/ae4432c6-40cd-4991-8113-ca4b1c6970db">

9. In the section '**Identity and Access Management (IAM) roles** select the next options:

    - **Amazon EMR Service Role**: EMR_DefaultRole
    - **EC2 Instance Profile for Amazon EMR**: EMR_EC2_DefaultRole
    - **Custom Auto Scaling Role**: LabRole

    <img width="794" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/468e587b-a997-4906-9352-68b024984050">
    
10. Finally, click on `Create cluster`.
    
    <img width="262" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/8ab20a33-8614-414e-bc67-ae337bae4a0f">

---

### Section 3: Edit security groups for the applications

Reminder: The following steps should only be performed once, each time a cluster is created, destroyed or cloned.

1. Go to the AWS web console and search for the EMR service.
    
    <img width="684" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/1ddb76cf-1af7-4bb5-94c7-264f31346247">
    
2. Within the Amazon EMR menu select the option **Block public access**.
    
    <img width="355" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/73a8498e-a976-499a-abad-76cb1eadf7c2">
    
3. Select the `Edit` button. In the **Block public access** section select the `Turn off` option and select the `Save` button.
    
    <img width="621" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/8b2be033-7a50-4da5-b1e5-6bf73c9e11a1">

4. Within the Amazon EMR menu go to **Clusters** and select the `Cluster ID` that has the status 'Waiting'. Then select the `Applications` option.
    
    <img width="1095" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/3d4b9a42-3dfe-400f-8983-378be8fdf686">

    The TCP ports above must be opened, in addition to TCP ports 22, 14000 and 9878. 

5. Search for the EC2 service. Then, go to `Security groups` section.
    
    <img width="927" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/33f33183-643a-42ce-9e58-ac5ca72c54e9">

6. Click on the ID of the SG that has the name ‘ElasticMapReduce-master’.
    
    <img width="1392" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/290e6513-6f98-4d0e-bf67-525f8afcb7ce">

9. Click on `Edit inbound rules`.
    
    <img width="1390" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/81e337ab-bd03-401a-a353-c416b4798035">

10. For each of the ports shown in the steps 4, perform the following:
    1. Click on `Add rule`:
    3. Select the `Custom TCP` option (if needed, or you could search the option), enter the port number and select the 'Anywhere-IPv4' option:
    4. Type the port.
    5. Click on `Save rules` once you have added all.

---

### Section 4: Access to Primary node

1. Within the Amazon EMR menu go to **Clusters** and select the `Cluster ID` that has the create before.
2. Click on the URL `Connect to the Primary node using SSM` and follow the instructions there. 
    
    <img width="1567" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/c7d53aef-fcec-4338-9da4-1b44f5f79f71">

3. A successful SSH connection to the master node of the cluster will look as follows:
    
    <img width="623" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/56d34303-2972-46f2-80d0-7e58bdaef4f5">

4. You will need to edit the 'hue.ini' file by following these steps: 
    1. Type the following command in the terminal:
   
        ```bash
        sudo nano /etc/hue/conf/hue.ini
        ```
        
    2. Find the line containing 'webhdfs_url' and change the port. You should put the HDFS Name Node port found in the Applications section over your cluster.

        <img width="624" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/d5d797bc-ef9d-4341-8075-d277cf321b0b">

        As you can see, the selected port must be 9870
        
        <img width="620" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/ac5a3857-5d64-4404-8746-f1df054f820d">
        
    3. Save the changes over the file.
    4. Restart the Hue service using the following command:
        
        ```bash
        sudo systemctl restart hue.service
        ```
        
---

### Section 5: Using Hue

1. Within the Amazon EMR menu go to **Clusters** and select the `Cluster ID` that has the status 'Waiting'. Then select the `Applications` option.
    
    <img width="1095" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/3d4b9a42-3dfe-400f-8983-378be8fdf686">
    
2. Select the URL of the 'Hue' field. Then, enter the user 'hadoop' and a password of your choice.
    
    <img width="562" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/21caa9e3-7a9c-48ba-8edc-12bda1712fb1">

✅ You're done! You can now manage files through Hue for HDFS.

---

### Parte 7: Using JupyterHub

1. Log into the AWS web console and search for the EMR service, select the `Cluster ID` that has the status 'Waiting'; then select the **Applications** option.
2. Select the URL of the 'JupyterHub' field. Now, enter the user 'jovyan' and password 'jupyter'.
3. Select the `New` button and select the `PySpark` option:
    
    <img width="526" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/92508034-3f18-47d5-ae4f-37bb2a11218b">
    
4. Verify the Spark context variables are installed:
    
    <img width="614" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/34b0254d-5d74-491e-a032-12d7c5e3e880">

✅ You're done! You can now build PySpark notebooks.

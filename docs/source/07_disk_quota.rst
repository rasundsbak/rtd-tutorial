.. _07 disk quota:
07 Disk quota exceeded problem
===================

This guide helps you address the "disk quota exceeded" problem by detailing steps to clean up your home directory, delete cache files, and check available disk space. 
# Summary for Cleaning Up Temporary Data

This guide provides steps to clean up temporary data generated during the usage of 
Hugging Face RAG models to avoid "disk quota exceeded" issues.

### Step 1: Remove Temporary Data from Cache Directory

First, check and remove temporary files from the cache directory.

1. **List contents of the cache directory**:
    ```sh
    ls -lh /fp/projects01/projectname/huggingface/cache/RAG_Sequence_NQ
    ```

2. **Remove all files and subdirectories in the cache directory**:
    ```sh
    rm -rf /fp/projects01/projectname/huggingface/cache/RAG_Sequence_NQ/*
    ```

### Step 2: Remove Temporary Data from Dataset Directory

Next, check and remove temporary data from the dataset directory.

1. **List contents of the dataset directory**:
    ```sh
    ls -lh /fp/projects01/projectname/rag_datasets
    ```

2. **Remove all dataset files**:
    ```sh
    rm -rf /fp/projects01/projectname/rag_datasets/*
    ```

### Step 3: Check and Remove Temporary Data from Home Directory

Temporary data might also be stored in your home directory, especially in `.cache` or `.local` folders.

1. **Check contents of the .cache folder**:
    ```sh
    ls -lh /fp/homes01/u01/username/.cache
    ```

2. **Remove cache files from the .cache directory**:
    ```sh
    rm -rf /fp/homes01/u01/username/.cache/*
    ```

3. **Check contents of the .local folder**:
    ```sh
    ls -lh /fp/homes01/u01/username/.local
    ```

4. **Remove unnecessary files from the .local directory**:
    ```sh
    rm -rf /fp/homes01/u01/username/.local/*
    ```

### Explanation:
- **Cache Directory**: /fp/projects01/projectname/huggingface/cache/RAG_Sequence_NQ
- **Dataset Directory**: /fp/projects01/projectname/rag_datasets
- **Home Directory**: Used for storing user-specific temporary data.

Following these steps will help you free up disk space and avoid exceeding your disk quota while working with Hugging Face RAG models.


If you have further questions or need additional assistance, contact the system administrator.

.. _07 Disk quota:
07 Disk quota exceeded problem
===================

This guide helps you address the "disk quota exceeded" problem by detailing steps to clean up your home directory, delete cache files, and check available disk space. 

Step 1: List contents in the home directory

Listing the contents in your home directory can help identify large files or folders that can be deleted or moved.

Terminal view 1::

   ```
   $ ls -lh /fp/homes01/u01/username
   ```

This command will display a list of all files and folders in your directory along with their sizes.

Step 2: Delete unnecessary cache files

Cache files can often take up significant space. We recommend identifying and deleting them.

#### Find cache files:
Terminal view 2::

   ```
   $ find /fp/homes01/u01/username -type f -name "*.cache"
   ```

#### Delete cache files:
Terminal view 3::

   ```
   $ find /fp/homes01/u01/username -type f -name "*.cache" -exec rm {} \;
   ```

### Step 3: Check available disk space

After deleting unnecessary files, check the available disk space to ensure the problem is resolved.

Terminal view 4::

   ```
   $ df -h /fp/homes01/u01/username
   ```

This will display information about the disk space usage, including the total size of the filesystem, used space, available space, and percentage used.

### Example Workflow:

#### 1. List contents

Terminal view 5::

   ```
   $ ls -lh /fp/homes01/u01/username
   ```

Example output:

```
total 4.0K
drwxr-xr-x 2 user group 4.0K Jun  1 12:34 old_data
-rw-r--r-- 1 user group 2.0G Jun  1 12:34 large_file.txt
```

#### 2. Delete cache files

Find cache files:
Terminal view 6::

   ```
   $ find /fp/homes01/u01/username -type f -name "*.cache"
   ```

Delete cache files:
Terminal view 7::

   ```
   $ find /fp/homes01/u01/username -type f -name "*.cache" -exec rm {} \;
   ```

#### 3. Check available disk space

Terminal view 8::

   ```
   $ df -h /fp/homes01/u01/username
   ```

Example output:

```
Filesystem      Size  Used Avail Use% Mounted on
fp-homes01       30T   10T   20T  34% /fp/homes01
```

This procedure helps you free up disk space by identifying and deleting unnecessary files, providing a simple process to maintain optimal disk management. Be cautious when deleting files to avoid removing important data.

### Final Notes:

- Use `ls -lh` to identify large files or folders.
- Use `find` to locate and delete cache files.
- Use `df -h` to check available disk space after cleanup.

If you have further questions or need additional assistance, contact the system administrator.

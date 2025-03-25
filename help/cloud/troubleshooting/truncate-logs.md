---
title: Truncate logs
description: Learn how to triage a failed deployment because of a full hard drive by truncating large log files.
feature: Cloud, Site Management
topic: Commerce, Development
role: Architect, Developer
level: Beginner, Intermediate
doc-type: Technical Video
duration: 206
last-substantial-update: 2025-3-25
jira: KT-17595
exl-id: 4a36de40-fb55-41ad-afef-35fc18a271ec
---
# Truncate logs

Learn how to triage and a failed deployment due to a full hard drive. Learn how to find and what commands can be run to free up space in your Adobe Commerce Cloud environment. 

If you think you might need these log files, you can `rsync` them or use other methods to get a copy available off the server before you truncate them.

## Who is this video for

- Developers and IT Professionals
- System Administrators

## Video Content

- Diagnose and Resolve a failed deployment
- Where some common large log files are found
- Quick method to truncate a log file

>[!VIDEO](https://video.tv.adobe.com/v/3454572?learn=on)


## Commands used in the video

To check hard drive space `df -h`. Pay attention to the line dev/mapper/xxxx

```SHELL
df -h

Filesystem                              Size  Used Avail Use% Mounted on
/dev/loop217                           1016M 1016M     0 100% /
none                                    492K  4.0K  488K   1% /dev
fake-sysfs                              120G     0  120G   0% /sys
tmpfs                                   120G     0  120G   0% /sys/fs/cgroup
tmpfs                                   384M     0  384M   0% /dev/shm
tmpfs                                    50M  460K   50M   1% /run
tmpfs                                   5.0M     0  5.0M   0% /run/lock
/dev/loop236                            144M  144M     0 100% /app
/dev/mapper/hyjh5nlaoabqtxxnh4opgjqzpu  4.9G  4.9G     0 100% /mnt
/dev/loop14                             8.0G  403M  7.6G   5% /tmp
/dev/mapper/platform-lxc                5.0T   69G  4.7T   2% /run/shared
```


Display the files and their sizes in human readable format such as kb, mb and gb using the command `ls -lah`

```SHELL 
ls -lah

total 4.7G
drwxr-xr-x 2 web web 4.0K Jul 16  2024 .
drwxr-xr-x 6 web web 4.0K Jan 10  2024 ..
-rw-rw-r-- 1 web web 487K Jul  5  2024 cache.log
-rw-r--r-- 1 web web 1.2K Jul 16  2024 cloud.error.log
-rw-r--r-- 1 web web 328K Mar 25 14:09 cloud.log
-rw-rw-r-- 1 web web 2.4G Jul  5  2024 cron.log
-rw-rw-r-- 1 web web  363 Dec  6  2023 debug.log
-rw-rw-r-- 1 web web  15K Jan 10  2024 indexation.log
-rw-r--r-- 1 web web 229K Jan 10  2024 install_upgrade.log
-rw-r--r-- 1 web web 2.9K Jul 16  2024 patch.log
-rw-rw-r-- 1 web web 2.4G Mar 25 15:36 support_report.log
-rw-rw-r-- 1 web web  516 Dec  6  2023 system.log
```

## Examples for truncate log

After you ssh into the right project and environment, change into the `var/log` directory. Then you can truncate a file with something similar to `> some-log-file.log`

```BASH
> support_report.log 
> cron.log 
```

## Related documentation

- [Health notifications](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/dev-tools/integrations/health-notifications){target="_blank"}

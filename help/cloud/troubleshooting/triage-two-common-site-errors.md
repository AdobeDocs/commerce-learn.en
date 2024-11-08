---
title: Diagnose and fix a few common Commerce Cloud errors
description: Resolve two common Adobe Cloud project errors that prevent the site from loading.
feature: Cloud, Site Management
topic: Commerce, Development
role: Architect, Developer
level: Beginner, Intermediate
doc-type: Technical Video
duration: 260
last-substantial-update: 2024-10-30
jira: KT-16419
exl-id: 4c21b6a6-783a-422f-9071-3534ed68e8be
---
# Diagnose and fix service unavailable and an error occurred

Learn how to triage and resolve two common errors seen on Adobe Commerce Cloud projects.  Understand how and why these errors happen and what are the recommended steps to resolve them.

## Who is this video for

- Developers and IT Professionals
- System Administrators

## Video Content

- Diagnose and Resolve Storage Issues:
- Manage Maintenance Mode
- Efficient Troubleshooting tips

>[!VIDEO](https://video.tv.adobe.com/v/3435766?learn=on)


## Commands used in the video

Find the last 5 lines of the exception log mentioned in the response message.

```SHELL
 tail -n 5 ~/var/log/exception.log
```

To check hard drive space. Pay attention to the line dev/mapper/xxxx

```SHELL 
df -h
```

Lets find the top 15 largest files

```SHELL
find -type f -exec du -Sh {} + | sort -rh | head -n 15
```

Display the status of maintenance mode

```SHELL 
php bin/magento maintenance:status
```

Disable the maintenance mode

```SHELL
php bin/magento maintenance:disable 
```

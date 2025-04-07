---
title: - Detect IP addresses
description: Learn how to detect IP addresses for Adobe Commerce Cloud environments to enhance security and streamline server communication
feature: Cloud, Configuration
topic: Commerce, Development, Integrations
role: Developer
level: Beginner
doc-type: Technical Video
duration: 0
last-substantial-update: 2025-04-07
jira: KT-17553
---

# Learn how to detect IP addresses for all the types of environments in your Commerce Cloud project

Learn how to detect IP addresses for different environments in an Adobe Commerce Cloud project. By using a series of commands including Adobe Commerce CLI, sed, xargs, dig, grep, and sort -u, users can identify IP addresses for development, staging, and production environments.

## Who is this video for?

* Developers: looking to understand how to gather the IP addresses for the Adobe Commerce Cloud project.
* DevOps and security teams needing to restrict access to third party or backend systems 

## Video content {#video-content}

* Learn how to uncover the IP address for any environment in Adobe Commerce Cloud.

>[!VIDEO](https://video.tv.adobe.com/v/3457493/?learn=on)

## Command to get the IP address

Please note, you need to use your project ID and the environment name instead of the placeholder information.  There may also be a need to change the `{1..3}` to match the number of nodes in your Adobe Commerce Cloud cluster, but 3 is most common.

```bash
magento-cloud environment:url -p InsertYourProjectID -e UseYourEnvironmentName --pipe -1 | sed 's/.\.c\.(.)/\1/;s/.$//' | xargs -I% dig +short {1..3}."%" | grep '^\d' | sort -u
```

## Adobe Commerce Cloud CLI

```bash
magento-cloud environment:url -p InsertYourProjectID -e UseYourEnvironmentName --pipe -1
```

The magento-cloud CLI tool is designed to help developers and system administrators manage Adobe Commerce Cloud projects and environments efficiently. It extends the functionality of the Cloud Console, enabling users to perform routine tasks and run automation locally. Key features include managing integration environments, checking out and merging environments, listing variables, and using SSH to connect to remote environments. The tool simplifies workflows by allowing commands to be executed directly from the local workstation, enhancing the overall development and deployment process.

In this initial section of the example code, `magento-cloud environment:url -p InsertYourProjectID -e UseYourEnvironmentName --pipe -1` it is requesting the URL for the environment. The returned value looks something like this `http://integration-1ajmyuq-mk7xr7zmslfg.us-4.magentosite.cloud/`. Every once in a while it looks more like this `http://mcprod.russell.dummycachetest.com.c.abcikdxbg789.ent.magento.cloud/`.  This first command is rather simple, and now it's time to move along to the next command.

For more information, please read [Cloud CLI Overview](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/dev-tools/cloud-cli/cloud-cli-overview){target="_blank"}

## Using `sed` for search and replace

```bash
sed 's/.\.c\.(.)/\1/;s/.$//'
```

The command `sed` in UNIX&reg;Linux&reg; stands for Stream Editor. It is used to perform basic text transformations on an input stream (a file or input from a pipeline). Common uses include searching, finding and replacing, inserting, and deleting text. The command `sed` processes text line by line and applies specified operations, making it a powerful tool for text manipulation and scripting.

As mentioned earlier, there are typically 2 types of URLs returned from the `magento-cloud` cli. There is one variation which contains `.com.c.c` in the middle. This variant is the one which needs to be manipulated. If this structure is detected, it requires the removal everything starting from the beginning of the URL through `.com.c.c`.  Then, what is left is only the last part of the URL. An example URL looks like `http://mcprod.russell.dummycachetest.com.c.abcikdxbg789.ent.magento.cloud/`.  When this pattern is detected, the goal is to keep everything after `.c.`.  In this example code provided, `sed 's/.\.c\.(.)/\1/'` is used to grab this part and ignore the rest of the original returned value. The remaining part of the URL resembles something like `abcikdxbg789.ent.magento.cloud/`.  
There are two commands being executed in `sed`. They are separated by a semi-colon. The second part of my `sed` command `;s/.$//'` is to remove any trailing slashes if they exist, to clean up that URL to look like `abcikdxbg789.ent.magento.cloud`.  At this point, the URL has been cleaned up and ready for the next command.

## Xargs with dig

```bash
xargs -I% dig +short {1..3}."%"
```

The`xargs` command in UNIX&reg;Linux&reg; is used to build and execute command lines from standard input. It takes input from a pipe or a file and converts it into arguments for another command. It is particularly useful for handling large numbers of arguments that exceed the shell's limit. The command `xargs` can be used to perform operations like moving, copying, or deleting files. It allows for efficient batch processing by passing multiple arguments to commands in a single execution.

The `dig` command, short for Domain Information Groper, is a network administration tool used to query DNS (Domain Name System) servers. It helps retrieve information about DNS records, such as A, AAAA, MX, and CNAME records. The command `dig` is commonly used to troubleshoot DNS issues, verify DNS configurations, and gather detailed information about domain names and their associated IP addresses. By using various options and flags, users can customize the output to display specific details or a concise summary.

The use of `xargs` with `dig` makes it complicated, but it is necessary. The goal is to take that cleaned up URL and save it.  Once the URL is saved as the variable, it is inserted into the `dig` command.  

The command `dig` was created to gather DNS information. To reduce the amount of data that is returned, the argument `+short` is used. By using `dig` combined with `+short`, IP addresses and sometimes strings are returned.

In that part of the command, `xargs` will save that URL `abcikdxbg789.ent.magento.cloud` and is being inserted it into the next command `dig`. The technique of saving the URL combined with iteration, makes it easier to use with the `dig` command. Keep in mind that my sample code is one way to accomplish the goal, feel free to modify things to meet your needs and expectations.

At this point, the URL is ready. Next, let's see how it is possible to check each server in the cluster. For Adobe Commerce Cloud, each server in the cluster has a number. The server identifier is a prefix to the url that was just cleaned up and made ready for use. A quick and easy way to check off of the servers is by using `{1..3}`. By using `{1..3}` that notifies the `dig` command to be executed 3 times. The following is a representation of what happens if you were to watch the execution in real time.

```bash
dig +short 1.<projectid>.ent.magento.cloud
dig +short 2.<projectid>.ent.magento.cloud
dig +short 3.<projectid>.ent.magento.cloud
```

For better illustration purposes, this example URL being used by `dig` would resemble:

```bash
dig +short 1.aabcikdxbg789.ent.magento.cloud
dig +short 2.abcikdxbg789.ent.magento.cloud
dig +short 3.abcikdxbg789.ent.magento.cloud
```

If `{1..3}` was modified to be `{1..6}`, then it would look like this:

```bash
dig +short 1.aabcikdxbg789.ent.magento.cloud
dig +short 2.abcikdxbg789.ent.magento.cloud
dig +short 3.abcikdxbg789.ent.magento.cloud
dig +short 4.aabcikdxbg789.ent.magento.cloud
dig +short 5.abcikdxbg789.ent.magento.cloud
dig +short 6.abcikdxbg789.ent.magento.cloud
```

## The command `grep`

There are times when a string is returned as part of the result from `dig`. For this purpose, the goal is only IP addresses and they are made up of numbers with periods. To make sure the final output only contains numbers, it is possible to adjust the command. When completed, the final syntax is ` grep '^\d'`.  By adding `'^\d'`, the command `grep` only keeps numbers and disregard anything else. 

## The command `sort`

By using `sort -u`, it removes any duplicates from the list of IPs. Duplicates only happen when looking in development levels. 

These lower level environments are multi-tenant and share underlying servers with many other projects. Development environments are single servers, and never a cluster. Therefore, when the dig command is looping over each iteration, it returns the same IP many times. So, by using the command `sort -u`, all duplicate IPs are removed and only unique IP addresses remain. 



## Related Documentation

* [Regional IP Addresses](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/project/regional-ip-addresses|https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/project/regional-ip-addresses){target="_blank"}

---
title: Use Fastly to deny access to an entire website
description: Restrict Adobe Commerce Site Access with Fastly Edge ACLs and  a Custom VCL
feature: Cloud, Configuration, Site Management, System
topic: Administration,Commerce,Development, Security
role: Admin, Developer, User
level: Intermediate, Experienced
doc-type: Technical Video
duration: 200
last-substantial-update: 2025-07-11
jira: KT-18494
---

# Use Fastly to deny access for an entire website

Learn how to restrict access to your Adobe Commerce Cloud site using Fastly Edge ACLs and custom VCL snippets. This step-by-step guide helps you secure your pre-launch environment by allowing only specific IP addresses, ensuring your development site stays private. 

## What you'll learn

Restrict Adobe Commerce Site Access with Fastly Edge ACLs & Custom VCL | Secure Pre-Launch Environments

## Who is this video for?

* DevOps Engineer
* Adobe Commerce Developer
* Site Reliability Engineer

>[!VIDEO](https://video.tv.adobe.com/v/3464779/?learn=on&enablevpops)

## Code Sample

This is an example of the VCL used

```BASH
if ( !(client.ip ~ allowlist) && !req.http.Fastly-FF) { error 403 "Forbidden";}
```

## Related Documentation

* [Detecting malicious IP address](https://experienceleague.adobe.com/en/docs/commerce-learn/tutorials/tools/new-relic/malicious-ip)
* [Custom VCL for allowing requests](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/cdn/custom-vcl-snippets/fastly-vcl-allowlist)
* [Custom VCL for blocking requests](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/cdn/custom-vcl-snippets/fastly-vcl-blocking)
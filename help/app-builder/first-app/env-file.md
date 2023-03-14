---
title: The .env file
description: Learn about the types of files in the .env file for this sample application
landing-page-description: Learn about Adobe Developer App Builder used with Adobe Commerce and what types content is used in the .env file
kt: 12423
doc-type: tutorial
audience: all
last-substantial-update: 2023-03-13

---

# The `.env` file

This is a special file that is not part of the sample module, but is important for use in your Adobe Developer App Builder application. It contains secrets and other information that should not be committed to a repository. 

## Who is this video for?

* Developers new to Adobe Commerce with limited experience using Adobe App Builder who want to learn about the `.env` file.

## Video content

* Introduction to the .env file and its purpose
* How to generate the .env file
* How to append the file to add new secrets
* Avoid committing this file because it contains sensitive information

>[!VIDEO](https://video.tv.adobe.com/v/3416593)

## Code Sample

```bash
# Specify your secrets here
# This file must not be committed to source control
## Adobe I/O Runtime credentials
AIO_runtime_auth=abcd1234-aaa-bbb-ccc-12345:Abcdd12345asdfadsfadsfee2323232323232
AIO_runtime_namespace=12345-someworkspace-stage
AIO_runtime_apihost=https://adobeioruntime.net
## Adobe I/O Console service account credentials (JWT) Api Key
SERVICE_API_KEY=

# You can include some commerce OAUTH credentials too, our sample module will use this
#COMMERCE_BASE_URL=https://somecommercewebsite.com/
#COMMERCE_CONSUMER_KEY=abcebdme5bvafnemk0mdeeiyfq123
#COMMERCE_CONSUMER_SECRET=ffff86sqws3pss5hhuofiqgq4t04rrr11
#COMMERCE_ACCESS_TOKEN=gdddfccronj098r4m04zyq773s5o64
#COMMERCE_ACCESS_TOKEN_SECRET=ggg7nb19jhr5gi9jzfan9ggzipe8yrus
```

You can see these static values being used in the sample module in file `actions/commerce.index.js`

```javascript
        const oauth = getCommerceOauthClient(
            {
                url: params.COMMERCE_BASE_URL,
                consumerKey: params.COMMERCE_CONSUMER_KEY,
                consumerSecret: params.COMMERCE_CONSUMER_SECRET,
                accessToken: params.COMMERCE_ACCESS_TOKEN,
                accessTokenSecret: params.COMMERCE_ACCESS_TOKEN_SECRET
            },
            logger
        )

```

{{$include /help/_includes/app-builder-first-app-related-links.md}}

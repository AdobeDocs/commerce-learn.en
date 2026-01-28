---
title: Explore New Customer REST APIs
description: Discover how to use new customer REST APIs in Adobe Commerce Cloud Service. Ideal for architects and developers.
feature: REST, Customers, Saas
topic: Development, Integrations
role: Architect, Developer
level: Beginner
doc-type: Tutorial
duration: 225
last-substantial-update: 2026-01-27
jira: KT-20160
---

# Customer REST API

Learn to use new customer REST APIs in Adobe Commerce as a Cloud Service. This tutorial is perfect for architects and developers looking to integrate and optimize API solutions effectively.

## Who is this video for?

* Backend developers responsible for building integrations with Adobe Commerce
* Technical architects designing customer management workflows for headless commerce implementations

## Video content

* Authenticate with Adobe IMS using server-to-server credentials to obtain an access token for API requests
* Use the correct REST API endpoint format for Commerce as a Cloud Service
* Create and update customer accounts programmatically using POST and PUT requests with proper JSON payloads

>[!VIDEO](https://video.tv.adobe.com/v/3479361/?learn=on&enablevpops)

## Code samples

Before starting, gather all the required values from [Experience Cloud](https://experience.adobe.com) and the [Adobe Developer Console](https://developer.adobe.com/console). Having these values ready ensures a smooth setup process.

>[!NOTE]
>
>Make sure you are working in the correct organization. Your organization selection affects which instances and environments are visible in both Experience Cloud and the Developer Console.

### Instance details - experience.adobe.com

The instance details contain things like your Instance ID, GraphQL endpoints, credentials.

### Developer details - https://developer.adobe.com/console/

The Developer Console is where you manage your API credentials, including client IDs, client secrets, and access tokens. You can also create new credential types, such as Server-to-Server or Native App authentication.

## Prerequisites

| Item | Value | Where is this value |
|--- |--- |--- |
| Instance ID | `<instance_id>` | experience.adobe.com |
| REST Endpoint | `<rest_endpoint>` | experience.adobe.com |
| Client ID | `<client_id>` | developer.adobe.com/console |
| Client Secret | `<client_secret>` | developer.adobe.com/console |


## Step 1: Get Access Token (Server-to-Server Authentication)

>[!IMPORTANT]
>
> The variables shown in this sample are not valid. Use the <client_id> and <client_secret> from your project credentials.

```bash
curl -X POST 'https://ims-na1.adobelogin.com/ims/token/v3' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>&scope=openid,AdobeID,email,additional_info.projectedProductContext,profile,commerce.aco.ingestion,commerce.accs,org.read,additional_info.roles'
```

**Sample Response:**

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIs...",
  "token_type": "bearer",
  "expires_in": 86399
}
```

## Step 2: Create a Customer

>[!IMPORTANT]
>
> The URL provided in this sample is not valid. Use your REST base url. Exchange '<rest_endpoint>' with your URL. It looks  similar to this  `https://na1-sandbox.api.commerce.adobe.com/AbCYab34cdEfGHiJ27123`.
>
> This endpoint does not have /rest/ as part of the URL. Including that leads to an error.

**Endpoint:** `POST /V1/customers`

```bash
curl -X POST \
  "<rest_endpoint>/V1/customers" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -d '{
    "customer": {
      "email": "john.doe@example.com",
      "firstname": "John",
      "lastname": "Doe",
      "store_id": 1,
      "website_id": 1
    },
    "password": "TempPa55word!"
  }'
```

**Response:**

```json
{
  "id": 5,
  "group_id": 1,
  "created_at": "2026-01-23 20:40:15",
  "updated_at": "2026-01-23 20:40:15",
  "created_in": "Default Store View",
  "email": "john.doe@example.com",
  "firstname": "John",
  "lastname": "Doe",
  "store_id": 1,
  "website_id": 1,
  "addresses": [],
  "disable_auto_group_change": 0
}
```

## Step 3: Update a Customer

>[!IMPORTANT]
>
> The URL provided in this sample is not valid. Use your REST base url. Exchange '<rest_endpoint>' with your URL. It looks  similar to this  `https://na1-sandbox.api.commerce.adobe.com/AbCYab34cdEfGHiJ27123`.

The number `5` in the following example is the ID from the previously created customer using POST `"id": 5,`. Be sure to change`5` to whatever id was returned in your request.

**Endpoint:** `PUT /V1/customers/{customerId}`

```bash
curl -X PUT \
  "<rest_endpoint>/V1/customers/5" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -d '{
    "customer": {
      "id": 5,
      "email": "john.doe@example.com",
      "firstname": "John",
      "lastname": "Doe-Updated"
    }
  }'
```

**Response:**

```json
{
  "id": 5,
  "group_id": 1,
  "created_at": "2026-01-23 20:40:15",
  "updated_at": "2026-01-23 20:40:30",
  "created_in": "Default Store View",
  "email": "john.doe@example.com",
  "firstname": "John",
  "lastname": "Doe-Updated",
  "store_id": 1,
  "website_id": 1,
  "addresses": []
}
```

## Complete Script (All-in-One)

>[!IMPORTANT]
>
> The variables shown in this sample are not valid. Use the client ID and client secret from your project credentials. Use your REST base url. Exchange '<rest_endpoint>' with your REST endpoint URL from experience.adobe.com. It looks similar to this  `https://na1-sandbox.api.commerce.adobe.com/AbCDefGHiJ1234567`.

```bash
#!/bin/bash

# Configuration be sure to update these with your projects unique values
CLIENT_ID="<client_id>"
CLIENT_SECRET="<client_secret>"
REST_ENDPOINT="<rest_endpoint>"

# Step 1: Get Access Token
echo "Getting access token..."
ACCESS_TOKEN=$(curl -s -X POST 'https://ims-na1.adobelogin.com/ims/token/v3' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d "grant_type=client_credentials&client_id=${CLIENT_ID}&client_secret=${CLIENT_SECRET}&scope=openid,AdobeID,email,additional_info.projectedProductContext,profile,commerce.aco.ingestion,commerce.accs,org.read,additional_info.roles" | jq -r '.access_token')

echo "Token obtained: ${ACCESS_TOKEN:0:50}..."

# Step 2: Create Customer
echo ""
echo "Creating customer..."
CREATE_RESPONSE=$(curl -s -X POST \
  "${REST_ENDPOINT}/V1/customers" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -d '{
    "customer": {
      "email": "john.doe@example.com",
      "firstname": "John",
      "lastname": "Doe",
      "store_id": 1,
      "website_id": 1
    },
    "password": "TempPa55word!"
  }')

echo "Create Response:"
echo "$CREATE_RESPONSE" | jq .

# Extract customer ID
CUSTOMER_ID=$(echo "$CREATE_RESPONSE" | jq -r '.id')
echo "Customer ID: $CUSTOMER_ID"

# Step 3: Update Customer
echo ""
echo "Updating customer..."
curl -s -X PUT \
  "${REST_ENDPOINT}/V1/customers/${CUSTOMER_ID}" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -d "{
    \"customer\": {
      \"id\": ${CUSTOMER_ID},
      \"email\": \"john.doe@example.com\",
      \"firstname\": \"john\",
      \"lastname\": \"Doe-Updated\"
    }
  }" | jq .
```

## Important Notes about this tutorial

1. **URL Path**: Use `https://<server>.api.commerce.adobe.com/<tenant-id>/V1/customers` — **NOT** `https://<host>/rest/<store-view-code>/V1/customers`
1. **Authentication**: This tutorial used Server-to-Server (`client_credentials` grant type)
1. **Required Scope**: `commerce.accs`
1. **Token Expiry**: 86400 seconds (24 hours)

## References

* [Adobe Commerce as a Cloud Service Release Notes](https://experienceleague.adobe.com/en/docs/commerce/cloud-service/release-notes)
* [SaaS REST API Reference](https://developer.adobe.com/commerce/webapi/reference/rest/saas/)
* [User Authentication Guide](https://developer.adobe.com/commerce/webapi/rest/authentication/user/)

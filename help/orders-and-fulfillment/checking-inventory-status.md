---
title: Inventory status checks development and performance considerations
description: Learn some ideas and considerations for doing inventory status checks for Adobe Commerce.
feature: Best Practices, Inventory
topic: Development, Performance
role: Architect, Developer
level: Intermediate, Experienced
doc-type: Tutorial
duration: 0
last-substantial-update: 2024-05-09
jira: KT-15462
---

# Inventory status checks development and performance considerations

Accuracy with inventory to ensure the website does not oversell is a very important consideration. There are some native features that can help ensure this risk is as low as possible. A few of those are using backorders and setting the out of stock threshold. Both of those topics can be read on [Experience League](https://experienceleague.adobe.com/en/docs/commerce-admin/inventory/configuration/backorders) for further explanation.

There will be projects and instances where real time inventory status checks are requested for an Adobe Commerce store. This tutorial will provide insight for handling this conversation with development and performance considerations. 

## Validate if this request is absolutely necessary

Prepare to engage with the conversation with as much information as possible. First and foremost verfify that anything outside of the native functionality is a requirement for this project. Find the reasoning behind this request to validate that all of the native capabilities of Adobe Commerce fail to fulfil this request.

Another consideration is the cost to develop, test and maintain this feature. Just because some stakeholder thinks it is necessary, does not mean it is a requirement. There will be associated costs to doing inventory validation out side of the core functionality of Adobe Commerce.

## Determine what is an acceptable inventory update cadence

Try to consider this a 3 tier approach to inventory status checks.  

1. Using native functionality no changes/customizations needed
2. Near real time, meaning you have an integration that feeds commerce frequently to update its inventory on a schedule. For example every hour.
3. Live inventory checks to an external API or data source.

Work with the request for inventory update checks but validate what is a tolerable timeframe for when Adobe Commerce is updated with the latest inventory status. By doing frequent inventory updates to Adobe Commerce and still leveraging out of the box functionality, you reduce the amount of custom code and overall complexity for the store.

## Considerations when native inventory management functionality will not work

Keep the customizations as non-complex as possible.
How flat can the organization of the inventory be, is it just 1 sku and the total amount of available stock OR are there other attributes that need to be considered.

If the inventory information is fairly flat, for example a sku and the total available quantity, the options for near-real-time are expanded. Near real time means there is a background operation that gathers the inventory from the source, and then populates a storage engine to be used to respond to the request. For this you can use things such as Redis, Mongo, or other non-relational databases. These options are nice because they are very fast and work great for key/value pairs. If the data is a bit more complex, then using a relation database, either inside or outside the commerce application is likely to be required. By offloading this from the commerce database, you keep the core commerce application isolated from these transactions and save the I/O from the commerce application, CPU, RAM etc from use and leverage APIS to pull the data from the storage.  This will likely need a middleware to help transform any data and ensure that the calling application can get the result as expected, Adobe App Builder with API mesh is a good option and should be considered.

Using Adobe App Builder with API mesh is also a great option when there are multiple sources of inventory. 


## Moving the execution logic to an out-of-process location 

Taking advantage of a middleware solution will help with x,y, z.
Using App Builder and API mesh is a great start to this. ..

## When to do inventory checks

Encourage the minimal amount of times a product is required to find available inventory.  Keeping this down to product pages, cart and checkout is ideal.

## Research how the inventory source

Comprehensive investigation of the external inventory source is required. items that should be evaluated are available API options, support for GraphQL, and expected response times. If the inventory source has a limited bandwidth or was never intended to be used in a real time request, this will exclude this from being an option and you will have to consider near-real-time instead.  If the aPI request times will exceed the defined parameters  this will also exclude this from being a viable option.  An example of this would be api responses are 200ms for one a time requests, but rise to 500 to 900ms under moderate load.  This would likely just get worse with more load and will rule out live inventory calls from being available.

Be sure to test the api response times with simple requests as well as with a high volume similar to the expected traffic on the live website. Remember to test all areas from commerce at the same time to simulate real world scenarios.  If the expectation is a live inventory call should occur on product pages, when viewing and editing a cart and during checkout, the load testing needs to simulate all of these at the same to to mimic real customer behavior and the expectation for a store.

## Fallback options

IF the inventory source is down and monitoring is available, using the native capability of Adobe Commerce is recommended. However, with proper monitoring the customer experience can dynamically change to reflect the loss of real time inventory checks. This may mean that a sale or event is cancelled early or removed from display to avoid overselling. The expectation for what to do when the inventory source is down for any reason needs to be considered and discussed with the store owner so everyone is aware of any automatic process that take over in that unfortunate circumstance.



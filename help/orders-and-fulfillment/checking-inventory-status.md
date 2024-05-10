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

Accuracy with inventory is a very important consideration. There are some native features that can help ensure that this risk is as low as possible such as back orders and setting the out of stock threshold. Both of those topics can be read on [Experience League](https://experienceleague.adobe.com/en/docs/commerce-admin/inventory/configuration/backorders) for further explanation.

There are projects and use cases where real time inventory status checks are requested for an Adobe Commerce store. This tutorial provides insight for handling this conversation with development and performance considerations. 

## Validate if this request is absolutely necessary

Prepare to engage with the conversation with as much information as possible. The most important thing to do is to verify that native functionality is not acceptable for this project. Find the reasoning behind this request to validate that the native capabilities of Adobe Commerce fail to fulfill this request.

Another consideration is the cost to develop, test and maintain this feature. Just because some stakeholder thinks it is necessary, does not mean it is a requirement. There are associated costs with doing inventory validation out side of the core functionality of Adobe Commerce. These costs come at technical debt, more testing and validation as well as usage documentation and supporting documents for its architecture.

## Determine what is an acceptable inventory update cadence

Try to consider inventory checks and how it is accomplished in 3 categories. Each one has benefits and limitations. They do also increase in complexity and require more testing and thought for error handling. Remember when you decide to go a custom route, there are added responsibilities and considerations. A few examples would include a fallback process, monitoring, testing and troubleshooting fall to the development team. There will also need to be new supporting documentation, training and monitoring to ensure this can be supported entirely by the development team. Another side effect is that the development team has to completely own this process. Adobe support is unable to assist with this level of customization.

The first category is using the native functionality. Using native functionality is the least amount of risk and has many benefits. Taking this approach means you can rely on all existing documentation and tutorials that Adobe Commerce provides for the use of the feature. There are many aspects to inventory management so using what comes with the application should be the first consideration.  However, there are use cases where the data found in commerce at the time of the order may not be completely accurate.  For example, you allow sales outside the application.  This would require some sort of integration to keep the Adobe Commerce information as close to accurate as possible. If over-selling is not acceptable, then adding an out of stock threshold is a good method to stop the sale of items before you get to zero. The native sync functionality for Adobe Commerce is at a maximum of 1 time per day, so this may work for some use 

The second category would be near real time.  This still uses the native functionality however this includes some extra work to provide an integration that feeds commerce frequently to update its inventory on a schedule. For example every hour. This option needs some thought for how an integration may work, but using the "bulk api" and having some middleware do the transformation of the data and push it to commerce is a great approach. Look at using Adobe App Builder or similar platforms to do the bulk of the work and push the information to Adobe commerce on a more frequent cadence.

The third category and the most complex with the most amount of risk and responsibility is realtime Live inventory checks to an external API or data source. Doing a real-time inventory check to an external system is risky and has several other elements that need to be considered.   Here are just a small set of other things that need to be evaluated:

* Can the external system accept REST or GraphQL requests
* are there any limits to the endpoint such as X number of requests per minute that may not coincide with the website traffic
* What happens to the response time under load
* What happens when the response times are long, do you terminate this automatically and use a fallback option such as the native inventory.  
* What type of monitoring is available to ensure that API requests are within the tolerance limits

## Considerations when native inventory management functionality will not work

Keep the customizations as non-complex as possible.
How flat can the organization of the inventory be, is it just 1 sku and the total amount of available stock OR are there other attributes that need to be considered.

If the inventory information is fairly flat, for example a sku and the total available quantity, the options for near-real-time are expanded. Near real time means that there is a background operation that gathers the inventory from the source, and then populates a storage engine to be used to respond to the request. For this you can use things such as Redis, Mongo, or other non-relational databases. These options are nice because they are very fast and work great for key/value pairs. If the data is a bit more complex, then using a relation database, either inside or outside the commerce application, is likely to be required. By offloading this from the commerce database, you keep the core commerce application isolated from these transactions and save the I/O from the commerce application, CPU, RAM etc. from use and leverage APIS to pull the data from the storage.  This will likely need a middleware to help transform any data and ensure that the calling application can get the result as expected, Adobe App Builder with API mesh is a good option and should be considered.

Using Adobe App Builder with API mesh is also a great option when there are multiple sources of inventory. 


## Moving the execution logic to an out-of-process location 

Adobe Developer App Builder provides a unified third-party extensibility framework for integrating and creating custom experiences to extend Adobe solutions. Adobe Commerce can use Adobe Developer App Builder. This would be an excellent use case for extending some functionality that normally occurs in the core application and moves it off-site. By removing functionality from the Commerce application this reduces the number of modules and complexity to the Commerce application.  In turn, lower numbers of in-process customizations reduce the complexity for upgrading and maintenance.

NEED MORE INFORMATION

## When to do inventory checks

Encourage the minimal number of times a product is required to find available inventory.  Keeping this down to product pages, cart and checkout are ideal.

EXPAND ON THIS

## Research how the inventory source

Comprehensive investigation of the external inventory source is required. Items that should be evaluated are available API options, support for GraphQL, and expected response times. If the inventory source has a limited bandwidth or was never intended to be used in a real time request, this excludes this from being an option and you have to consider near-real-time instead.  If the aPI request times exceed the defined parameters this will also exclude this from being a viable option.  An example of this would be api responses are 200MS&reg; for one a time requests, but rise to 500 to 900MS&reg; under moderate load.  This would likely just get worse with more load and will rule out live inventory calls from being available.

Be sure to test the api response times with simple requests as well as with a high volume similar to the expected traffic on the live website. Remember to test all areas from commerce at the same time to simulate real world scenarios.  If the expectation is a live inventory call should occur on product pages, when viewing and editing a cart and during checkout, the load testing needs to simulate all of these at the same time to mimic real customer behavior and the expectation for a store.

## Fallback options

IF the inventory source is down and monitoring is available, using the native capability of Adobe Commerce is recommended. However, with proper monitoring the customer experience can dynamically change to reflect the loss of real time inventory checks. This may mean that a sale or event is canceled early or removed from display to avoid overselling. The expectation for what to do when the inventory source is down for any reason needs to be considered and discussed with the store owner so everyone is aware of any automatic process that takes over in that unfortunate circumstance.


## Conclusion

The decision to do real-time inventory checks is a significant one. Ensuring that the website owner, development team, and others are fully educated and aware of all gains and potential pitfalls rest on the developer lead or architect. By providing a thoughtful plan that covers reasons and a fallback process is key to success.

NEED MORE HERE

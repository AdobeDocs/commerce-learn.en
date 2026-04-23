---
title: Create Cart Price Rules
description: Learn how to create cart price rules that apply discounts in the shopping cart when conditions you define are met.
doc-type: Tutorial
last-substantial-update: 2022-12-28T00:00:00.000Z
feature: Configuration, System, Customers, Shopping Cart
topic: Commerce, Administration
role: User
level: Beginner
duration: 353
jira: KT-17148
exl-id: ae8cab73-8a8b-4266-8205-b7397633e9bf
TQID: https://experienceleague.adobe.com/2gmoGQBVz2foQwnGJRlXzWF-OkNGZtiJkQWy0F-0utg
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: d1e21356-0064-4f48-9089-16e3f0dbd2a6
    internal-label: Storefront
  - id: dac87252-6066-4d6e-a9d2-f6d84c323de7
    internal-label: Configuration
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: f8a45b24-4be7-4f1b-909b-60d06b483a20
    internal-label: Leader
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Create Cart Price Rules

Cart price rules apply discounts to items in the shopping cart based on conditions you set. The discount can apply automatically when conditions are met, or when the customer enters a valid coupon code. The discount appears in the cart under the subtotal. You can turn a rule on or off for a season or promotion by changing its status and date range.

## Who is this video for?

* eCommerce marketers
* Website managers

## Video content

* Create cart price rules and optional coupon codes.
* See how discounts appear in the cart and for promotions.

>[!VIDEO](https://video.tv.adobe.com/v/343835?learn=on)

## Pricing display issues

In some cases, each line item must show the discount applied, but displayed values may not match exactly. This happens when a cart price rule applies one discount across multiple products and the split does not divide evenly to two decimal places.

>[!BEGINSHADEBOX]

Cart Price Rule = 10% discount applied to 2 products in the cart
Condition for price rule to take effect: total items in cart is 2
Actions apply percent of product price discount and that discount amount is 10

2 items are added to the cart, each are $19.95

To get the discount amount multiply the product price times 0.1

19.95 x 0.1 = 1.995

This is the issue, we have 3 decimal places, instead of two. Converting this to dollars is now a problem

>[!ENDSHADEBOX]

### The solution

For the merchant in the Admin, the clearest approach is to show each ordered line with its discount in dollars. To keep the order total correct, round the first line item up and drop the third decimal on the remaining line items. Review this scenario:

>[!BEGINSHADEBOX]

Same 10% discount as above cart rule in effect
Add 2 products to the cart that are 19.95

Each product should get $1.995 in discounts
Product 1 - 19.95 x 0.1 = 1.995
2 - 19.95 x 0.1 = 1.995

A grand total of 3.99 is provided as a discount to the customer

When displaying the line items to the store owner in the admin,
we need to adjust the first item and round it up to 2.000. For the second item, drop the third decimal.
Product 1 = 2.00
Product 2 = 1.99

The total discount of the two products now when summed together matches the actual discount provided to a customer.
>[!ENDSHADEBOX]

Here is a screenshot as it would show in the admin for an order that has this scenario:

![Admin view showing ordered items with different values](../assets/commerce-admin-cart-price-rule-values-different.png)

### Other potential solutions and why they were not used

>[!BEGINSHADEBOX]

Same 10% discount as above cart rule in effect
Add 2 products to the cart that are 19.95

Each product should get $1.995 in discounts,
however if we just round them up, it shows too much discount.

Product 1 - 19.95 x 0.1 = 1.995
Product 2 - 19.95 x 0.1 = 1.995

Convert to round up all items
Product 1 New value is 2.00
Product 2 New value is 2.00

A grand total of 3.99 was actually provided as a discount to the customer,
however if we round up, it would show that $4.00 was given, and that is incorrect.

2.00 + 2.00 = $4.00

>[!ENDSHADEBOX]

Similar issue if the third decimal was dropped for all items, it would show too little discount provided.

>[!BEGINSHADEBOX]

Same 10% discount as above cart rule in effect
Add 2 products to the cart that are 19.95

Each product should get $1.995 in discounts, however if we just drop the third decimal, this happens:
Product 1 - 19.95 x 0.1 = 1.995
Product 2 - 19.95 x 0.1 = 1.995

Convert to drop the third decimal for all items
Product 1 New value is 1.99
Product 2 New value is 1.99

A grand total of 3.99 was actually provided as a discount to the customer,
however if we drop the third decimal, it would show that $3.98 was given, and that is incorrect.

1.99 + 1.99 = $3.98

>[!ENDSHADEBOX]

## Additional resources

* [Create a Cart Price Rule - [!DNL Commerce] Merchandising and Promotions Guide](https://experienceleague.adobe.com/docs/commerce-admin/marketing/promotions/cart-rules/price-rules-cart-create.html){target="_blank"}
* [Coupon Codes - [!DNL Commerce] Merchandising and Promotions Guide](https://experienceleague.adobe.com/docs/commerce-admin/marketing/promotions/cart-rules/price-rules-cart-coupon.html){target="_blank"}

# Acceptance criteria (Given / When / Then)

## OGD-4 – Browse Grocery Categories

Given the customer is on the home page, When the customer selects a grocery category, Then the application displays products belonging to that category.

## OGD-5 – Search Grocery Products (positive)

Given the customer is on the product search page, When the customer enters a valid product name and submits the search, Then matching products are displayed.

## OGD-5 – Search Grocery Products (negative)

Given the customer enters a product name that has no matching items, When the search is submitted, Then the application displays a clear “No products found” message and does not show unrelated products.

## OGD-8 – Add Products to Cart

Given a product is available, When the customer selects Add to Cart, Then the product is added to the cart and the cart quantity/count is updated.

## OGD-11 – Complete Checkout

Given the cart contains at least one item, When the customer provides valid delivery details and confirms checkout, Then the application displays an order summary for confirmation.

## OGD-13 – Make Secure Payment

Given an order is ready for payment, When the customer completes a valid payment, Then the transaction result is recorded and the customer receives a payment confirmation.


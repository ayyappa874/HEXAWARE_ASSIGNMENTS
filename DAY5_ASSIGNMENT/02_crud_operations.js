// Insert five ProductReviews documents
db.ProductReviews.insertMany([
  { SKU: "P101", Customer_Name: "Rahul", Rating: NumberInt(5), Review: "Excellent laptop with good performance" },
  { SKU: "P102", Customer_Name: "Priya", Rating: NumberInt(4), Review: "Good wireless mouse" },
  { SKU: "P103", Customer_Name: "Arun", Rating: NumberInt(3), Review: "Average keyboard quality" },
  { SKU: "P104", Customer_Name: "Sneha", Rating: NumberInt(5), Review: "Excellent monitor" },
  { SKU: "P105", Customer_Name: "Kiran", Rating: NumberInt(4), Review: "Useful USB-C hub" }
]);

// Find all reviews and product-specific review
db.ProductReviews.find({});
db.ProductReviews.find({ SKU: "P101" });

// Update one review
db.ProductReviews.updateOne(
  { SKU: "P101", Customer_Name: "Rahul" },
  { $set: { Rating: NumberInt(4), Review: "Good laptop performance" } }
);

// Delete one review
db.ProductReviews.deleteOne({ SKU: "P103", Customer_Name: "Arun" });

// Verify remaining documents
db.ProductReviews.find({});

// Day 6 – Set 1: Retail Sales Reporting
// Database: RetailInventoryDB | Collection: reviews
use("RetailInventoryDB");

// Pipeline 1: Count reviews by rating (ratings >= 4)
db.reviews.aggregate([
  { $match: { Rating: { $gte: 4 } } },
  { $group: { _id: "$Rating", TotalReviews: { $sum: 1 } } },
  { $sort: { _id: -1 } }
]);

// Pipeline 2: Average rating by product (ratings >= 3)
db.reviews.aggregate([
  { $match: { Rating: { $gte: 3 } } },
  { $group: { _id: "$SKU", AverageRating: { $avg: "$Rating" } } },
  { $sort: { AverageRating: -1 } }
]);

// Pipeline 3: Customers who gave 5-star reviews
db.reviews.aggregate([
  { $match: { Rating: 5 } },
  { $group: { _id: "$CustomerName", TotalReviews: { $sum: 1 } } },
  { $sort: { TotalReviews: -1 } }
]);

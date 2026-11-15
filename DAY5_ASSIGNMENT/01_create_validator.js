// Run in mongosh. If ProductReviews already exists, use the collMod block below.
db.createCollection("ProductReviews", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["SKU", "Customer_Name", "Rating", "Review"],
      properties: {
        SKU: { bsonType: "string" },
        Customer_Name: { bsonType: "string" },
        Rating: { bsonType: "int", minimum: 1, maximum: 5 },
        Review: { bsonType: "string" }
      }
    }
  },
  validationLevel: "strict",
  validationAction: "error"
});

// If the collection already exists, apply validator:
// db.runCommand({
//   collMod: "ProductReviews",
//   validator: { $jsonSchema: {
//     bsonType: "object",
//     required: ["SKU", "Customer_Name", "Rating", "Review"],
//     properties: {
//       SKU: { bsonType: "string" },
//       Customer_Name: { bsonType: "string" },
//       Rating: { bsonType: "int", minimum: 1, maximum: 5 },
//       Review: { bsonType: "string" }
//     }
//   }},
//   validationLevel: "strict",
//   validationAction: "error"
// });

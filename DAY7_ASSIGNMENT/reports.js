// PART F – MONGODB COLLECTIONS AND SAMPLE DATA
// F.1 Database, hubs, carriers and customers
use LogisticsDB
db.hubs.insertMany([   { HubID:1, HubName:"Chennai Hub",   City:"Chennai" },
{ HubID:2, HubName:"Bangalore Hub", City:"Bangalore" },
{ HubID:3, HubName:"Hyderabad Hub", City:"Hyderabad" },
{ HubID:4, HubName:"Mumbai Hub",    City:"Mumbai" },
{ HubID:5, HubName:"Delhi Hub",     City:"Delhi" } ]);
db.carriers.insertMany([   { CarrierID:1, CarrierName:"BlueDart" },
{ CarrierID:2, CarrierName:"DTDC" },
{ CarrierID:3, CarrierName:"Delhivery" },
{ CarrierID:4, CarrierName:"DHL" },
{ CarrierID:5, CarrierName:"FedEx" } ]);
db.customers.insertMany([   { CustomerID:1, CustomerName:"Arun",  City:"Chennai" },
{ CustomerID:2, CustomerName:"Priya", City:"Bangalore" },
{ CustomerID:3, CustomerName:"Kavin", City:"Hyderabad" },
{ CustomerID:4, CustomerName:"Divya", City:"Mumbai" },
{ CustomerID:5, CustomerName:"Ravi",  City:"Delhi" }
]);
// F.2 Shipments
db.shipments.insertMany([   { ShipmentID:1001, CustomerID:1, HubID:1, CarrierID:1, ShippingCost:500,     ExpectedDeliveryDate:ISODate("2026-10-03"), ActualDeliveryDate:ISODate("2026-10-03") },
{ ShipmentID:1002, CustomerID:2, HubID:2, CarrierID:2, ShippingCost:700,     ExpectedDeliveryDate:ISODate("2026-10-04"), ActualDeliveryDate:ISODate("2026-10-08") },
{ ShipmentID:1003, CustomerID:3, HubID:3, CarrierID:3, ShippingCost:900,     ExpectedDeliveryDate:ISODate("2026-10-05"), ActualDeliveryDate:ISODate("2026-10-09") },
{ ShipmentID:1004, CustomerID:4, HubID:1, CarrierID:1, ShippingCost:400,     ExpectedDeliveryDate:ISODate("2026-10-06"), ActualDeliveryDate:ISODate("2026-10-06") },
{ ShipmentID:1005, CustomerID:5, HubID:2, CarrierID:4, ShippingCost:1200,     ExpectedDeliveryDate:ISODate("2026-10-07"), ActualDeliveryDate:ISODate("2026-10-10") },
{ ShipmentID:1006, CustomerID:1, HubID:3, CarrierID:2, ShippingCost:600,     ExpectedDeliveryDate:ISODate("2026-10-08"), ActualDeliveryDate:ISODate("2026-10-08") },
{ ShipmentID:1007, CustomerID:2, HubID:4, CarrierID:3, ShippingCost:800,
{ ShipmentID:1008, CustomerID:3, HubID:1, CarrierID:1, ShippingCost:1500,
{ ShipmentID:1009, CustomerID:4, HubID:2, CarrierID:4, ShippingCost:1100,     ExpectedDeliveryDate:ISODate("2026-10-11"), ActualDeliveryDate:ISODate("2026-10-11") },
{ ShipmentID:1010, CustomerID:1, HubID:2, CarrierID:1, ShippingCost:650,     ExpectedDeliveryDate:ISODate("2026-10-14"), ActualDeliveryDate:ISODate("2026-10-14") },
{ ShipmentID:1011, CustomerID:1, HubID:4, CarrierID:2, ShippingCost:750,
{ ShipmentID:1012, CustomerID:1, HubID:5, CarrierID:3, ShippingCost:850,
]);
// F.3 Delivery events
db.delivery_events.insertMany([   { EventID:1, ShipmentID:1001, EventType:"Picked Up",  Location:"Chennai" },
{ EventID:2, ShipmentID:1001, EventType:"Delivered",  Location:"Chennai" },
{ EventID:3, ShipmentID:1002, EventType:"In Transit", Location:"Bangalore" },
{ EventID:4, ShipmentID:1003, EventType:"Delivered",  Location:"Hyderabad" },
{ EventID:5, ShipmentID:1004, EventType:"Delivered",  Location:"Mumbai" },
{ EventID:6, ShipmentID:1005, EventType:"Delivered",  Location:"Delhi" },
{ EventID:7, ShipmentID:1006, EventType:"Delivered",  Location:"Bangalore" },   { EventID:8, ShipmentID:1008, EventType:"Delivered",  Location:"Mumbai" }
]);
// Figure 6. MongoDB Compass Mongosh showing the data insert, verification commands and the entered aggregation commands. The screenshot does not display the final result documents.
// PART G – THREE MONGODB $lookup AGGREGATION PIPELINES
// Pipeline 1 – Shipments with delivery events
db.shipments.aggregate([   {     $lookup: {       from: "delivery_events",       localField: "ShipmentID",       foreignField: "ShipmentID",       as: "DeliveryEvents"     }
}
]);
// Pipeline 2 – Customers with their shipments
db.customers.aggregate([   {     $lookup: {       from: "shipments",       localField: "CustomerID",       foreignField: "CustomerID",       as: "CustomerShipments"     }
}
]);
// Figure 7. MongoDB Compass Mongosh showing the LogisticsDB shell and the first two aggregation commands.
// Pipeline 3 – Carriers with delivery delay statistics
db.carriers.aggregate([   {     $lookup: {       from: "shipments",       let: { carrierId: "$CarrierID" },       pipeline: [         {
$match: {
$expr: {
$and: [
{ $eq: ["$CarrierID", "$$carrierId"] },
{ $ne: ["$ActualDeliveryDate", null] }
]
}
}
},
{
$set: {
}
}
},
{
$group: {
}
},
{
$project: {
}
}       ],       as: "DelayStatistics"     }
}
]);
// This pipeline joins each carrier to its shipments, calculates delay in days for shipments with an actual delivery date, and returns the total count, average delay and maximum delay in the DelayStatistics array.
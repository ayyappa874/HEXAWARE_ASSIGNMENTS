// Display all events
db.LoginEvents.find();

// Successful login events
db.LoginEvents.find({ status: "Success" });

// Failed login events
db.LoginEvents.find({ status: "Failed" });

// Count capped collection documents
db.LoginEvents.countDocuments();

// Last five login events for user/customer 1, newest first
db.LoginEvents.find({ user_id: 1 })
  .sort({ login_time: -1 })
  .limit(5);

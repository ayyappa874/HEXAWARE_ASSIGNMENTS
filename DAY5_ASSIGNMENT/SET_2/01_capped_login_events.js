// Run in mongosh. Drop/recreate to ensure capped configuration.
use BankBranchDB
db.LoginEvents.drop();

db.createCollection("LoginEvents", {
  capped: true,
  size: 100000,
  max: 20
});

// Insert 20 login-event documents; statuses alternate Success/Failed
for (let i = 1; i <= 20; i++) {
  db.LoginEvents.insertOne({
    user_id: i,
    username: "user" + i,
    login_time: new Date(),
    status: i % 2 === 0 ? "Success" : "Failed",
    ip_address: "192.168.1." + i
  });
}

db.LoginEvents.countDocuments(); // expected 20

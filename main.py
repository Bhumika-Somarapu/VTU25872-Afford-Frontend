from datetime import datetime
notifications = [
    { "id" : 1,"type": "Placement" ,
     "message":"Amazon Hiring","timestamp":"2026-06-14 10:00:00" },
    { "id" : 2,"type": "Event" ,
     "message":"Tech Fest","timestamp":"2026-06-14 09:00:00" },
    { "id" : 3,"type": "Result" ,
     "message":"Mid Exam Result","timestamp":"2026-06-14 08:00:00" },
    { "id" : 4,"type": "Placement" ,
     "message":"Google Hiring","timestamp":"2026-06-13 18:00:00" },
]
priority_weight = {
    "Placement" : 3,
    "Result" : 2,
    "Event" :1   
}
for notification in notifications:
    notification["score"] = (
        priority_weight[notification["type"]],
        datetime.strptime(
            notification["timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )
    )
top_notifications = sorted(
    notifications,
    key=lambda x: x["score"],
    reverse = True
)[:10]
print("Top Priority Notifications:\n")
for n in top_notifications:
    print(
        f"ID: {n['id']} | "
        f"Type: {n['type']} | "
        f"Message: {n['message']} | "
        f"Time: {n['timestamp']}"
    )
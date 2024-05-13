from plyer import notification

title = "Important!"
message = "Kushal drink water"

notification.notify(
    title=title,
    message=message,
    app_name="Python Notification",
    timeout=10  
)

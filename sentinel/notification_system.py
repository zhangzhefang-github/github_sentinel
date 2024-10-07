class NotificationSystem:
    def __init__(self, config):
        self.notification_type = config['notification_type']  # Email, Slack等

    def send_notification(self, report):
        # 根据配置发送通知，可以是邮件或其他通知方式
        if self.notification_type == "email":
            self.send_email(report)
        elif self.notification_type == "slack":
            self.send_slack_message(report)

    def send_email(self, report):
        print(f"Sending email with report: {report}")

    def send_slack_message(self, report):
        print(f"Sending Slack message with report: {report}")

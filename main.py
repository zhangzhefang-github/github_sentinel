from sentinel.subscription_manager import SubscriptionManager
from sentinel.update_fetcher import UpdateFetcher
from sentinel.notification_system import NotificationSystem
from sentinel.report_generator import ReportGenerator
import yaml

def load_config():
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config

if __name__ == "__main__":
    # 加载配置文件
    config = load_config()

    # 初始化模块
    subscription_manager = SubscriptionManager(config)
    update_fetcher = UpdateFetcher(config)
    notification_system = NotificationSystem(config)
    report_generator = ReportGenerator(config)

    # 获取更新并处理
    repos = subscription_manager.get_subscribed_repos()
    updates = update_fetcher.fetch_updates(repos)
    
    # 生成报告并通知
    report = report_generator.generate_report(updates)
    notification_system.send_notification(report)

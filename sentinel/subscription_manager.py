class SubscriptionManager:
    def __init__(self, config):
        self.config = config
        self.subscriptions = []  # 可以从数据库或文件读取订阅数据

    def get_subscribed_repos(self):
        # 从订阅列表中获取所有订阅的仓库
        return self.subscriptions

    def add_subscription(self, repo):
        # 添加新的GitHub仓库订阅
        self.subscriptions.append(repo)

    def remove_subscription(self, repo):
        # 移除GitHub仓库订阅
        self.subscriptions.remove(repo)

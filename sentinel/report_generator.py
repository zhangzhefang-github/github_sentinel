class ReportGenerator:
    def __init__(self, config):
        self.template = config['report_template']

    def generate_report(self, updates):
        report = "GitHub Sentinel Updates Report\n"
        for repo, commits in updates.items():
            report += f"\nRepository: {repo}\n"
            for commit in commits:
                report += f"- {commit['commit']['message']} by {commit['commit']['author']['name']}\n"
        return report

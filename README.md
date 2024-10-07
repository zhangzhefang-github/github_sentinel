# GitHub Sentinel

**GitHub Sentinel** is an open-source AI-powered tool designed to automate the tracking and reporting of GitHub repository activities. It allows developers and project managers to subscribe to repositories and receive notifications for updates such as commits, issues, and pull requests. GitHub Sentinel significantly enhances team collaboration by providing timely insights into repository changes.

## Key Features

- **Subscription Management**: Easily subscribe to and manage multiple GitHub repositories.
- **Automated Updates**: Fetch the latest commits and activities from subscribed repositories via the GitHub API.
- **Notification System**: Automatically send notifications (via email or Slack) for summarized repository updates.
- **Report Generation**: Generate detailed reports summarizing changes across repositories.
- **Configurable Frequency**: Set the update frequency (daily or weekly) based on project needs.
- **Open Source and Extensible**: Fully customizable to suit different team requirements.

## Getting Started

Follow the instructions below to set up and run GitHub Sentinel on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/github_sentinel.git
   cd github_sentinel
   ```
2. **Install dependencies:**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure your settings:**
- Navigate to the config/config.yaml file.
- Replace "your_github_token_here" with your actual GitHub API Token to allow API access.
- Set your desired notification method (email or slack) and configure report templates.
### Example config/config.yaml:
  ```
  github_token: "your_github_token_here"
  notification_type: "email"  # or 'slack'
  report_template: "default_template"
  ```


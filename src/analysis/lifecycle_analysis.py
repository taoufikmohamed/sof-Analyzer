import requests
import os
from dotenv import load_dotenv

class LifecycleAnalyzer:
    def __init__(self, repo_url):
        self.repo_url = repo_url
        load_dotenv()
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.repo_data = self.fetch_repo_data()
        self.commits_data = self.fetch_commits_data()
        self.issues_data = self.fetch_issues_data()
        self.branches_data = self.fetch_branches_data()
        print(f"\nAnalyzing repository: {self.repo_url}")
        print(f"Repository details:")
        print(f"- Name: {self.repo_data.get('name', 'N/A')}")
        print(f"- Owner: {self.repo_data.get('owner', {}).get('login', 'N/A')}")
        print(f"- Description: {self.repo_data.get('description', 'N/A')}")
        print(f"- Stars: {self.repo_data.get('stargazers_count', 0)}")
        print(f"- Forks: {self.repo_data.get('forks_count', 0)}\n")

    def fetch_repo_data(self):
        # Format GitHub API URL
        owner, repo = self.repo_url.split('/')[-2:]
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        
        # Set up headers with authentication
        headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }

        # Make API request
        response = requests.get(api_url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise Exception(f"Repository not found: {self.repo_url}")
        else:
            raise Exception(f"GitHub API error: {response.status_code} - {response.text}")

    def fetch_commits_data(self):
        owner, repo = self.repo_url.split('/')[-2:]
        api_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
        headers = {'Authorization': f'token {self.github_token}'}
        response = requests.get(api_url, headers=headers)
        return response.json() if response.status_code == 200 else []

    def fetch_issues_data(self):
        owner, repo = self.repo_url.split('/')[-2:]
        api_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
        headers = {'Authorization': f'token {self.github_token}'}
        response = requests.get(api_url, headers=headers)
        return response.json() if response.status_code == 200 else []

    def fetch_branches_data(self):
        owner, repo = self.repo_url.split('/')[-2:]
        api_url = f"https://api.github.com/repos/{owner}/{repo}/branches"
        headers = {'Authorization': f'token {self.github_token}'}
        response = requests.get(api_url, headers=headers)
        return response.json() if response.status_code == 200 else []

    def fetch_pull_requests(self):
        owner, repo = self.repo_url.split('/')[-2:]
        api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=all"
        headers = {'Authorization': f'token {self.github_token}'}
        response = requests.get(api_url, headers=headers)
        return response.json() if response.status_code == 200 else []

    def fetch_review_comments(self, pr_number):
        owner, repo = self.repo_url.split('/')[-2:]
        api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/comments"
        headers = {'Authorization': f'token {self.github_token}'}
        response = requests.get(api_url, headers=headers)
        return response.json() if response.status_code == 200 else []

    def analyze_lifecycle(self, project_data):
        analysis_results = {
            "planning": self.analyze_planning(project_data),
            "development": self.analyze_development(project_data),
            "testing": self.analyze_testing(project_data),
            "deployment": self.analyze_deployment(project_data),
            "maintenance": self.analyze_maintenance(project_data),
            "code_reviews": self.analyze_code_reviews()
        }
        return analysis_results

    def analyze_planning(self, project_data):
        # Analyze planning stage
        return {"status": "completed", "details": "Planning phase is completed."}

    def analyze_development(self, project_data):
        # Analyze development stage
        return {"status": "in progress", "details": "Development is ongoing."}

    def analyze_testing(self, project_data):
        # Analyze testing stage
        return {"status": "not started", "details": "Testing phase has not begun."}

    def analyze_deployment(self, project_data):
        # Analyze deployment stage
        return {"status": "pending", "details": "Deployment is scheduled."}

    def analyze_maintenance(self, project_data):
        # Analyze maintenance stage
        return {"status": "not applicable", "details": "No maintenance required yet."}

    def analyze_git_metrics(self):
        return {
            "status": "analyzed",
            "details": f"Total commits: {len(self.commits_data)}, Active branches: {len(self.branches_data)}",
            "metrics": {
                "commit_frequency": len(self.commits_data),
                "branch_count": len(self.branches_data),
                "issue_count": len(self.issues_data)
            }
        }

    def analyze_ci_cd(self):
        workflows_path = ".github/workflows"
        has_ci = any(file.endswith('.yml') for file in os.listdir(workflows_path)) if os.path.exists(workflows_path) else False
        return {
            "status": "configured" if has_ci else "missing",
            "details": "CI/CD workflows found" if has_ci else "No CI/CD configuration detected"
        }

    def analyze_code_quality(self):
        # Add code quality metrics (could integrate with SonarQube or similar tools)
        return {
            "status": "pending",
            "details": "Code quality analysis required",
            "suggested_tools": ["SonarQube", "ESLint", "Pylint"]
        }

    def analyze_testing_coverage(self):
        test_files = self.count_test_files()
        return {
            "status": "adequate" if test_files > 0 else "inadequate",
            "details": f"Found {test_files} test files",
            "coverage_metrics": {
                "test_files": test_files,
                "coverage_percentage": "Unknown"
            }
        }

    def count_test_files(self):
        test_count = 0
        for root, _, files in os.walk(os.path.dirname(self.repo_url)):
            test_count += sum(1 for f in files if 'test' in f.lower())
        return test_count

    def analyze_security(self):
        return {
            "status": "review_needed",
            "details": "Security analysis recommended",
            "checks": [
                "Dependency scanning",
                "SAST analysis",
                "Container scanning",
                "Secret detection"
            ]
        }

    def analyze_code_reviews(self):
        pull_requests = self.fetch_pull_requests()
        review_metrics = {
            'total_prs': len(pull_requests),
            'reviewed_prs': 0,
            'total_comments': 0,
            'avg_review_time': 0,
            'reviewers': set()
        }

        for pr in pull_requests:
            if pr.get('review_comments', 0) > 0:
                review_metrics['reviewed_prs'] += 1
                review_metrics['total_comments'] += pr['review_comments']
                review_metrics['reviewers'].update([review['user']['login'] for review in self.fetch_review_comments(pr['number'])])
                
                # Calculate review time
                created = datetime.strptime(pr['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                closed = datetime.strptime(pr['closed_at'], '%Y-%m-%dT%H:%M:%SZ') if pr['closed_at'] else datetime.now()
                review_metrics['avg_review_time'] += (closed - created).days

        if review_metrics['reviewed_prs'] > 0:
            review_metrics['avg_review_time'] /= review_metrics['reviewed_prs']

        return {
            'status': 'analyzed',
            'metrics': review_metrics,
            'details': f"Found {review_metrics['total_prs']} PRs, {review_metrics['reviewed_prs']} reviewed"
        }

    def generate_review_report(self, review_analysis):
        metrics = review_analysis['metrics']
        report = "\nCode Review Analysis\n"
        report += "=" * 20 + "\n"
        report += f"Total Pull Requests: {metrics['total_prs']}\n"
        report += f"Reviewed PRs: {metrics['reviewed_prs']}\n"
        report += f"Total Review Comments: {metrics['total_comments']}\n"
        report += f"Average Review Time: {metrics['avg_review_time']:.1f} days\n"
        report += f"Number of Reviewers: {len(metrics['reviewers'])}\n"
        return report

    def generate_report(self, analysis_results):
        report = f"Software Lifecycle Analysis Report for {self.repo_url}\n"
        report += "=" * 50 + "\n\n"
        
        # Basic stages
        for stage, result in analysis_results.items():
            report += f"{stage.capitalize()}: {result['status']} - {result['details']}\n"
        
        # Git metrics
        git_metrics = self.analyze_git_metrics()
        report += f"\nGit Metrics:\n{'-' * 20}\n"
        report += f"Commits: {git_metrics['metrics']['commit_frequency']}\n"
        report += f"Branches: {git_metrics['metrics']['branch_count']}\n"
        report += f"Issues: {git_metrics['metrics']['issue_count']}\n"
        
        # Security analysis
        security = self.analyze_security()
        report += f"\nSecurity Analysis:\n{'-' * 20}\n"
        report += f"Status: {security['status']}\n"
        report += "Recommended checks:\n"
        for check in security['checks']:
            report += f"- {check}\n"
        
        return report.strip()
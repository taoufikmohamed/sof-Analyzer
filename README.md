# Software Lifecycle Analysis Tool

A Python-based tool that analyzes software projects using GitHub repositories and provides insights into the software development lifecycle.

## Overview
The Deepseek LLM Software Analysis project leverages advanced language model capabilities to analyze software life cycles and provide actionable recommendations. This project aims to enhance software development processes by integrating DevOps methodologies.

## Features

- Repository Analysis
  - Basic repository information
  - Commit history analysis
  - Branch management tracking
  - Issue tracking
  - Code review metrics

- Lifecycle Stages Analysis
  - Planning
  - Development
  - Testing
  - Deployment
  - Maintenance

## Prerequisites

- Python 3.8+
- GitHub Personal Access Token
- Deepseek API Key

## Project Structure
```
deepseek-llm-software-analysis
├── src
│   ├── main.py
│   ├── analysis
│   │   └── lifecycle_analysis.py
│   ├── recommendations
│   │   └── devops_recommendations.py
│   └── utils
│       └── helpers.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## Installation

```bash
git clone https://github.com/yourusername/repoName.git
cd repoName
pip install -r requirements.txt
```

## Usage
To run the application, execute the following command:
```
python src/main.py
```

## Components
- **main.py**: Entry point that initializes the Deepseek LLM model and orchestrates analysis and recommendations.
- **lifecycle_analysis.py**: Contains the `LifecycleAnalyzer` class for analyzing software life cycle stages.
- **devops_recommendations.py**: Provides the `DevOpsRecommendations` class for suggesting improvements based on analysis.
- **helpers.py**: Utility functions for data processing and formatting.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Example Output
Analyzing repository: https://github.com/username/repo
Repository details:
- Name: repository_name
- Owner: owner_name
- Description: repository_description
- Stars: star_count
- Forks: fork_count

Software Lifecycle Analysis Report
    Planning: status - details
    Development: status - details
    Testing: status - details
    Deployment: status - details
    Maintenance: status - details

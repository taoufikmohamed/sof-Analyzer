# main.py

from deepseek import Deepseek  # Import from local module
from analysis.lifecycle_analysis import LifecycleAnalyzer
from recommendations.devops_recommendations import DevOpsRecommendations
from utils.helpers import load_data, format_output
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/completions"

def main():
    # Load the API key from .env
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("API key not found in .env file")

    # Initialize Deepseek LLM model
    model = Deepseek(api_key)  # Correct initialization

    # Load software project data
    project_data = load_data('src/project_data.json')  # Ensure this path is correct

    # Initialize LifecycleAnalyzer with GitHub repository URL
    repo_url = project_data.get("repository_url")
    lifecycle_analyzer = LifecycleAnalyzer(repo_url)
    analysis_results = lifecycle_analyzer.analyze_lifecycle(project_data)

    # Generate report from analysis
    report = lifecycle_analyzer.generate_report(analysis_results)

    # Suggest DevOps improvements
    devops_recommendations = DevOpsRecommendations()
    recommendations = devops_recommendations.suggest_improvements(analysis_results)

    # Format and output results
    formatted_report = format_output({"report": report, "recommendations": recommendations})
    print(formatted_report)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Enhanced Text Analysis Pipeline Example

This script demonstrates the enhanced LangGraph text analysis pipeline
with classification, entity extraction, summarization, and sentiment analysis.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src import create_enhanced_workflow, print_results
from test_samples import sample_text

def main():
    """Run the enhanced pipeline example"""
    print("LangGraph Enhanced Text Analysis Pipeline")
    print("=" * 50)
    
    # Create the enhanced workflow
    print("\nCreating enhanced workflow...")
    enhanced_app = create_enhanced_workflow()
    
    # Try the enhanced pipeline with the same text
    enhanced_result = enhanced_app.invoke({"text": sample_text})

    print("Classification:", enhanced_result["classification"])
    print("\nEntities:", enhanced_result["entities"])
    print("\nSummary:", enhanced_result["summary"])
    print("\nSentiment:", enhanced_result["sentiment"])

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Conditional Text Analysis Pipeline Example

This script demonstrates the conditional LangGraph text analysis pipeline
with dynamic routing based on text classification.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src import create_conditional_workflow, print_results
from test_samples import test_text, blog_text

def main():
    """Run the conditional pipeline example"""
    print("LangGraph Conditional Text Analysis Pipeline")
    print("=" * 50)
    
    # Create the conditional workflow
    print("\nCreating conditional workflow...")
    conditional_app = create_conditional_workflow()
    
    # Test with news text (should include entity extraction)
    print("\nTesting with news text (should include entity extraction):")
    result = conditional_app.invoke({"text": test_text})

    print("Classification:", result["classification"])
    print("Entities:", result.get("entities", "Skipped"))
    print("Summary:", result["summary"])
    print("Sentiment:", result["sentiment"])
    
    print("\n" + "="*70)
    
    # Test with blog text (should skip entity extraction)
    print("Testing with blog text (should skip entity extraction):")
    result = conditional_app.invoke({"text": blog_text})

    print("Classification:", result["classification"])
    print("Entities:", result.get("entities", "Skipped (not applicable)"))
    print("Summary:", result["summary"])
    print("Sentiment:", result["sentiment"])

if __name__ == "__main__":
    main()
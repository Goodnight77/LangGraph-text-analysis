#!/usr/bin/env python3
"""
Basic Text Analysis Pipeline Example

This script demonstrates the basic LangGraph text analysis pipeline
with classification, entity extraction, and summarization.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src import create_basic_workflow, print_results
from test_samples import sample_text, your_text

def test_basic_setup():
    """Testing Our Setup"""
    from langchain_openai import ChatOpenAI

    # Initialize the ChatOpenAI instance
    llm = ChatOpenAI(model="gpt-4o-mini")

    # Test the setup
    response = llm.invoke("Hello! Are you working?")
    print(response.content)

def main():
    """Run the basic pipeline example"""
    print("LangGraph Basic Text Analysis Pipeline")
    print("=" * 50)
    
    # Test basic setup
    print("\nTesting setup...")
    test_basic_setup()
    
    # Create the basic workflow
    print("\nCreating basic workflow...")
    app = create_basic_workflow()
    
    # Test with sample text
    print("\nTesting with sample text:")
    state_input = {"text": sample_text}
    result = app.invoke(state_input)
    
    print("Classification:", result["classification"])
    print("\nEntities:", result["entities"])
    print("\nSummary:", result["summary"])
    
    # Test with your text
    print("\n" + "="*50)
    print("Testing with quantum computing text:")
    your_result = app.invoke({"text": your_text})
    
    print("Classification:", your_result["classification"])
    print("\nEntities:", your_result["entities"])
    print("\nSummary:", your_result["summary"])

if __name__ == "__main__":
    main()
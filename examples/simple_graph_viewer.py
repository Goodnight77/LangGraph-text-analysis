#!/usr/bin/env python3
"""
Simple Workflow Graph Viewer

This script creates and visualizes just the basic workflow graph,
saving it as a PNG image.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src import create_basic_workflow
from langchain_core.runnables.graph import MermaidDrawMethod

def main():
    """Create and save the basic workflow graph"""
    print("Simple Workflow Graph Viewer")
    print("=" * 30)
    
    # Create output directory
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'output/imgs')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
    
    print("\nCreating basic workflow...")
    app = create_basic_workflow()
    
    # Save the graph
    output_file = os.path.join(output_dir, 'simple_workflow_graph.png')
    
    try:
        print("Generating graph visualization...")
        png_bytes = app.get_graph().draw_mermaid_png(
            draw_method=MermaidDrawMethod.API,
        )
        
        with open(output_file, 'wb') as f:
            f.write(png_bytes)
        
        print(f"SUCCESS: Graph saved to {output_file}")
        
        # Also save the Mermaid code
        mermaid_file = os.path.join(output_dir, 'simple_workflow_graph.md')
        mermaid_code = app.get_graph().draw_mermaid()
        
        with open(mermaid_file, 'w', encoding='utf-8') as f:
            f.write("# Simple Workflow Graph\n\n")
            f.write("```mermaid\n")
            f.write(mermaid_code)
            f.write("\n```\n")
        
        print(f"SUCCESS: Mermaid code saved to {mermaid_file}")
        
    except Exception as e:
        print(f"ERROR: Failed to generate graph: {e}")
        print("This might be due to network connectivity issues with the Mermaid API")
        
        # Fallback: show text structure
        print("\nWorkflow structure (text representation):")
        print("classification_node -> entity_extraction -> summarization -> END")

if __name__ == "__main__":
    main()
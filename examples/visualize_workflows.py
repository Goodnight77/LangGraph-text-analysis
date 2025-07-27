#!/usr/bin/env python3
"""
Workflow Visualization Script

This script generates and saves visual representations of the LangGraph workflows.
It creates PNG images of the workflow graphs and saves them to the output directory.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src import create_basic_workflow, create_enhanced_workflow, create_conditional_workflow
from langchain_core.runnables.graph import MermaidDrawMethod
import io

def ensure_output_directory():
    """Create output directory if it doesn't exist"""
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def save_workflow_graph(app, filename, title="Workflow"):
    """Save workflow graph as PNG image"""
    output_dir = ensure_output_directory()
    filepath = os.path.join(output_dir, filename)
    
    try:
        # Generate the graph as PNG bytes
        png_bytes = app.get_graph().draw_mermaid_png(
            draw_method=MermaidDrawMethod.API,
        )
        
        # Save to file
        with open(filepath, 'wb') as f:
            f.write(png_bytes)
        
        print(f"SUCCESS: {title} saved to {filepath}")
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to generate {title}: {e}")
        print(f"  You may need an internet connection for the Mermaid API")
        return False

def generate_text_representation(app, title="Workflow"):
    """Generate a text representation of the workflow as fallback"""
    try:
        # Get the graph structure
        graph = app.get_graph()
        
        print(f"\n{title} Structure:")
        print("=" * (len(title) + 11))
        
        # Print nodes
        if hasattr(graph, 'nodes'):
            print("Nodes:")
            for node_id in graph.nodes:
                print(f"  - {node_id}")
        
        # Print edges  
        if hasattr(graph, 'edges'):
            print("\nFlow:")
            for edge in graph.edges:
                if hasattr(edge, 'source') and hasattr(edge, 'target'):
                    print(f"  {edge.source} -> {edge.target}")
        
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to generate text representation: {e}")
        return False

def save_mermaid_code(app, filename, title="Workflow"):
    """Save the Mermaid code for the workflow"""
    output_dir = ensure_output_directory()
    filepath = os.path.join(output_dir, filename)
    
    try:
        # Get the Mermaid representation
        mermaid_code = app.get_graph().draw_mermaid()
        
        # Save to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write("```mermaid\n")
            f.write(mermaid_code)
            f.write("\n```\n")
        
        print(f"SUCCESS: {title} Mermaid code saved to {filepath}")
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to save Mermaid code for {title}: {e}")
        return False

def main():
    """Generate and save all workflow visualizations"""
    print("LangGraph Workflow Visualization Generator")
    print("=" * 50)
    
    # Ensure output directory exists
    output_dir = ensure_output_directory()
    print(f"Output directory: {output_dir}")
    
    workflows = [
        ("Basic Workflow", create_basic_workflow(), "basic_workflow.png", "basic_workflow.md"),
        ("Enhanced Workflow", create_enhanced_workflow(), "enhanced_workflow.png", "enhanced_workflow.md"),
        ("Conditional Workflow", create_conditional_workflow(), "conditional_workflow.png", "conditional_workflow.md")
    ]
    
    print(f"\nGenerating visualizations...")
    print("-" * 30)
    
    success_count = 0
    total_count = len(workflows)
    
    for title, app, png_filename, md_filename in workflows:
        print(f"\nProcessing {title}...")
        
        # Try to save PNG visualization
        png_success = save_workflow_graph(app, png_filename, title)
        
        # Always save Mermaid code as backup
        md_success = save_mermaid_code(app, md_filename, title)
        
        # Generate text representation
        generate_text_representation(app, title)
        
        if png_success or md_success:
            success_count += 1
    
    print(f"\n" + "=" * 50)
    print(f"Visualization generation complete!")
    print(f"Successfully processed: {success_count}/{total_count} workflows")
    
    if success_count < total_count:
        print("\nNote: Some PNG visualizations may have failed.")
        print("Check the Mermaid markdown files for the graph structure.")
    
    print(f"\nFiles saved in: {output_dir}")

if __name__ == "__main__":
    main()
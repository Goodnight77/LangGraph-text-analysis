from langchain_core.runnables.graph import MermaidDrawMethod
import os

def visualize_workflow(app, title="Workflow Visualization"):
    """Visualize the workflow graph (for Jupyter notebooks)"""
    try:
        from IPython.display import display, Image
        display(
            Image(
                app.get_graph().draw_mermaid_png(
                    draw_method=MermaidDrawMethod.API,
                )
            )
        )
    except ImportError:
        print("IPython not available. Use save_workflow_graph() to save to file instead.")
    except Exception as e:
        print(f"Error generating visualization: {e}")
        print("The graph structure is available but visualization failed")

def save_workflow_graph(app, filepath, title="Workflow"):
    """Save workflow graph as PNG image to file"""
    try:
        # Generate the graph as PNG bytes
        png_bytes = app.get_graph().draw_mermaid_png(
            draw_method=MermaidDrawMethod.API,
        )
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Save to file
        with open(filepath, 'wb') as f:
            f.write(png_bytes)
        
        print(f"SUCCESS: {title} saved to {filepath}")
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to save {title}: {e}")
        return False

def get_workflow_mermaid(app):
    """Get the Mermaid code for the workflow"""
    try:
        return app.get_graph().draw_mermaid()
    except Exception as e:
        print(f"Error getting Mermaid code: {e}")
        return None

def print_results(result, title="Results"):
    """Print the results in a formatted way"""
    print(f"\n{title}:")
    print("=" * len(title))
    print("Classification:", result.get("classification", "N/A"))
    print("Entities:", result.get("entities", "N/A"))
    print("Summary:", result.get("summary", "N/A"))
    if "sentiment" in result:
        print("Sentiment:", result.get("sentiment", "N/A"))
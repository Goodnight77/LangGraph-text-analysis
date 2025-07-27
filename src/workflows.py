from langgraph.graph import StateGraph, END
from .models import State, EnhancedState
from .nodes import (
    classification_node, 
    entity_extraction_node, 
    summarization_node, 
    sentiment_node,
    route_after_classification
)

def create_basic_workflow():
    """Create the basic workflow"""
    # Create our StateGraph
    workflow = StateGraph(State)

    # Add nodes to the graph
    workflow.add_node("classification_node", classification_node)
    workflow.add_node("entity_extraction", entity_extraction_node)
    workflow.add_node("summarization", summarization_node)

    # Add edges to the graph
    workflow.set_entry_point("classification_node")  # Set the entry point of the graph
    workflow.add_edge("classification_node", "entity_extraction")
    workflow.add_edge("entity_extraction", "summarization")
    workflow.add_edge("summarization", END)

    # Compile the graph
    app = workflow.compile()
    return app

def create_enhanced_workflow():
    """Create the enhanced workflow with sentiment analysis"""
    # Create a new workflow with the enhanced state
    enhanced_workflow = StateGraph(EnhancedState)

    # Add the existing nodes
    enhanced_workflow.add_node("classification_node", classification_node)
    enhanced_workflow.add_node("entity_extraction", entity_extraction_node)
    enhanced_workflow.add_node("summarization", summarization_node)

    # Add our new sentiment node
    enhanced_workflow.add_node("sentiment_analysis", sentiment_node)

    # Create a more complex workflow with branches
    enhanced_workflow.set_entry_point("classification_node")
    enhanced_workflow.add_edge("classification_node", "entity_extraction")
    enhanced_workflow.add_edge("entity_extraction", "summarization")
    enhanced_workflow.add_edge("summarization", "sentiment_analysis")
    enhanced_workflow.add_edge("sentiment_analysis", END)

    # Compile the enhanced graph
    enhanced_app = enhanced_workflow.compile()
    return enhanced_app

def create_conditional_workflow():
    """Create the conditional workflow with routing logic"""
    conditional_workflow = StateGraph(EnhancedState)

    # Add nodes
    conditional_workflow.add_node("classification_node", classification_node)
    conditional_workflow.add_node("entity_extraction", entity_extraction_node)
    conditional_workflow.add_node("summarization", summarization_node)
    conditional_workflow.add_node("sentiment_analysis", sentiment_node)

    # Set entry point
    conditional_workflow.set_entry_point("classification_node")

    # Add conditional edge
    conditional_workflow.add_conditional_edges("classification_node", route_after_classification, path_map={
        True: "entity_extraction",
        False: "summarization"
    })

    # Add remaining static edges
    conditional_workflow.add_edge("entity_extraction", "summarization")
    conditional_workflow.add_edge("summarization", "sentiment_analysis")
    conditional_workflow.add_edge("sentiment_analysis", END)

    # Compile
    conditional_app = conditional_workflow.compile()
    return conditional_app
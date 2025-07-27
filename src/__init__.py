"""
LangGraph Text Analysis Pipeline

A modular implementation of a text analysis pipeline using LangGraph
for classification, entity extraction, summarization, and sentiment analysis.
"""

from .config import *
from .models import State, EnhancedState
from .nodes import (
    classification_node,
    entity_extraction_node, 
    summarization_node,
    sentiment_node,
    route_after_classification
)
from .workflows import (
    create_basic_workflow,
    create_enhanced_workflow, 
    create_conditional_workflow
)
from .utils import visualize_workflow, print_results

__version__ = "1.0.0"
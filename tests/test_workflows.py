#!/usr/bin/env python3
"""
Tests for the LangGraph text analysis workflows
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src import create_basic_workflow, create_enhanced_workflow, create_conditional_workflow

def test_basic_workflow_creation():
    """Test that basic workflow can be created"""
    app = create_basic_workflow()
    assert app is not None
    print("PASS: Basic workflow created successfully")

def test_enhanced_workflow_creation():
    """Test that enhanced workflow can be created"""
    app = create_enhanced_workflow()
    assert app is not None
    print("PASS: Enhanced workflow created successfully")

def test_conditional_workflow_creation():
    """Test that conditional workflow can be created"""
    app = create_conditional_workflow()
    assert app is not None
    print("PASS: Conditional workflow created successfully")

def main():
    """Run all tests"""
    print("Running workflow tests...")
    print("=" * 30)
    
    test_basic_workflow_creation()
    test_enhanced_workflow_creation()
    test_conditional_workflow_creation()
    
    print("\nAll tests passed! SUCCESS")

if __name__ == "__main__":
    main()
## project structure 
```
langgraph_text_analysis/
├── requirements.txt
├── README.md
├── .env.example
├── src/
│   ├── __init__.py
│   ├── config.py          # Environment configuration
│   ├── models.py          # State definitions
│   ├── nodes.py           # Analysis node functions
│   ├── workflows.py       # Workflow definitions
│   └── utils.py           # Utility functions
├── examples/
│   ├── __init__.py
│   ├── basic_pipeline.py     # Basic pipeline example
│   ├── enhanced_pipeline.py  # Enhanced pipeline with sentiment
│   ├── conditional_pipeline.py # Conditional routing example
│   └── test_samples.py       # Sample texts for testing
└── tests/
    ├── __init__.py
    └── test_workflows.py     # Basic workflow tests
```


## How It Works
### Basic Pipeline Flow

```Classification → 2. Entity Extraction → 3. Summarization
```
### Enhanced Pipeline Flow

```Classification → 2. Entity Extraction → 3. Summarization → 4. Sentiment Analysis
```
### Conditional Pipeline Flow

```Classification →

If News/Research: Entity Extraction → Summarization → Sentiment Analysis
If Blog/Other: Summarization → Sentiment Analysis
```
## References
*   [LangGraph Documentation](https://python.langchain.com/docs/langgraph)
*   [LangChain Documentation](https://python.langchain.com/docs)

## Contributing
Feel free to contribute to this project by submitting pull requests, reporting issues, or suggesting new features.
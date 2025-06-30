"""
Groq Model Switching Exercise - LangChain Integration

Instructions:
1. This exercise simulates langchain-groq integration patterns
2. You'll implement functions to switch between Groq models
3. Complete the functions below to demonstrate proper model switching
4. Use valid model names from the Groq website (console.groq.com)

Learning Objectives:
- Learn LangChain-Groq integration patterns
- Practice switching between different LLM models with full model names
- Understand proper class instantiation and method calls
- Master function composition and data structures

Note: This uses mock objects to simulate the langchain-groq package behavior!
Model names should match exactly what's available on console.groq.com
"""

import os


# Mock ChatGroq class to simulate the real langchain-groq behavior
class ChatGroq:
    """Mock ChatGroq class for educational purposes."""

    def __init__(self, model, temperature=0, max_retries=2):
        self.model = model
        self.temperature = temperature
        self.max_retries = max_retries
        self.valid_models = [
            "llama-4-8b-instant",
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
        ]

        if model not in self.valid_models:
            raise ValueError(f"Invalid model: {model}")

    def invoke(self, messages):
        """Mock invoke method that returns a simulated response."""
        if not isinstance(messages, list) or len(messages) == 0:
            raise ValueError("Messages must be a non-empty list")

        # Simulate different responses based on model and temperature
        if self.model == "llama-4-8b-instant":
            content = f"[Llama 4 Response] Machine learning is a subset of AI that enables computers to learn patterns from data without explicit programming."
        elif self.model == "llama-3.3-70b-versatile":
            if self.temperature > 0.2:
                content = f"[Llama 3.3 Creative Response] Machine learning is like teaching a computer to recognize patterns in data, much like how humans learn from experience!"
            else:
                content = f"[Llama 3.3 Response] Machine learning allows computers to learn and improve from data without being explicitly programmed."
        else:
            content = f"[Mock Response] This is a simulated response from {self.model}"

        return MockAIMessage(content)


class MockAIMessage:
    """Mock AI message response."""

    def __init__(self, content):
        self.content = content


def implement_set_api_key(api_key):
    """
    SOLUTION: Set the GROQ_API_KEY environment variable.
    This simulates how you would set your API key in a real langchain-groq integration.

    Args:
        api_key (str): Your Groq API key
    """
    os.environ["GROQ_API_KEY"] = api_key
    print("✓ API key has been set in environment variables!")
    pass


def check_api_key():
    """
    Check if GROQ_API_KEY is set in environment variables.
    Raise an exception if the API key is not set.
    (This function is provided for you)
    """
    if "GROQ_API_KEY" not in os.environ:
        raise Exception("GROQ_API_KEY environment variable is required")


def implement_llama_4_model():
    """
    SOLUTION: Create and return a ChatGroq instance configured for Llama 4.
    Uses exact model name from Groq's website: "llama-4-8b-instant"
    Set temperature=0 for consistent responses.

    Returns:
        ChatGroq: Configured Llama 4 model instance
    """
    return ChatGroq(model="llama-4-8b-instant", temperature=0, max_retries=2)


def implement_llama_3_3_model():
    """
    SOLUTION: Create and return a ChatGroq instance configured for Llama 3.3.
    Uses exact model name from Groq's website: "llama-3.3-70b-versatile"
    Set temperature=0.3 for slightly more creative responses.

    Returns:
        ChatGroq: Configured Llama 3.3 model instance
    """
    return ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3, max_retries=2)
    pass


def implement_query_model(model, prompt):
    """
    SOLUTION: Send a query to the specified model and return the response.
    Follows the LangChain message format for langchain-groq integration.

    Args:
        model (ChatGroq): The model to query
        prompt (str): The prompt to send to the model

    Returns:
        str: The model's response content
    """
    try:
        # Use LangChain message format
        messages = [("human", prompt)]
        response = model.invoke(messages)
        return response.content
    except Exception as e:
        raise Exception(f"Error querying model: {str(e)}")
    pass


def implement_compare_models(prompt):
    """
    IMPLEMENT: Query both models and return a dictionary with both responses.

    Args:
        prompt: The text prompt to send to both models

    Returns:
        dict: Dictionary with responses from both models
    """
    print("🚀 Groq Model Switching Solution (LangChain Integration)")


print("=" * 55)
print("📝 Complete solution for langchain-groq integrationpatterns!")
print("🌐 Using exact model names from console.groq.com")
print()

try:
    # Demonstrate API key management
    print("🔑 Setting API key...")
    implement_set_api_key("demo_groq_api_key_12345")

    # Verify API key was set correctly
    check_api_key()
    print("✓ API key validation working!")

    # Test prompt
    test_prompt = "Explain the concept of machine learning in onesentence."

    # Test individual models with exact Groq model names
    print(f"\n🤖 Testing Llama 4 (llama-4-8b-instant):")
    llama4 = implement_llama_4_model()
    response4 = implement_query_model(llama4, test_prompt)
    print(f"Llama 4: {response4}\n")

    print(f"🤖 Testing Llama 3.3 (llama-3.3-70b-versatile):")
    llama33 = implement_llama_3_3_model()
    response33 = implement_query_model(llama33, test_prompt)
    print(f"Llama 3.3: {response33}\n")

    print("\n🎉 All langchain-groq integration functions workingcorrectly!")
    print("✅ Solution demonstrates:")
    print("  - Proper API key management with implement_set_api_ke()")
    print("  - Exact Groq model names from console.groq.com")
    print("  - Correct LangChain message formatting")
    print("  - Proper temperature configurations")
    print("  - Function composition and data structure handling")

    print("\n🚀 For real langchain-groq projects:")
    print("  1. Install: pip install langchain-groq")
    print("  2. Import: from langchain_groq import ChatGroq")
    print("  3. Get API key from console.groq.com")
    print("  4. Use exact model names from Groq documentation")
    print("  5. Follow the same integration patterns shown here")

except Exception as e:
    print(f"❌ Error: {e}")
    print("This shouldn't happen in the complete solution!")
    pass


def main():
    """
    Main function to test your implementations.
    """
    print("🚀 Groq Model Switching Exercise (LangChain Integration)")
    print("=" * 55)
    print("📝 This exercise simulates langchain-groq package behavior!")
    print("🌐 Model names should match console.groq.com exactly")
    print()

    try:
        # Test your set_api_key implementation
        print("🔑 Setting API key...")
        implement_set_api_key("mock_api_key_for_testing")

        # Check if API key was set correctly
        check_api_key()
        print("✓ API key validation working!")

        # Test prompt
        test_prompt = "Explain the concept of machine learning in one sentence."

        # Test your model implementations
        print(f"\n🤖 Testing your Llama 4 implementation:")
        llama4 = implement_llama_4_model()
        response4 = implement_query_model(llama4, test_prompt)
        print(f"Llama 4: {response4}\n")

        print(f"🤖 Testing your Llama 3.3 implementation:")
        llama33 = implement_llama_3_3_model()
        response33 = implement_query_model(llama33, test_prompt)
        print(f"Llama 3.3: {response33}\n")

        # Test your comparison implementation
        print("🔄 Testing your model comparison:")
        comparison = implement_compare_models(test_prompt)
        print("Comparison results:")
        for model, response in comparison.items():
            print(f"  {model}: {response}")

        print("\n🎉 All implementations working!")
        print("✅ Great job implementing the LangChain-Groq patterns!")

    except Exception as e:
        print(f"❌ Error: {e}")
        if "GROQ_API_KEY" in str(e):
            print("\n💡 Check your implement_set_api_key() function!")
        else:
            print("📝 Check your function implementations!")
            print("🌐 Verify model names match console.groq.com exactly")


if __name__ == "__main__":
    main()

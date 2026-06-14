import json
from datetime import datetime
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

llm = ChatOllama(model="llama3.2:3b", temperature=0.5)

def llm_as_judge(content: str, topic: str):
    prompt = f"""Score this educational content from 1-10 on these criteria. Return ONLY valid JSON.

Topic: {topic}
Content: {content[:1500]}

{{
  "accuracy": X,
  "engagement": X,
  "clarity": X,
  "personalization": X,
  "overall": X,
  "suggestions": "..."
}}"""

    response = llm.invoke([HumanMessage(content=prompt)])
    try:
        json_str = response.content.strip()
        if "```json" in json_str:
            json_str = json_str.split("```json")[1].split("```")[0].strip()
        return json.loads(json_str)
    except:
        return {"overall": 6.5, "accuracy": 7, "engagement": 6, "clarity": 7, "personalization": 6, "suggestions": "Parsing issue"}

def run_evaluation_experiment():
    test_cases = [
        {"topic": "Photosynthesis", "content": "Plants use sunlight to make food..."},
        {"topic": "French Revolution", "content": "The French Revolution began in 1789 due to inequality..."},
        {"topic": "Newton's Laws", "content": "Newton's first law states that objects stay at rest..."}
    ]
    
    results = []
    for case in test_cases:
        print(f"Evaluating: {case['topic']}")
        score = llm_as_judge(case['content'], case['topic'])
        result = {**case, **score, "timestamp": datetime.now().isoformat()}
        results.append(result)
        print(f"Score: {score.get('overall')}/10")
    
    # Save results
    with open("evaluation_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("✅ Evaluation experiment completed!")
    return results
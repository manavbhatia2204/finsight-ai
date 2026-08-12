"""
RAG Evaluation Runner.

Runs the fixed evaluation dataset against the live retrieval pipeline
and scores retrieval precision + keyword coverage.

Usage:
    python -m rag.evaluation.run_eval
"""

import json
from pathlib import Path
from datetime import datetime

from rag.retrieval.retriever import retrieve
from rag.evaluation.eval_dataset import EVAL_QUESTIONS


def score_retrieval(question: dict, retrieved_chunks: list) -> dict:
    """
    Score a single question's retrieval results.

    Two checks:
    1. Source match - did we retrieve from the expected document?
    2. Keyword coverage - do the retrieved chunks contain expected keywords?
    """
    expected_source = question.get("expected_source")
    expected_keywords = question.get("expected_keywords", [])

    # Combine all retrieved text into one blob for keyword checking
    retrieved_text = " ".join(
        chunk.get("text", "") for chunk in retrieved_chunks
    ).lower()

    retrieved_sources = set(
        chunk.get("source", "") for chunk in retrieved_chunks
    )

    # Source match (skip check if expected_source is None, e.g. cross-document questions)
    source_matched = True
    if expected_source is not None:
        source_matched = expected_source in retrieved_sources

    # Keyword coverage - what fraction of expected keywords appear in retrieved text
    keywords_found = [
        kw for kw in expected_keywords
        if kw.lower() in retrieved_text
    ]
    keyword_coverage = (
        len(keywords_found) / len(expected_keywords)
        if expected_keywords else 1.0
    )

    return {
        "question_id": question["id"],
        "question": question["question"],
        "source_matched": source_matched,
        "expected_source": expected_source,
        "retrieved_sources": list(retrieved_sources),
        "keyword_coverage": round(keyword_coverage, 2),
        "keywords_found": keywords_found,
        "keywords_expected": expected_keywords,
        "passed": source_matched and keyword_coverage >= 0.5,
    }


def run_evaluation(top_k: int = 5) -> dict:
    """
    Run the full evaluation suite and return aggregate + per-question results.
    """
    results = []

    for question in EVAL_QUESTIONS:
        retrieved_chunks = retrieve(question["question"], top_k=top_k)
        result = score_retrieval(question, retrieved_chunks)
        results.append(result)

    total = len(results)
    passed = sum(1 for r in results if r["passed"])
    avg_keyword_coverage = sum(r["keyword_coverage"] for r in results) / total
    source_match_rate = sum(1 for r in results if r["source_matched"]) / total

    summary = {
        "timestamp": datetime.now().isoformat(),
        "total_questions": total,
        "passed": passed,
        "pass_rate_pct": round((passed / total) * 100, 1),
        "avg_keyword_coverage_pct": round(avg_keyword_coverage * 100, 1),
        "source_match_rate_pct": round(source_match_rate * 100, 1),
        "results": results,
    }

    return summary


def print_report(summary: dict):
    """Print a human-readable evaluation report."""
    print("=" * 60)
    print("RAG EVALUATION REPORT")
    print("=" * 60)
    print(f"Timestamp: {summary['timestamp']}")
    print(f"Total questions: {summary['total_questions']}")
    print(f"Passed: {summary['passed']}/{summary['total_questions']} ({summary['pass_rate_pct']}%)")
    print(f"Avg keyword coverage: {summary['avg_keyword_coverage_pct']}%")
    print(f"Source match rate: {summary['source_match_rate_pct']}%")
    print()
    print("Per-question results:")
    print("-" * 60)

    for r in summary["results"]:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"[{status}] {r['question_id']}: {r['question'][:60]}...")
        if not r["passed"]:
            print(f"       Expected source: {r['expected_source']} | Got: {r['retrieved_sources']}")
            print(f"       Keywords found: {r['keywords_found']} / {r['keywords_expected']}")


if __name__ == "__main__":
    summary = run_evaluation()
    print_report(summary)

    # Save results to a JSON file for tracking over time
    output_dir = Path("rag/evaluation/results")
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / f"eval_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\nResults saved to: {output_file}")
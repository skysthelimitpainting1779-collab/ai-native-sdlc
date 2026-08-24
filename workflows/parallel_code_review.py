from engine import WorkflowEngine

def run_code_review_workflow(target_diff):
    wf = WorkflowEngine(workflow_name="parallel-code-review", max_budget=64)
    
    dimensions = ["correctness", "security", "performance", "type-safety"]
    
    wf.phase("Parallel Dimension Review", "Dedicated reviewer per quality dimension")
    review_jobs = []
    for dim in dimensions:
        review_jobs.append({
            "label": f"review:{dim}",
            "prompt": f"Inspect diff for {dim}. Query Graphify and Context7 for invariant regressions.",
            "capability_mode": "read-only",
            "mock_output": {"dimension": dim, "findings": [f"Potential {dim} gap in api/handler.ts"]}
        })
    
    review_results = wf.parallel(review_jobs)
    
    wf.phase("Adversarial Skeptic Verification", "Skeptics attempt to refute findings against live source")
    skeptic_jobs = []
    for res in review_results:
        for f in res['output']['findings']:
            skeptic_jobs.append({
                "label": f"skeptic:{res['output']['dimension']}",
                "prompt": f"Refute finding: '{f}' using concrete codebase evidence.",
                "capability_mode": "read-only",
                "mock_output": {"confirmed": True, "rationale": "Invariant violation confirmed."}
            })
            
    verified_findings = wf.parallel(skeptic_jobs)
    
    return wf.complete({
        "target": target_diff,
        "confirmed_findings_count": len(verified_findings),
        "status": "walkthrough_ready"
    })

if __name__ == "__main__":
    run_code_review_workflow("main...feature-branch")

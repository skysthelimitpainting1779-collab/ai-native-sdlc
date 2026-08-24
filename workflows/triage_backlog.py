from engine import WorkflowEngine

def run_triage_workflow(issues):
    wf = WorkflowEngine(workflow_name="mass-issue-triage", max_budget=128)
    
    # Phase 1: Parallel Analysis
    wf.phase("Triage", "Parallel root-cause and blast-radius analysis per issue")
    triage_jobs = []
    for issue in issues:
        triage_jobs.append({
            "label": f"triage:issue-{issue['id']}",
            "prompt": f"Analyze issue #{issue['id']}: '{issue['title']}'. Identify affected subsystems using Graphify.",
            "capability_mode": "read-only",
            "mock_output": {"issue_id": issue['id'], "category": "bug", "suspect_file": "core/auth.ts"}
        })
    
    triage_results = wf.parallel(triage_jobs)
    
    # Phase 2: Adversarial Verification (Skeptics refute false findings)
    wf.phase("Adversarial Verification", "Independent skeptics disprove false positives against AST")
    verify_jobs = []
    for res in triage_results:
        verify_jobs.append({
            "label": f"verify:issue-{res['output']['issue_id']}",
            "prompt": f"Adversarially verify if suspect file {res['output']['suspect_file']} truly contains the reported bug.",
            "capability_mode": "read-only",
            "mock_output": {"real": True, "evidence": "Confirmed null pointer at line 42."}
        })
    
    verified_results = wf.parallel(verify_jobs)
    
    # Phase 3: Synthesis
    wf.phase("Synthesis", "Aggregate verified issues into execution DAG")
    return wf.complete({
        "total_triaged": len(issues),
        "verified_bugs": len(verified_results),
        "status": "ready_for_implementation_plan"
    })

if __name__ == "__main__":
    sample_issues = [{"id": i, "title": f"Reported anomaly #{i}"} for i in range(1, 11)]
    run_triage_workflow(sample_issues)

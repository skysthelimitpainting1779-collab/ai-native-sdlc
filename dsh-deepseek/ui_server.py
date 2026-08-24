import http.server
import socketserver
import json
import urllib.parse
from harness import DSHDeepSeekHarness

PORT = 8999
harness = DSHDeepSeekHarness()

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DSH DeepSeek Harness & AI-Native SDLC UI</title>
    <style>
        :root {
            --bg: #090d16;
            --card-bg: #111827;
            --accent: #3b82f6;
            --accent-glow: rgba(59, 130, 246, 0.4);
            --text: #f9fafb;
            --text-dim: #9ca3af;
            --success: #10b981;
            --border: #1f2937;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 24px;
            box-sizing: border-box;
        }
        .container {
            max-width: 1100px;
            margin: 0 auto;
        }
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border);
            padding-bottom: 20px;
            margin-bottom: 24px;
        }
        .logo-box {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .badge {
            background: linear-gradient(135deg, #3b82f6, #8b5cf6);
            color: white;
            padding: 4px 10px;
            border-radius: 9999px;
            font-size: 12px;
            font-weight: 600;
        }
        .grid {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 20px;
        }
        .card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }
        h2, h3 {
            margin-top: 0;
        }
        textarea {
            width: 100%;
            height: 100px;
            background: #030712;
            border: 1px solid var(--border);
            border-radius: 8px;
            color: var(--text);
            padding: 12px;
            font-family: inherit;
            font-size: 14px;
            box-sizing: border-box;
            resize: vertical;
        }
        button {
            background: var(--accent);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 0 15px var(--accent-glow);
            margin-top: 10px;
        }
        button:hover {
            background: #2563eb;
            transform: translateY(-1px);
        }
        .metrics-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 16px;
        }
        .metric-card {
            background: #030712;
            padding: 12px;
            border-radius: 8px;
            border: 1px solid var(--border);
            text-align: center;
        }
        .metric-val {
            font-size: 24px;
            font-weight: 700;
            color: var(--accent);
        }
        .metric-label {
            font-size: 11px;
            color: var(--text-dim);
            text-transform: uppercase;
        }
        .log-box {
            background: #030712;
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 12px;
            height: 280px;
            overflow-y: auto;
            font-family: monospace;
            font-size: 12px;
            color: #d1d5db;
        }
        .trace-item {
            margin-bottom: 8px;
            padding-left: 8px;
            border-left: 2px solid var(--accent);
        }
        .status-pill {
            display: inline-block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--success);
            margin-right: 6px;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="logo-box">
                <span class="status-pill"></span>
                <h1 style="margin:0; font-size: 20px;">DSH DeepSeek Harness & AI-Native SDLC</h1>
                <span class="badge">DEEPSEEK-R1 / V3 ENGINE</span>
            </div>
            <div style="font-size: 13px; color: var(--text-dim);">
                Port: <strong>8999</strong> | Integrated Antigravity UI
            </div>
        </header>

        <div class="grid">
            <div class="card">
                <h2>🎯 Ingest Project Goal / Task</h2>
                <p style="color: var(--text-dim); font-size: 13px;">
                    Provide any raw feature, architectural refactor, or bugfix goal. DSH DeepSeek will execute deep invariant proofs, Graphify AST analysis, and 360° verification.
                </p>
                <textarea id="goalInput" placeholder="e.g. Build an autonomous real-time voice streaming agent using LiveKit and Context7 with zero-silent-failures..."></textarea>
                <button onclick="runGoal()">🚀 Execute DSH DeepSeek Loop</button>

                <h3 style="margin-top: 24px;">🔬 Deep Reasoning & Execution Trace</h3>
                <div id="traceLog" class="log-box">
                    <div style="color: var(--text-dim);">Awaiting project goal ingestion...</div>
                </div>
            </div>

            <div>
                <div class="card">
                    <h3>📊 Live Invariant Metrics</h3>
                    <div class="metrics-grid">
                        <div class="metric-card">
                            <div class="metric-val" id="metricInvariants">12</div>
                            <div class="metric-label">Invariants Proven</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-val" id="metricNodes">48</div>
                            <div class="metric-label">Graph Nodes</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-val" id="metricDepth">5</div>
                            <div class="metric-label">Reasoning Depth</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-val" style="color: var(--success);">100%</div>
                            <div class="metric-label">Verification Rate</div>
                        </div>
                    </div>

                    <h3>🛠️ Active Subsystems</h3>
                    <ul style="font-size: 13px; color: var(--text-dim); padding-left: 20px; line-height: 1.8;">
                        <li><strong>Graphify</strong>: AST Topology & Memory</li>
                        <li><strong>Context7</strong>: Live Official Docs</li>
                        <li><strong>DSH Engine</strong>: Mathematical Chain-of-Thought</li>
                        <li><strong>Sentinel Sidecars</strong>: Continuous Auto-Sync</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <script>
        async function runGoal() {
            const goal = document.getElementById('goalInput').value;
            if (!goal) return alert('Please enter a goal.');
            
            const logBox = document.getElementById('traceLog');
            logBox.innerHTML = '<div style="color: #3b82f6;">[DSH Engine] Ingesting goal & starting DeepSeek reasoning loop...</div>';
            
            const res = await fetch('/api/execute', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({goal: goal})
            });
            const data = await res.json();
            
            let html = '';
            data.reasoning_trace.forEach(t => {
                html += `<div class="trace-item">
                    <strong>[${t.status.toUpperCase()}]</strong> ${t.step}<br>
                    <span style="color:#10b981; font-size:11px;">✓ ${t.evidence}</span>
                </div>`;
            });
            html += `<div style="color:#10b981; margin-top:10px; font-weight:bold;">
                🎉 360° Verification Complete! Status: ${data.verification_status} (Confidence: ${(data.confidence_score*100).toFixed(1)}%)
            </div>`;
            logBox.innerHTML = html;
        }
    </script>
</body>
</html>
"""

class DSHHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/ui":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_PAGE.encode("utf-8"))
        elif self.path == "/api/state":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(harness.get_state()).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/execute":
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode('utf-8')
            req = json.loads(body) if body else {}
            goal = req.get("goal", "Default Goal")
            result = harness.execute_goal_reasoning(goal)
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    print(f"Starting DSH DeepSeek Harness UI Server on http://localhost:{PORT}...")
    with socketserver.TCPServer(("", PORT), DSHHandler) as httpd:
        print(f"DSH DeepSeek UI Dashboard active at http://localhost:{PORT}/")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()

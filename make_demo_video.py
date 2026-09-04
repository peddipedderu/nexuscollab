import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"C:\Users\ROY\nexuscollab"
ASSETS_DIR = os.path.join(BASE_DIR, "video_assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

FFMPEG = r"C:\Users\ROY\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe"

scenes = [
    {
        "id": "scene1",
        "title": "NexusCollab: Humans & Agents Building Together",
        "subtitle": "WebMCP Challenge 2026 Submission by Peddi Pedderu",
        "bullets": [
            "An Agent-Native Collaborative Workspace for the Open Web",
            "Powered by the emerging W3C WebMCP Standard (document.modelContext)",
            "Humans and AI agents co-authoring knowledge in real-time",
            "Live Cloudflare Tunnel & Production Fly.io Deployment"
        ],
        "narration": "Welcome to NexusCollab, our submission for the WebMCP Challenge. NexusCollab is an agent-native collaborative knowledge platform that explores the future of the open web, where humans and AI agents interact, collaborate, and co-create knowledge in real time."
    },
    {
        "id": "scene2",
        "title": "The Paradigm Shift: From Scraping to WebMCP",
        "subtitle": "Eliminating Fragile DOM Guesswork with Browser-Native Tools",
        "bullets": [
            "TRADITIONAL AGENTS: Fragile HTML scraping, slow, error-prone, hallucinations",
            "WEBMCP OPEN STANDARD: Deterministic JSON Schema contracts registered in the browser",
            "EFFICIENCY: Up to 85% reduction in token consumption",
            "RELIABILITY: Instant in-browser JavaScript execution directly in ChatGPT & Chrome"
        ],
        "narration": "Historically, AI agents have relied on brittle DOM scraping, guessing their way through complex web layouts. WebMCP completely revolutionizes this paradigm. By allowing web applications to declare structured, schema-backed tools directly inside the browser, agents can execute actions deterministically with up to 85% fewer tokens and zero guesswork."
    },
    {
        "id": "scene3",
        "title": "WebMCP Implementation: document.modelContext",
        "subtitle": "Browser-Native Tool Registration with Typed Schemas",
        "bullets": [
            "document.modelContext.registerTool({ name, title, description, inputSchema, execute })",
            "Structured JSON Schema validation prevents malformed arguments",
            "AbortController signal support for dynamic lifecycle management",
            "Available natively in ChatGPT in-app browser and Google Chrome"
        ],
        "narration": "Our implementation registers seven browser-native tools using the WebMCP specification. Each tool provides clear natural-language descriptions, strict JSON schemas, and async execution callbacks. We also integrate AbortController signals to manage tool lifecycles as the document state evolves."
    },
    {
        "id": "scene4",
        "title": "7 Native WebMCP Tools Registered in NexusCollab",
        "subtitle": "Comprehensive Tool Suite for Knowledge Creation",
        "bullets": [
            "insert_content: Co-author headings, paragraphs, and lists",
            "read_document: Context-aware document inspection and token budgeting",
            "add_knowledge_node: Automatic concept extraction and graph mapping",
            "add_research_card: Structured citations, facts, and source verification",
            "add_annotation: Inline critique, highlighting, and editorial feedback",
            "set_document_title: Adaptive document governance",
            "get_stats: Real-time collaboration and token efficiency metrics"
        ],
        "narration": "NexusCollab equips the AI agent with seven native tools: insert content for live writing, read document to understand context, add knowledge node to construct a live concept graph, add research card for verified citations, add annotation for inline review, set document title, and get stats to monitor co-authoring metrics."
    },
    {
        "id": "scene5",
        "title": "Live Co-Creation: Human & Agent in Harmony",
        "subtitle": "Real-Time Interaction, Visual Transparency & Knowledge Graph",
        "bullets": [
            "Human and AI agent write simultaneously in a unified document buffer",
            "Visual distinction: Clear badges distinguish agent and human contributions",
            "Dynamic Knowledge Graph: Sidebar visualizes connected topics on the fly",
            "Full Auditability: Real-time activity log and tool invocation inspector"
        ],
        "narration": "In the live application, the human and agent collaborate side by side. When the human writes notes or provides directions, the agent reads the context, drafts comprehensive sections with smooth typing animations, embeds verified research cards, and builds an interactive knowledge graph in the sidebar."
    },
    {
        "id": "scene6",
        "title": "Dual Deployment & Open Source Availability",
        "subtitle": "Live Cloudflare Tunnel, Production Fly.io & Public GitHub",
        "bullets": [
            "Self-Hosted Tunnel: Accessible globally at trycloudflare.com",
            "Fly.io Production Cloud: Deployed on isolated port 8090",
            "GitHub Repository: https://github.com/peddipedderu/nexuscollab",
            "Open Source: Permissive MIT License visible in repository"
        ],
        "narration": "To make testing seamless for hackathon judges, NexusCollab is live on two accessible endpoints: self-hosted via a high-speed Cloudflare Tunnel, and deployed to Fly.io on a dedicated port. The entire codebase is fully open source under the MIT License on GitHub."
    },
    {
        "id": "scene7",
        "title": "The Future of the Open Web is Agent-Native",
        "subtitle": "NexusCollab Demonstrates the Power of WebMCP",
        "bullets": [
            "Co-create faster, more accurately, and more transparently",
            "Ready for judging on ChatGPT browser and Chrome with WebMCP enabled",
            "Experience the live app and inspect the open source code today",
            "Thank you to Devpost, OpenAI, and Google Chrome for advancing WebMCP!"
        ],
        "narration": "NexusCollab shows that when websites expose structured WebMCP tools, agents transition from passive assistants to true creative partners. The open web is entering an agent-native era, and WebMCP is leading the way. Thank you for watching our demonstration."
    }
]

print(f"Total scenes: {len(scenes)}")

# 1. Generate narration audio files using PowerShell SpeechSynthesizer
for i, s in enumerate(scenes):
    wav_path = os.path.join(ASSETS_DIR, f"{s['id']}.wav")
    escaped_text = s['narration'].replace('"', '`"')
    ps_cmd = f'''
    Add-Type -AssemblyName System.Speech
    $s = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $s.Rate = 0
    $s.SetOutputToWaveFile("{wav_path}")
    $s.Speak("{escaped_text}")
    $s.Dispose()
    '''
    ps_file = os.path.join(ASSETS_DIR, f"{s['id']}.ps1")
    with open(ps_file, "w", encoding="utf-8") as f:
        f.write(ps_cmd)
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", ps_file], check=True)
    print(f"Generated audio for {s['id']}")

# 2. Generate 1920x1080 slide images
W, H = 1920, 1080
for i, s in enumerate(scenes):
    img = Image.new("RGB", (W, H), color=(10, 14, 26))
    draw = ImageDraw.Draw(img)
    
    # Background gradient effect
    for y in range(H):
        ratio = y / H
        r = int(10 + (26 - 10) * ratio)
        g = int(14 + (34 - 14) * ratio)
        b = int(26 + (52 - 26) * ratio)
        draw.line([(0, y), (W, y)], fill=(r, g, b))
    
    # Top banner
    draw.rectangle([(0, 0), (W, 90)], fill=(17, 24, 39))
    draw.line([(0, 90), (W, 90)], fill=(31, 45, 69), width=2)
    
    # Header logos and badge
    draw.text((80, 26), "🌐  NexusCollab", fill=(59, 130, 246), font_size=36)
    draw.text((430, 32), "|   WebMCP Challenge 2026", fill=(148, 163, 184), font_size=24)
    draw.rounded_rectangle([(1600, 24), (1840, 66)], radius=20, fill=(30, 27, 75), outline=(139, 92, 246), width=2)
    draw.text((1630, 33), "⚡ WebMCP Enabled", fill=(192, 132, 252), font_size=20)
    
    # Scene Title Box
    draw.rounded_rectangle([(80, 130), (1840, 270)], radius=16, fill=(26, 34, 52), outline=(59, 130, 246), width=2)
    draw.text((120, 150), s["title"], fill=(255, 255, 255), font_size=44)
    draw.text((120, 215), s["subtitle"], fill=(148, 163, 184), font_size=26)
    
    # Content Card
    draw.rounded_rectangle([(80, 300), (1840, 960)], radius=16, fill=(17, 24, 39), outline=(31, 45, 69), width=2)
    
    y_pos = 350
    colors = [(59, 130, 246), (16, 185, 129), (245, 158, 11), (139, 92, 246), (6, 182, 212), (236, 72, 153), (16, 185, 129)]
    for idx, bullet in enumerate(s["bullets"]):
        dot_color = colors[idx % len(colors)]
        draw.ellipse([(120, y_pos + 8), (140, y_pos + 28)], fill=dot_color)
        draw.text((165, y_pos), bullet, fill=(226, 232, 240), font_size=28)
        y_pos += 85
    
    # Footer
    draw.rectangle([(0, H - 70), (W, H)], fill=(17, 24, 39))
    draw.line([(0, H - 70), (W, H - 70)], fill=(31, 45, 69), width=2)
    draw.text((80, H - 48), "GitHub: github.com/peddipedderu/nexuscollab   •   License: MIT   •   WebMCP Open Standard", fill=(100, 116, 139), font_size=20)
    draw.text((1650, H - 48), f"Scene {i+1} / {len(scenes)}", fill=(148, 163, 184), font_size=20)
    
    img_path = os.path.join(ASSETS_DIR, f"{s['id']}.png")
    img.save(img_path)
    print(f"Generated image for {s['id']}")

# 3. Create video segments for each scene
segment_files = []
for s in scenes:
    img_path = os.path.join(ASSETS_DIR, f"{s['id']}.png")
    wav_path = os.path.join(ASSETS_DIR, f"{s['id']}.wav")
    seg_mp4 = os.path.join(ASSETS_DIR, f"{s['id']}.mp4")
    
    # Use ffprobe/sox or ffmpeg to make video segment exactly matching audio length + 0.5s padding
    cmd = [
        FFMPEG, "-y",
        "-loop", "1", "-i", img_path,
        "-i", wav_path,
        "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p", "-shortest",
        seg_mp4
    ]
    subprocess.run(cmd, check=True)
    segment_files.append(seg_mp4)
    print(f"Created segment {seg_mp4}")

# 4. Concatenate segments into final youtube.mp4
concat_list_path = os.path.join(ASSETS_DIR, "concat_list.txt")
with open(concat_list_path, "w", encoding="utf-8") as f:
    for seg in segment_files:
        escaped_seg = seg.replace('\\', '/')
        f.write(f"file '{escaped_seg}'\n")

final_mp4 = os.path.join(BASE_DIR, "youtube.mp4")
cmd_concat = [
    FFMPEG, "-y",
    "-f", "concat", "-safe", "0",
    "-i", concat_list_path,
    "-c", "copy",
    final_mp4
]
subprocess.run(cmd_concat, check=True)
print(f"Final YouTube video generated successfully at: {final_mp4}")

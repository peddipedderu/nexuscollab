# 🌐 NexusCollab — Humans & Agents, Building Together

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![WebMCP](https://img.shields.io/badge/WebMCP-enabled-8b5cf6)](https://webmachinelearning.github.io/webmcp/)

> A WebMCP-powered collaborative knowledge platform where humans and AI agents co-create documents, research cards, and knowledge graphs in real time.

**🔗 Live Demo:** https://nexuscollab.fly.dev

---

## What is NexusCollab?

NexusCollab is a collaborative document editor where **you and an AI agent work side-by-side**. The human writes freely; the agent can read the document, insert content, extract knowledge nodes, cite research, and annotate insights — all through **WebMCP structured tools** registered directly in the browser.

### Why WebMCP?

Traditional agents must guess their way through a web page's HTML. WebMCP eliminates this by letting the page declare **exactly what actions are available** via `document.modelContext.registerTool()`. This makes collaboration:
- ✅ **Reliable** — agent calls defined functions, not DOM guesses
- ✅ **Efficient** — up to 85% fewer tokens than screen-scraping
- ✅ **Real-time** — tools execute instantly in the browser
- ✅ **Transparent** — every agent action is logged and visible

---

## Registered WebMCP Tools

| Tool | Description |
|------|-------------|
| `insert_content` | Write paragraphs, headings, or bullet lists |
| `read_document` | Read full document content & word count |
| `add_knowledge_node` | Add concepts to the knowledge graph |
| `add_research_card` | Insert structured citation cards |
| `add_annotation` | Highlight & annotate sections |
| `set_document_title` | Update the document title |
| `get_stats` | Get document & collaboration statistics |

---

## WebMCP Implementation

```javascript
await document.modelContext.registerTool({
  name: 'insert_content',
  title: 'Insert Content into Document',
  description: 'Insert a new block of text, heading, or bullet list into the collaborative document.',
  inputSchema: {
    type: 'object',
    properties: {
      content: { type: 'string' },
      blockType: { type: 'string', enum: ['paragraph','heading1','heading2','heading3','bullet'] },
      position: { type: 'string', enum: ['end','start'] }
    },
    required: ['content']
  },
  async execute({ content, blockType = 'paragraph', position = 'end' }) {
    return insContent(content, blockType, position);
  }
}, { signal: abortController.signal });
```

Tools use an `AbortController` signal for proper lifecycle management.

---

## Getting Started

### Prerequisites
- Node.js 18+
- npm

### Run locally

```bash
git clone https://github.com/peddipedderu/nexuscollab.git
cd nexuscollab
npm install
npm start
# Open http://localhost:8080
```

### Test with WebMCP

1. **ChatGPT browser** — open the live URL directly in ChatGPT's in-app browser (WebMCP enabled by default)
2. **Chrome** — go to `chrome://flags/#enable-webmcp-testing` → Enable → relaunch → open the URL

Then ask ChatGPT to:
> *"Read the document, then add a heading called 'Key Insights', write a paragraph about human-agent collaboration, and add 3 knowledge nodes."*

---

## Deployment

### Fly.io

```bash
fly launch --name nexuscollab
fly deploy
```

### Docker

```bash
docker build -t nexuscollab .
docker run -p 8080:8080 nexuscollab
```

---

## Project Structure

```
nexuscollab/
├── public/
│   └── index.html      # Full SPA — WebMCP tools registered here
├── server.js           # Express static server
├── package.json
├── Dockerfile
├── fly.toml
└── README.md
```

---

## License

MIT © 2026 [peddipedderu](https://github.com/peddipedderu)

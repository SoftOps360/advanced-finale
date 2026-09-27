# Episode 22 — Advanced: RAG vs Fine-tuning, Multi-Agent & What's Next (Series Finale)

The last episode. We answer the question everyone asks next — *"should I fine-tune?"* — look at
multi-agent systems and where ops-AI is heading, and recap the whole build.

## RAG vs fine-tuning (the question everyone asks)

> **RAG supplies KNOWLEDGE at question time. Fine-tuning teaches BEHAVIOUR / STYLE / FORMAT.**
> They're not rivals — and for most **ops** work, the answer is **RAG**.

- **Use RAG when:** the knowledge changes (runbooks, incidents), you need **citations** and
  freshness, the facts live in **your docs**, and you have no labeled dataset. → almost all ops.
- **Use fine-tuning when:** you need a **consistent format/tone** every time, you have **many
  labeled examples**, or you want to shrink long repeated prompts. It changes *how* the model
  behaves, not *what* it knows — and it goes **stale** as your data changes.
- **Combine** when you need both: fine-tune the style, RAG the facts.

`decide.py` makes this concrete — feed it traits of your use case and it recommends, with reasons.
Run it: `python decide.py`. (Rule of thumb baked in: **start with RAG** — cheaper, fresher, explainable.)

## Multi-agent systems

One agent is a loop (Ep12). A **multi-agent** system composes several: a *planner* splits the
work, *workers* each handle a piece (often with different tools), and a *synthesizer* combines the
results. It can help for genuinely parallel or specialized tasks — but it multiplies cost, latency,
and failure modes. **Don't reach for it first.** A single well-guardrailed agent (Ep11–13) solves
most ops problems; add agents only when one truly can't hold the task.

## Where ops-AI is heading (and how to stay sane)

Models, protocols (MCP), and tooling change fast. What **doesn't** change is the discipline this
series is built on: retrieve real context, keep humans in the loop for writes, guardrail the
tools, measure with evals, watch cost, and secure the pipeline. Chase capabilities; keep the
engineering.

## The series, in one page

**Part 1 — Fundamentals (prereq):** AI vs ML vs LLM · tokens/context/hallucination/temperature · RAG · agents · MCP.
**Part 2 — Practical skills:** first LLM app · prompt engineering · structured output & tool calling · choosing a model · running locally.
**Part 3 — AI for Ops:** log triage (Ep7) · summarize/watch logs (Ep8) · RAG over runbooks (Ep9) · retrieval quality (Ep10) · agent tools (Ep11) · the agent loop (Ep12) · **safety & guardrails (Ep13)**.
**Part 4 — Integration:** MCP server (Ep14) · ChatOps in Slack (Ep15) · AI in CI/CD & alerting (Ep16) · self-hosting & privacy (Ep17).
**Part 5 — Production:** evals (Ep18) · observability, cost & reliability (Ep19) · deploy (Ep20) · security & DevSecOps (Ep21) · **this finale (Ep22)**.

## The five ideas to keep

1. **The LLM proposes; your code disposes.** It asks for tools; you run them; policy gates writes.
2. **Retrieval quality is the ceiling.** Ground answers in your docs; cite; say "I don't know".
3. **Read-only by default, human-approved writes, blast-radius limits, audit.** Even a fooled
   prompt can't delete prod.
4. **Measure it** (evals) and **operate it** (cost, retries, fallback, health) like any service.
5. **Same code, swappable backend** — Groq / OpenAI / local Ollama via one `base_url`.

## Run it

```bash
python decide.py     # RAG vs fine-tuning advisor - pure Python, no key
```

## Honesty & limits (please keep these in the video)

- **`decide.py` is a rule of thumb, not an oracle.** The weights are opinions; use it to make the
  trade-off explicit, then decide with your own context and a small eval.
- **Fine-tuning isn't magic and isn't free.** It needs quality labeled data, costs to train, and
  goes stale — many teams that "need fine-tuning" actually needed better retrieval or prompting.
- **Multi-agent is often over-used.** More agents = more cost, latency, and ways to fail. Prefer
  one solid agent until you can prove you need more.
- **This series is a foundation, not the finish line.** The tools you built are real, but keep
  threat-modeling, evaluating, and updating as the landscape moves. Thanks for building along. 🙏

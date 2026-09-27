"""RAG vs fine-tuning: a decision helper. No AI, no key - just a transparent rule of thumb.

The most common question after this series: "should I fine-tune a model on my data?" For almost
all OPS work the answer is RAG, and this makes the reasoning explicit. Fine-tuning teaches new
BEHAVIOUR/STYLE/FORMAT; RAG supplies fresh KNOWLEDGE at question time. They also combine.
"""

# Each trait pushes toward RAG or FINE-TUNE. Weights are a rule of thumb, not a law.
SIGNALS = {
    # trait: (points_to_rag, points_to_finetune, why)
    "knowledge_changes_often":   (2, 0, "docs/runbooks change -> RAG stays fresh; a fine-tune goes stale"),
    "need_citations":            (2, 0, "must show WHERE an answer came from -> RAG cites sources"),
    "answers_from_your_docs":    (2, 0, "facts live in your docs -> retrieve them, don't bake them in"),
    "no_labeled_examples":       (1, 0, "fine-tuning needs a labeled dataset you may not have"),
    "need_consistent_format":    (0, 2, "always emit a strict style/format -> fine-tuning learns it"),
    "need_new_behavior_or_tone": (0, 2, "change how it behaves, not what it knows -> fine-tune"),
    "have_many_labeled_examples":(0, 2, "you have thousands of good examples -> fine-tuning can use them"),
    "shrink_prompt_for_latency": (0, 1, "bake repeated instructions in to cut prompt size/cost"),
}


def recommend(traits):
    rag = ft = 0
    reasons = []
    for trait, on in traits.items():
        if on and trait in SIGNALS:
            r, f, why = SIGNALS[trait]
            rag += r
            ft += f
            reasons.append(("RAG" if r >= f else "FINE-TUNE", why))
    if rag == ft == 0:
        verdict = "RAG (default for ops)"
    elif rag >= ft:
        verdict = "RAG"
    else:
        verdict = "FINE-TUNE (and consider RAG on top for facts)"
    return verdict, rag, ft, reasons


SCENARIOS = {
    "Answer from our runbooks (this whole series)": {
        "knowledge_changes_often": True, "need_citations": True,
        "answers_from_your_docs": True, "no_labeled_examples": True},
    "Always output our exact incident-report format": {
        "need_consistent_format": True, "have_many_labeled_examples": True,
        "need_new_behavior_or_tone": True},
    "Adopt our terse house style AND cite live docs": {
        "need_consistent_format": True, "knowledge_changes_often": True,
        "need_citations": True, "answers_from_your_docs": True},
}

if __name__ == "__main__":
    for name, traits in SCENARIOS.items():
        verdict, rag, ft, reasons = recommend(traits)
        print(f"\n{name}\n  -> {verdict}   (RAG {rag} vs fine-tune {ft})")
        for side, why in reasons:
            print(f"     [{side}] {why}")
    print("\nRule of thumb: RAG for KNOWLEDGE (most ops work); fine-tune for BEHAVIOUR/FORMAT; "
          "combine when you need both. Start with RAG - it's cheaper, fresher, and explainable.")

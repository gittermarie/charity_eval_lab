# Charity Evaluation Lab

A small Streamlit app for a charity evaluation workshop.

## Run locally

Requires Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows
pip install -r requirements.txt
streamlit run app.py
```

## What it does

- Four charity profiles with logos, selected report visuals, source-linked evaluation metrics, evidence types, and caveats.
- A scenario sandbox separating illustrative outcome quantities from moral weights, with adjustable sensitivity ranges.
- A budget allocation interface with CSV export.
- Discussion prompts for empirical uncertainty, counterfactuals, moral weights, and decision quality.

## Important limitations

The scenario inputs in the sandbox are illustrative placeholders, not estimates of actual impact. The resulting score is not a valid cross-charity cost-effectiveness estimate. Replace the placeholders only if the workshop has explicitly agreed on a defensible model and documented sources for its inputs.

Sandbox uncertainty bands are user-set sensitivity ranges for each illustrative outcome input and moral weight, not statistical confidence intervals or probability estimates. The displayed score range combines all input lower bounds and all input upper bounds as scenarios; it is not an evidence-based uncertainty bound.

The profile metrics are curated snapshots from the linked reports and evaluations, not automatically refreshed data. Their periods, methods, and caveats differ, so do not compare the values as if they shared a common scale. Check the linked sources for updates before a workshop.

The other resource URLs are starting points. Before the workshop, check that each page is current and select the exact reports / sections you want participants to read.

## Suggested workshop use

1. Participants read the profiles and record an initial allocation.
2. Small groups review the source material and identify major uncertainties.
3. Groups use the sandbox to test assumptions, not to produce an authoritative ranking.
4. Participants submit a final allocation and explain what changed.

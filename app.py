from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Charity Evaluation Lab", page_icon="⚖️", layout="wide")

DATA_DIR = Path(__file__).parent / "data"
CHARITIES = {
    "Helen Keller Intl": {
        "logo": DATA_DIR / "HellenKeller.png",
        "category": "Global health",
        "mission": "Supports vitamin A supplementation and other public-health programmes to improve health and survival, especially among children.",
        "pathway": "Funding → supplements procured and distributed → children reached → deficiency and illness reduced → health and survival improve.",
        "profile_visual": {
            "image": DATA_DIR / "helen_keller_mission.png",
            "title": "Global needs and reported reach",
            "caption": "This organizational infographic pairs broad global need figures with Helen Keller Intl's reported reach. The figures are undated in the image and are context, not a causal impact estimate.",
            "source": "https://www.helenkellerintl.org/",
            "source_label": "Helen Keller Intl website",
        },
        "evidence": "GiveWell's charity and technical assessments discuss the evidence base, implementation data, cost-effectiveness, and important uncertainties.",
        "risks": ["Current effect may differ from older studies", "Coverage and implementation estimates may be uncertain", "Marginal funding needs may change over time"],
        "report_metrics": [
            {
                "metric": "Estimated cost per child death averted",
                "result": "About $1,000–$8,500",
                "period": "GiveWell estimate as of Feb 2024",
                "evidence_type": "Modelled outcome",
                "caveat": "Varies by location; based on uncertain evidence, including trials mostly conducted decades ago. Not a measured count of deaths averted by Helen Keller Intl.",
                "source": "https://www.givewell.org/international/technical/programs/vitamin-A",
            },
            {
                "metric": "Estimated reduction in child mortality from vitamin A supplementation",
                "result": "About 4%–12%",
                "period": "GiveWell estimate, published Apr 2024",
                "evidence_type": "Modelled outcome",
                "caveat": "Estimate varies by location and is adjusted for study limitations and changes in child health since the trials.",
                "source": "https://www.givewell.org/international/technical/programs/vitamin-A",
            },
        ],
        "links": [
            ("Helen Keller Intl website", "https://www.helenkellerintl.org/"),
            ("GiveWell charity evaluation", "https://www.givewell.org/charities/helen-keller-international"),
            ("GiveWell vitamin A technical assessment", "https://www.givewell.org/international/technical/programs/vitamin-A"),
            ("Giving What We Can profile", "https://www.givingwhatwecan.org/charities/helen-keller-international"),
        ],
        "published_metric": "Use the latest GiveWell assessment for current cost-effectiveness estimates. Older headline figures should be labelled with their analysis date.",
    },
    "The Humane League": {
        "logo": DATA_DIR / "the-human-league-logo-wide.png",
        "category": "Animal welfare",
        "mission": "Works to reduce farmed-animal suffering, particularly through corporate campaigns and accountability for animal-welfare commitments.",
        "pathway": "Campaigns and pressure → corporate commitments → implementation and compliance → changes in animals' living conditions → welfare effects.",
        "profile_visual": {
            "image": DATA_DIR / "humane_league_eval_overview.png",
            "title": "Animal Charity Evaluators: The Humane League at a glance",
            "caption": "ACE's 2025 overview includes its estimate of animals helped per dollar. Treat this as an evaluator estimate, not a directly counted or independently attributable outcome.",
            "source": "https://animalcharityevaluators.org/charity-review/the-humane-league/",
            "source_label": "Animal Charity Evaluators review",
        },
        "evidence": "Animal Charity Evaluators provides an external assessment; the organisation also publishes its own impact and annual reports.",
        "risks": ["Commitments may not be implemented fully", "Animals covered is not the same as welfare improvement", "Duration, severity, and counterfactual changes matter"],
        "report_metrics": [
            {
                "metric": "Hens reported spared from cages",
                "result": "4.6 million",
                "period": "2024",
                "evidence_type": "Organization-reported impact estimate",
                "caveat": "The report's summary does not provide an independently auditable attribution method.",
                "source": "https://thehumaneleague.org/annual-report-2024",
            },
            {
                "metric": "Corporate cage-free commitments due by 2023 or earlier reported fulfilled",
                "result": "89%",
                "period": "Reported in 2024 annual report",
                "evidence_type": "Reported implementation indicator",
                "caveat": "Fulfilment is a useful implementation measure, but not itself a direct measure of animal welfare.",
                "source": "https://thehumaneleague.org/annual-report-2024",
            },
            {
                "metric": "US egg-laying hens reported living outside cages",
                "result": "40%",
                "period": "2024",
                "evidence_type": "Sector-level outcome indicator",
                "caveat": "Industry-wide change cannot be attributed to The Humane League alone.",
                "source": "https://thehumaneleague.org/annual-report-2024",
            },
            {
                "metric": "Hens covered by new commitments",
                "result": "79 million",
                "period": "Commitments secured in 2024",
                "evidence_type": "Projected future reach",
                "caveat": "Commitments are prospective and should not be counted as realised welfare improvements.",
                "source": "https://thehumaneleague.org/annual-report-2024",
            },
        ],
        "links": [
            ("Animal Charity Evaluators review", "https://animalcharityevaluators.org/charity-review/the-humane-league/"),
            ("The Humane League impact", "https://thehumaneleague.org.uk/impact"),
            ("Giving What We Can profile", "https://www.givingwhatwecan.org/charities/the-humane-league"),
        ],
        "published_metric": "Treat 'animals affected' figures as reach or projected reach unless the source explicitly measures realised welfare improvements.",
    },
    "GovAI": {
        "logo": DATA_DIR / "GovAI_logo.png",
        "category": "AI governance",
        "mission": "Conducts research and develops expertise to help decision-makers navigate advanced AI and its societal implications.",
        "pathway": "Funding → research and talent development → ideas and expertise reach decision-makers → decisions or institutions change → downstream outcomes.",
        "focus_areas": [
            ("Threat modeling", "Assess evidence about potential AI-enabled security risks and how future capabilities could change them."),
            ("Risk management", "Explore how AI developers, evaluators, auditors, and governments can manage deployment risks."),
            ("Economics of AI", "Study AI's effects on work, growth, and competition, and the policy options available."),
            ("Frontier AI regulation", "Analyze proposed rules for advanced AI and the trade-offs they create."),
            ("Geopolitics and military AI", "Examine international competition, cooperation, and AI's military applications."),
            ("Government adoption", "Understand how public agencies can adopt AI effectively and manage associated barriers and risks."),
            ("Technical governance", "Develop technical approaches that can support policy and governance goals."),
            ("Frontier research", "Study longer-term AI capability trajectories and ways to anticipate future policy challenges."),
        ],
        "evidence": "Use GovAI's annual report, research publications, and concrete examples of policy engagement. Outputs and influence are not the same as final social impact.",
        "risks": ["Attribution of policy change is difficult", "Research may not affect decisions", "The direction and scale of future AI risks are uncertain"],
        "report_metrics": [
            {
                "metric": "Quantified downstream impact attributable to GovAI",
                "result": "No estimate reported",
                "period": "2025 annual report",
                "evidence_type": "Evidence gap",
                "caveat": "The report does not quantify attributable policy change or resulting risk reduction.",
                "source": "https://www.governance.ai/post/annual-report-2025",
            },
            {
                "metric": "Documented policy engagement: GovAI researcher served as vice-chair in drawing up the EU Code of Practice for general-purpose AI",
                "result": "Documented role",
                "period": "2025",
                "evidence_type": "Qualitative contribution evidence",
                "caveat": "A role in the process does not establish which provisions changed because of GovAI or what downstream effects followed.",
                "source": "https://cdn.governance.ai/GovAI_Annual_Report_2025.pdf#page=15",
            },
        ],
        "links": [
            ("About GovAI", "https://www.governance.ai/about-us"),
            ("Annual reports and updates", "https://www.governance.ai/"),
            ("Research publications", "https://www.governance.ai/research"),
            ("Giving What We Can profile", "https://www.givingwhatwecan.org/charities/govai"),
        ],
        "published_metric": "Avoid forcing a cost-per-life-saved estimate. Track outputs, influence evidence, additionality, and the assumptions connecting them to outcomes.",
    },
    "Giving What We Can": {
        "logo": DATA_DIR / "gwwc-logo.png",
        "category": "Effective giving / meta",
        "mission": "Encourages and enables people to give more to charities expected to do unusually large amounts of good through their pledge program and effective charities recommendations.",
        "pathway": "Outreach, research, and tools → changes in donor behaviour → additional donations to effective charities → recipient programmes create impact.",
        "profile_visual": {
            "image": DATA_DIR / "gwwc_2025_pledge_donation_dist.png",
            "title": "Where pledge donations go",
            "caption": "The 2025 evaluation's breakdown of pledge donations by cause area. This describes the distribution of giving, not the impact caused by Giving What We Can.",
            "source": "https://docs.google.com/document/d/1GPFnzgSL_HROQYoDDjvYyT_WiPtI1skTfc3NGA0l0Bk/edit",
            "source_label": "GWWC 2025 impact evaluation",
        },
        "evidence": "Its impact evaluation estimates additional giving and organisational costs, while acknowledging counterfactual and marginal-impact limitations.",
        "risks": ["Some donations might have happened anyway", "Pledgers may change giving over time", "Average impact may not represent marginal impact"],
        "report_metrics": [
            {
                "metric": "Estimated giving multiplier",
                "result": "7.1× best guess",
                "period": "2025 evaluation",
                "evidence_type": "Modelled average counterfactual estimate",
                "caveat": "Retrospective average, not a forecast or marginal return; depends on assumptions about counterfactuality and future giving.",
                "source": "https://docs.google.com/document/d/1GPFnzgSL_HROQYoDDjvYyT_WiPtI1skTfc3NGA0l0Bk/edit",
            },
            {
                "metric": "Estimated additional donations to highly effective charities",
                "result": "$16.1 million, at a cost of $2.3 million",
                "period": "2025 evaluation",
                "evidence_type": "Modelled counterfactual estimate",
                "caveat": "Not directly observed as donations caused; relies partly on self-reported data and counterfactual assumptions. Figures are in 2025 USD.",
                "source": "https://www.givingwhatwecan.org/impact",
            },
            {
                "metric": "Combined-conservative giving multiplier",
                "result": "1.5×",
                "period": "2025 evaluation",
                "evidence_type": "Conservative modelled scenario",
                "caveat": "A sensitivity case, not a confidence interval; it depends on a different set of conservative assumptions.",
                "source": "https://docs.google.com/document/d/1GPFnzgSL_HROQYoDDjvYyT_WiPtI1skTfc3NGA0l0Bk/edit",
            },
        ],
        "links": [
            ("Impact evaluation", "https://www.givingwhatwecan.org/impact"),
            ("Impact overview", "https://www.givingwhatwecan.org/impact"),
            ("Evaluating charity evaluators", "https://www.givingwhatwecan.org/why-and-how-gwwc-evaluates-the-evaluators"),
        ],
        "published_metric": "Separate estimated additional donations from the downstream impact of recipient charities; do not treat a giving multiplier as a universal marginal return.",
    },
}

st.title("Charity Evaluation Lab")
st.caption("Workshop prototype · evidence browser + transparent assumption sandbox")

with st.expander("How to use this app and interpret its numbers", expanded=True):
    st.markdown("""
    - **Profiles** link to primary and evaluator material. Check the date and methodology of any figure before using it.
    - **Assumptions sandbox** is a discussion aid, not a validated cross-cause cost-effectiveness model.
    - Assumption sandbox units and weights are user-set assumptions, not estimates of real-world charity impact.
    - The model deliberately separates *empirical assumptions* (what outcomes a donation might cause) from *moral weights* (how those outcomes are valued).
    - Do not compare published metrics from different evaluators as if they were measured on a common scale.
    """)

tab_profiles, tab_model, tab_allocation, tab_prompts = st.tabs(
    ["1 · Charity profiles", "2 · Assumption sandbox", "3 · Budget allocation", "4 · Discussion prompts"]
)
with tab_profiles:
    selected = st.selectbox("Choose a charity", list(CHARITIES.keys()))
    c = CHARITIES[selected]

    with st.container(border=True):
        logo_col, intro_col = st.columns([1, 4])
        with logo_col:
            st.image(c["logo"], width=180)
        with intro_col:
            st.markdown(f"## {selected}")
            st.caption(c["category"])

    if "profile_visual" in c:
        visual = c["profile_visual"]
        with st.container(border=True):
            st.markdown(f"### {visual['title']}")
            st.write(visual["caption"])
            st.markdown(f"[Source: {visual['source_label']}]({visual['source']})")
            st.image(visual["image"])

    mission_col, pathway_col = st.columns(2)
    with mission_col:
        with st.container(border=True):
            st.markdown("### Mission")
            st.write(c["mission"])
    with pathway_col:
        with st.container(border=True):
            st.markdown("### Theory of change")
            st.write(c["pathway"])

    if "focus_areas" in c:
        st.markdown("### What GovAI works on")
        st.caption(
            "A plain-language summary of GovAI's current research focus areas. "
            "[See GovAI's overview](https://www.governance.ai/about-us)."
        )
        focus_cols = st.columns(2)
        for i, (title, description) in enumerate(c["focus_areas"]):
            with focus_cols[i % 2]:
                with st.container(border=True):
                    st.markdown(f"**{title}**")
                    st.write(description)

    evidence_col, cautions_col = st.columns(2)
    with evidence_col:
        with st.container(border=True):
            st.markdown("### Evidence to consult")
            st.write(c["evidence"])
    with cautions_col:
        with st.container(border=True):
            st.markdown("### Key evaluation cautions")
            for risk in c["risks"]:
                st.markdown(f"- {risk}")

    st.markdown("### Latest outcome and evaluation evidence")
    st.caption(
        "These measures use different units and methods; compare each with its own caveats, "
        "not as a cross-charity ranking. Reported reach, implementation, and modelled impact are distinguished below."
    )
    for metric in c["report_metrics"]:
        with st.container(border=True):
            metric_col, result_col = st.columns([3, 2])
            with metric_col:
                st.markdown(f"**{metric['metric']}**")
            with result_col:
                st.markdown(f"**Result:** {metric['result']}")
            st.caption(f"{metric['period']} · {metric['evidence_type']}")
            st.markdown(f"**Caveat:** {metric['caveat']}")
            st.markdown(f"[Open source]({metric['source']})")

    st.info(c["published_metric"])
    st.markdown("### Explore further")
    resource_cols = st.columns(2)
    for i, (label, url) in enumerate(c["links"]):
        with resource_cols[i % 2]:
            st.link_button(label, url)


with tab_model:
    st.subheader("Explore how assumptions change the ranking")
    st.warning("All outcome quantities below are illustrative scenario inputs. They are not published estimates for these charities.")
    st.markdown("""
    Define three abstract outcome dimensions for a hypothetical €1,000 donation:
    - **Human health benefit units**: a normalised proxy for health gains.
    - **Animal welfare benefit units**: a normalised proxy for animal welfare improvements.
    - **Future-risk reduction units**: a normalised proxy for reducing severe future risks.

    The units are not inherently comparable. The weights below are the explicit conversion assumptions that make a combined score possible.
    """)

    defaults = {
        "Helen Keller Intl": {"health": 8.0, "animal": 0.0, "future": 0.1, "indirect": 0.0},
        "The Humane League": {"health": 0.0, "animal": 8.0, "future": 0.1, "indirect": 0.0},
        "GovAI": {"health": 0.2, "animal": 0.1, "future": 6.0, "indirect": 1.0},
        "Giving What We Can": {"health": 2.0, "animal": 2.0, "future": 1.0, "indirect": 5.0},
    }
    st.markdown("#### 1. Set illustrative outcomes and uncertainty per €1,000")
    st.caption(
        "Set each outcome value and its uncertainty independently. Uncertainty is an absolute range "
        "in that outcome's units, not a statistical confidence interval."
    )
    inputs = {}
    cols = st.columns(2)
    for i, name in enumerate(CHARITIES):
        with cols[i % 2]:
            st.markdown(f"**{name}**")
            with st.container(border=True):
                vals = {}
                for key, label in [
                    ("health", "Human health units"),
                    ("animal", "Animal welfare units"),
                    ("future", "Future-risk reduction units"),
                    ("indirect", "Indirect-system-change units"),
                ]:
                    value_col, uncertainty_col = st.columns(2)
                    with value_col:
                        vals[key] = st.number_input(
                            label,
                            min_value=0.0,
                            max_value=100.0,
                            value=float(defaults[name][key]),
                            step=0.5,
                            key=f"out_{name}_{key}",
                        )
                    with uncertainty_col:
                        vals[f"{key}_uncertainty"] = st.slider(
                            f"{label} uncertainty (± units)",
                            min_value=0.0,
                            max_value=100.0,
                            value=min(100.0, round(float(defaults[name][key]) * 0.5) / 2),
                            step=0.5,
                            key=f"out_uncertainty_{name}_{key}",
                            help="Sets the lower and upper sensitivity bounds for this outcome value.",
                        )
                inputs[name] = vals

    st.markdown("#### 2. Choose moral weights")
    st.caption("Set an uncertainty range for each moral weight too; these bounds are scenarios, not probability distributions.")
    wcols = st.columns(4)
    weights = {}
    weight_uncertainties = {}
    for column, (key, label) in zip(
        wcols,
        [
            ("health", "Human health"),
            ("animal", "Animal welfare"),
            ("future", "Future-risk reduction"),
            ("indirect", "Indirect system change"),
        ],
    ):
        with column:
            weights[key] = st.slider(
                label,
                min_value=0.0,
                max_value=10.0,
                value=1.0,
                step=0.25,
                key=f"weight_{key}",
            )
            weight_uncertainties[key] = st.slider(
                f"{label} uncertainty (± weight units)",
                min_value=0.0,
                max_value=10.0,
                value=0.25,
                step=0.25,
                key=f"weight_uncertainty_{key}",
                help="Sets lower and upper sensitivity bounds for this moral weight.",
            )

    rows = []
    for name, vals in inputs.items():
        score = sum(vals[k] * weights[k] for k in weights)
        lower = sum(
            max(0.0, vals[k] - vals[f"{k}_uncertainty"])
            * max(0.0, weights[k] - weight_uncertainties[k])
            for k in weights
        )
        upper = sum(
            min(100.0, vals[k] + vals[f"{k}_uncertainty"])
            * min(10.0, weights[k] + weight_uncertainties[k])
            for k in weights
        )
        rows.append({
            "Charity": name,
            "Illustrative score per €1,000": score,
            "Lower scenario": lower,
            "Upper scenario": upper,
            "Lower error": score - lower,
            "Upper error": upper - score,
        })
    df_scores = pd.DataFrame(rows).sort_values("Illustrative score per €1,000", ascending=False)
    st.markdown("#### Result")
    st.dataframe(
        df_scores[["Charity", "Illustrative score per €1,000", "Lower scenario", "Upper scenario"]],
        use_container_width=True,
        hide_index=True,
    )
    fig = px.bar(df_scores, x="Charity", y="Illustrative score per €1,000",
                 error_y="Upper error", error_y_minus="Lower error",
                 title="Scenario score (not a factual impact estimate)")
    st.plotly_chart(fig, use_container_width=True)
    st.caption(
        "Bars show central assumptions; whiskers show the combined lower/upper scenarios when "
        "each outcome and each moral weight is set to its lower or upper bound. These are "
        "user-defined sensitivity ranges, not confidence intervals or probability estimates."
    )
    st.caption("A high score means only that the chosen scenario inputs and weights favour that option. Try changing one assumption at a time and observe when the ranking changes.")


with tab_allocation:
    st.subheader("Allocate the workshop budget")
    budget = st.number_input("Total budget (€)", min_value=1, max_value=100000, value=100, step=100)
    st.markdown("Move the sliders to allocate the budget. Values are normalised proportionally if they do not sum to 100%.")
    alloc = {}
    a_cols = st.columns(2)
    for i, name in enumerate(CHARITIES):
        with a_cols[i % 2]:
            alloc[name] = st.slider(f"{name} (%)", 0, 100, 25, 1, key=f"alloc_{name}")
    total_pct = sum(alloc.values())
    if total_pct == 0:
        st.error("Allocate at least 1% to one charity.")
    else:
        rows = []
        for name, pct in alloc.items():
            share = pct / total_pct
            rows.append({"Charity": name, "Normalised share": share, "Donation (€)": budget * share})
        adf = pd.DataFrame(rows)
        st.dataframe(adf.assign(**{"Normalised share": adf["Normalised share"].map(lambda x: f"{x:.1%}"),
                                   "Donation (€)": adf["Donation (€)"].map(lambda x: f"€{x:,.2f}")}),
                     use_container_width=True, hide_index=True)
        fig = px.pie(adf, names="Charity", values="Donation (€)", title="Proposed allocation")
        st.plotly_chart(fig, use_container_width=True)
        st.download_button("Download allocation as CSV", adf.to_csv(index=False).encode("utf-8"),
                           file_name="charity_allocation.csv", mime="text/csv")

with tab_prompts:
    st.subheader("Questions for group discussion")
    st.markdown("""
    **Empirical**
    - What is the strongest evidence that the intervention works?
    - Which step in the theory of change is least certain?
    - What would an additional €100 fund, specifically?
    - Are the figures observed outcomes, projected reach, or modelled counterfactuals?

    **Normative**
    - How should we compare human health gains with animal welfare improvements?
    - How should uncertainty about future generations or catastrophic risks affect decisions?
    - Does a moral weight represent value per unit, priority under uncertainty, or both?

    **Decision quality**
    - Which single assumption most changes your ranking?
    - What evidence would change your mind?
    - What is the strongest case against your preferred charity?
    - How confident are you in the allocation, and what would you want to learn next?
    """)

# FM Enhanced Data Hub

A beginner-friendly Python project to analyze Football Manager player exports in a more flexible way than the in-game Data Hub. The app is meant to accept an exported file, apply a minimum-minutes threshold, and help compare players across the uploaded cohort with tables and charts. The current direction is to let filtering happen inside Football Manager before export, then use the app for deeper comparison and underperformance analysis.[cite:32][web:211]

## Project goal

This project is being built as a first Python project and as an MVP for a better Football Manager data-analysis workflow.[cite:32] The aim is not to replace every FM screen, but to give clearer player comparison across different scenarios such as squad review, league benchmarking, competition-specific analysis, and role-based underperformance checks.[cite:32][web:223]

## Current MVP direction

The MVP focuses on a simple workflow:

1. Filter players inside Football Manager.
2. Export the visible data.
3. Upload the file into the app.
4. Apply a minimum minutes filter.
5. Compare players using tables and selectable metrics.
6. Use visuals to spot strengths, weaknesses, and outliers.[cite:32]

The app should become a reusable analysis workspace rather than a one-chart tool. Role-aware and context-aware comparison matters more than one fixed graph, especially when switching between attackers, midfielders, defenders, and goalkeepers.[web:223][web:222]

## What the app should do

The app should support multiple player-analysis scenarios from the same uploaded cohort:

- Compare players inside the same squad.[cite:32]
- Compare players across the same league.[cite:32]
- Compare players across multiple leagues.[cite:32]
- Compare players within a specific competition.[cite:32]
- Check whether a player is underperforming relative to the metrics that matter for the role.[cite:32]

The uploaded file defines the comparison universe. Filtering should mostly happen in-game before export, while the app focuses on validation, metric handling, ranking, comparison, and visualization.[cite:32]

## MVP scope

The first useful version should stay small and practical:

- Upload CSV first; HTML/web-page export support can follow. pandas can read HTML tables through `read_html()`, which is a likely path for real FM exports later.[web:214][web:206]
- Keep only the minimum-minutes filter in the app for now.[cite:32]
- Show a cleaned dataframe preview.
- Let the user select comparison metrics dynamically.
- Show a sortable comparison table.
- Show a scatter plot with selectable axes instead of a fixed goals-vs-assists chart.
- Add a simple player weakness or underperformance summary later.[cite:32]

## What is intentionally out of scope for now

These features are useful, but they are not part of the first milestone:

- Direct Football Manager integration.
- Automatic tactic analysis.
- Database storage.
- Accounts or authentication.
- Full recruitment recommendation engine.
- Complex multi-file merging.
- Over-engineered backend structure.

This keeps the project realistic for a first Python build while still making it genuinely useful.[cite:32]

## Tech stack

The planned starter stack is:

- Python
- Streamlit
- pandas
- Plotly

This stack is enough to support file upload, dataframe processing, and interactive charts in a single beginner-friendly app.[web:211][web:137][web:112]

## Current app status

At the current stage, the app can:

- Upload a normal CSV file.
- Read it into pandas.
- Display the data.
- Render a basic chart.

That confirms the project foundation is working. The next step is to replace the generic chart with more useful role-aware comparison views and then adapt the input handling to real FM exports.[web:182][cite:32]

## Planned improvements

Near-term improvements:

- Support FM-style exported data consistently.
- Build a small fake FM dataset for testing.
- Add numeric metric selection.
- Use only minutes as the first filter.
- Add ranking views for chosen metrics.
- Add player-focused underperformance summaries.

Later improvements:

- HTML import for FM web-page exports with `pandas.read_html()`.[web:214]
- Better column mapping for FM export headers.
- Position-aware analysis modes such as Attack, Midfield, Defence, and Goalkeeping.[web:222][web:223]
- Tactic weakness analysis in a future phase.[cite:32]

## Suggested project structure

A simple structure is enough at the start:

```text
fm-enhanced-data-hub/
├── app.py
├── README.md
├── requirements.txt
└── sample_data/
    └── test_fm.csv
```

Once the app grows, it can move toward:

```text
fm-enhanced-data-hub/
├── app.py
├── pages/
├── parsers/
├── services/
├── charts/
├── sample_data/
└── README.md
```


Example commands:

```bash
pip install streamlit pandas plotly lxml html5lib
streamlit run app.py
```

HTML parser dependencies like `lxml` or `html5lib` may be useful later when supporting HTML table imports through pandas.[web:209][web:206]

## Test CSV example

A simple starter CSV for testing:

```csv
Name,Club,Position,Minutes,Goals,Assists,Average Rating
Hojlund,Man Utd,ST,1800,12,3,6.95
Bruno Fernandes,Man Utd,AM,2500,9,11,7.21
Mainoo,Man Utd,CM,2100,4,5,6.98
Saka,Arsenal,RW,2400,14,10,7.34
Rodri,Man City,DM,2600,6,8,7.41
```

This is only for validating upload, parsing, and display logic. Real FM exports will later need mapping and cleaning logic because export headers may differ from the internal column names expected by the app.[web:2]

## Principles

The project should follow a few simple principles:

- Keep filtering in FM where possible.[cite:32]
- Keep the app focused on comparison and interpretation.[cite:32]
- Prefer flexible metric selection over one hardcoded graph.
- Make the same tool useful for multiple football-analysis scenarios.[cite:32]
- Build in small steps and keep the code understandable.

## Notes

This README is a starting document and is expected to change as the project matures. The current version reflects the MVP direction rather than the final product scope.

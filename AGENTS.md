# AGENTS.md - Jupyter Book Project Guidelines

## Project Overview
This is a comprehensive Jupyter Book project aimed at building a large knowledge archive in the `_build` folder. The project covers multiple domains including frontend development, data science, time series analysis, and more.

## Current Focus
- Codex: threat modeling overview notebook expanded (completed, 2026-02-01 19:17 UTC).
- Codex: transformer forecasting notebook for time series deep learning completed (2026-02-01 20:45 UTC).
- Codex: time series clustering overview expansion completed (2026-02-01 19:17 UTC).
- Codex: changepoint detection notebook in time series anomaly detection completed (2026-02-01 19:13 UTC).
- Codex: exponential smoothing and Holt-Winters notebook for classical forecasting completed (2026-02-01 19:05 UTC).
- Codex: global and hierarchical forecasting notebook added for ML forecasting (2026-02-01 19:02 UTC).
- Codex: placeholder sweep complete (2026-02-01 18:54 UTC).
- Codex: sktime pipelines notebook added in time series pipelines (2026-02-01 18:50 UTC).
- Codex: classical ARIMA/SARIMA forecasting notebook completed (2026-02-01 19:01 UTC).
- Codex: dynamic time warping notebook added for time series classification (2026-02-01 19:01 UTC).

## Core Principles



!IMPORTANT! as long as there are placehlders for ipynbs alwas prioritize those fill them out with the crrespondign topic and explain it in high quality like mentioned it here for example in cyper security or devops system design finance backend frontend there are still palceholders


### 1. Project Structure Understanding
When entering this project:
- **First Action**: Examine the entire project structure
- Understand the current state (status quo)
- Review existing sections and subsections
- Check the `_toc.yml` for navigation structure
- Verify the `index.html` sidebar organization

### 2. Main Sections (DO NOT CHANGE)
The following top-level sections remain fixed:
- Frontend
- Data Science
- Time Series Analysis
- [Other existing main sections]

### 3. Subsection Organization (FLEXIBLE)
Within main sections, you are **encouraged** to:
- Create logical subsections for better organization
- Split broad topics into focused, specific notebooks
- Avoid overly large, monolithic notebooks
- Prefer multiple targeted notebooks over single comprehensive ones

## Content Creation Guidelines

### Notebook Development
1. **Precision & Clarity**
   - Be precise in explanations
   - Provide intuitive understanding of concepts
   - Include practical examples

2. **Visual Explanations**
   - Use **Plotly** for interactive visualizations
   - Embed relevant images from the web when they enhance understanding
   - Create diagrams and charts to illustrate concepts

3. **Mathematical Notation**
   - Use **LaTeX** for all mathematical formulas
   - Ensure proper rendering of equations
   - Provide context for mathematical concepts

4. **Code Quality**
   - Include working, executable code examples
   - Add comments and docstrings
   - Use best practices for each library/framework

### File Format Requirements
- **Use `.ipynb` (Jupyter Notebooks) ONLY** for content
- **Exception**: Keep only `CHANGELOG.md` and `AGENTS.md` as markdown files
- **Remove all other `.md` files** - convert them to `.ipynb`

## Special Focus: Time Series Section

### Priority Requirements
The **Time Series** section requires comprehensive coverage:

1. **sktime Library Coverage**
   - Create **multiple notebooks** covering different sktime functionalities
   - Topics to cover:
     - Forecasting methods (ARIMA, Prophet, exponential smoothing, etc.)
     - Time series classification
     - Time series regression
     - Time series clustering
     - Anomaly detection
     - Feature extraction
     - Transformations and preprocessing
     - Pipeline creation
     - Model selection and evaluation
     - Advanced forecasting (hierarchical, global models)

2. **Other Time Series Methods**
   - Classical statistical methods
   - Deep learning approaches (LSTM, GRU, Transformers)
   - State-space models
   - Facebook Prophet
   - TBATS, BATS
   - Dynamic time warping
   - Seasonal decomposition
   - Changepoint detection

3. **Notebook Organization**
   - Create separate notebooks for each major algorithm/method
   - Use subsections in `_toc.yml` to organize related notebooks
   - Ensure each notebook focuses on a specific area

## Workflow Protocol

### Before Starting Work

1. **Update CHANGELOG.md**
   ```markdown
   ## [Date/Time] - Agent Name
   ### Topic: [Specific topic you're implementing]
   **Start Time**: [Timestamp]
   **Status**: In Progress
   ```

2. **Check for Conflicts**
   - Review CHANGELOG.md to ensure no other agent is working on the same topic
   - Check AGENTS.md for coordination

### During Work

1. **Examine Placeholders**
   - Search for placeholder content throughout the project
   - Fill in all placeholders with complete, quality content

2. **Check TOC Structure**
   - Verify `_toc.yml` organization
   - Ensure sidebar remains navigable
   - Add subsections if needed to prevent clutter
   - Keep hierarchy logical and intuitive

3. **Polish Existing Notebooks**
   - If you encounter incomplete notebooks, you're encouraged to update them
   - Add missing sections, improve explanations, enhance visualizations

### After Completing Work

1. **Update CHANGELOG.md**
   ```markdown
   **End Time**: [Timestamp]
   **Status**: Finished
   **Summary**: [Brief description of what was implemented]
   ```

## Content Enhancement

### Creative Elements
- **Images**: Embed relevant images from the web to make notebooks more appealing
- **Diagrams**: Create flowcharts, architecture diagrams, process flows
- **Interactive Elements**: Use Plotly, widgets, or other interactive tools
- **Real-world Examples**: Include practical, relatable examples

### Quality Standards
1. Each notebook should be self-contained but well-integrated
2. Provide references and sources where appropriate
3. Include practical exercises or examples
4. Add "Further Reading" sections when relevant
5. Ensure code is tested and functional

## File Organization Best Practices

### Notebook Naming
- Use descriptive, lowercase names with underscores
- Examples:
  - `01_arima_forecasting.ipynb`
  - `02_prophet_basics.ipynb`
  - `03_sktime_classification.ipynb`

### Directory Structure
```
project_root/
├── _config.yml
├── _toc.yml
├── CHANGELOG.md
├── AGENTS.md
├── AGENTS.md (this file)
├── frontend/
│   ├── subsection_1/
│   │   ├── notebook_1.ipynb
│   │   └── notebook_2.ipynb
│   └── subsection_2/
├── data_science/
│   ├── machine_learning/
│   ├── deep_learning/
│   └── statistics/
├── timeseries/
│   ├── sktime/
│   │   ├── forecasting/
│   │   ├── classification/
│   │   ├── regression/
│   │   └── transformations/
│   ├── classical_methods/
│   ├── deep_learning_ts/
│   └── evaluation/
└── _build/
```

## Navigation & Accessibility

### TOC Management
- Keep the table of contents (`_toc.yml`) clean and organized
- Use parts/chapters/sections hierarchy effectively
- Ensure sidebar doesn't become overwhelming
- Group related notebooks under meaningful subsections

### Example TOC Structure for Time Series:
```yaml
- file: timeseries/intro
  sections:
  - file: timeseries/sktime/index
    title: sktime Library
    sections:
    - file: timeseries/sktime/forecasting/arima
    - file: timeseries/sktime/forecasting/prophet
    - file: timeseries/sktime/classification/rocket
  - file: timeseries/classical/index
    title: Classical Methods
    sections:
    - file: timeseries/classical/decomposition
    - file: timeseries/classical/exponential_smoothing
```

## Collaboration Guidelines

### Multiple Agents
- Always check CHANGELOG.md before starting
- Update AGENTS.md with your current focus area
- Communicate completed work clearly
- Don't duplicate effort

### Conflict Resolution
- If you find conflicting or duplicate work, consolidate and improve
- Document any major restructuring in CHANGELOG.md
- Maintain consistency in style and formatting across notebooks

## Quality Checklist

Before marking work as complete:
- [ ] Notebook executes without errors
- [ ] All code cells have proper outputs
- [ ] Mathematical notation renders correctly
- [ ] Visualizations display properly
- [ ] Images load correctly
- [ ] Text is clear and well-formatted
- [ ] TOC updated if new files added
- [ ] CHANGELOG.md updated
- [ ] No placeholders remain
- [ ] Related notebooks are cross-referenced

## Common Tasks Reference

### Adding a New Notebook
1. Create `.ipynb` file in appropriate directory
2. Add comprehensive content following guidelines above
3. Update `_toc.yml` with new entry
4. Test build process
5. Update CHANGELOG.md

### Converting MD to IPYNB
1. Copy markdown content
2. Create new notebook
3. Add content in markdown cells
4. Enhance with code examples, visualizations
5. Delete original `.md` file (except CHANGELOG.md, AGENTS.md, AGENTS.md)
6. Update TOC references

### Enhancing Existing Notebook
1. Review current content
2. Identify gaps or areas for improvement
3. Add missing sections
4. Improve code examples
5. Add visualizations
6. Update CHANGELOG.md with improvements

## Resources & Tools

### Recommended Libraries
- **Visualization**: Plotly, Matplotlib, Seaborn
- **Time Series**: sktime, statsmodels, Prophet, pmdarima
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: scikit-learn, XGBoost, LightGBM
- **Deep Learning**: TensorFlow, PyTorch, Keras

### Documentation Standards
- Use clear section headers (##, ###, ####)
- Include code comments
- Provide example outputs
- Add explanatory text between code cells
- Use proper markdown formatting

## Key Reminders

1. **Main sections are fixed** - don't rename or remove them
2. **Subsections are flexible** - organize as needed for clarity
3. **Time series gets priority** - especially sktime coverage
4. **Multiple focused notebooks > one large notebook**
5. **Always update CHANGELOG.md** - before starting and after finishing
6. **Check for placeholders** - fill them in
7. **Verify TOC structure** - keep sidebar navigable
8. **Use .ipynb only** - except CHANGELOG.md and AGENTS.md
9. **Be creative** - use images, interactive elements, real examples
10. **Polish existing work** - don't just add new content

---

## Getting Started Checklist

When you begin work on this project:

1. [ ] Read this AGENTS.md thoroughly
2. [ ] Examine entire project structure
3. [ ] Review `_toc.yml` for current organization
4. [ ] Check `_build` folder status
5. [ ] Read CHANGELOG.md for recent activity
6. [ ] Identify gaps in content (especially time series/sktime)
7. [ ] Update CHANGELOG.md with your planned work
8. [ ] Begin implementation following all guidelines above

---

**Remember**: The goal is a comprehensive, well-organized, highly navigable knowledge archive that serves as an excellent learning resource. Quality, clarity, and organization are paramount.

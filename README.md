[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8087943.svg)](https://doi.org/10.5281/zenodo.8087943)

**This repository contains the Python analysis code used for Campbell and Christensen et al., "Cracking the code: An evidence-based approach to teaching Python in an undergraduate earth science setting" (in review at _Journal of Geoscience Education_).**

Please contact me at [ethancc@uw.edu](mailto:ethancc@uw.edu) if you have any questions regarding this code.

### Attribution:
This code is freely available for reuse as described in the MIT License included in this repository. If using this code in an academic publication, we encourage you to provide the following citations:
* **Preprint**: Campbell, E.C.\*, Christensen, K.M.\*, Nuwer, M., Ahuja, A., Boram, O., Liu, J., Miller, R., Osuna, I., Riser, S.C. (2024). Cracking the code: An evidence-based approach to teaching Python in an undergraduate earth science setting. Earth and Space Open Archive. doi:[10.22541/essoar.168839439.99576639/v2](https://essopenarchive.org/doi/full/10.22541/essoar.168839439.99576639/v2) _(\* Co-first authors, reflecting equal contributions to this work)_
* **Zenodo code archive**: Campbell, E.C. & Christensen, K.M. (2024, June 24). Analysis code for "Cracking the code: An evidence-based approach to teaching Python in an undergraduate earth science setting". Zenodo. doi:[10.5281/zenodo.8087943](https://doi.org/10.5281/zenodo.8087943)

### Description:
* The Jupyter notebook `OCEAN_215_paper_analyses.ipynb` carries out analysis and visualization of anonymized course-related data, as described in the study text. Specifically, the notebook ingests an Excel data file titled `All OCEAN 215 data deidentified.xlsx` containing anonymized metrics organized in separate sheets. We have not made these data publicly available in order to ensure the privacy of student study participants. As indicated by section headers, code in the notebook is used to generate Figs. 2, 3, 4, 5, 6, 7 and Figs. S1, S2 in the Supplemental Materials. Dependencies are minimal and the notebook was last run in Google Colab using the following package versions: NumPy=1.25.2, Pandas=2.0.3, SciPy=1.11.4, Matplotlib=3.7.1.
* The supplementary Python script `student_final_project_code_analysis.py` calculates metrics based on students' submitted final project Python code. The script ingests students' individual Jupyter notebook files, counts occurrences of certain strings, and outputs metrics assessing the breadth of students' code usage.

### Related resources:
* Our OCEAN 215 course materials are available for free reuse and adaptation under a CC-BY-4.0 license at this website: https://ethan-campbell.github.io/OCEAN_215/
* Recorded course lessons are available on our YouTube channel: https://www.youtube.com/@ocean215python
* You can find the GitHub repository for the course website here: https://github.com/ethan-campbell/OCEAN_215

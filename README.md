**This repository contains the Python analysis code used for Campbell and Christensen et al., "Cracking the code: An evidence-based approach to teaching Python in an undergraduate earth science setting" (submitted to _Journal of Geoscience Education_).**

Please contact me at [ethancc@uw.edu](mailto:ethancc@uw.edu) if you have any questions regarding this code.

### Attribution:
This code is freely available for reuse as described in the MIT License included in this repository. If using this code in an academic publication, we encourage you to provide the following citations:
* Campbell, E.C. and Christensen, K.M. (2023, June 13). Analysis code for "Cracking the code: An evidence-based approach to teaching Python in an undergraduate earth science setting" (Version v1.0.0). Zenodo. doi:TBD.
* Study preprint citation (TBD)

### Description:
* The Jupyter notebook `OCEAN_215_paper_analyses.ipynb` carries out analysis and visualization of anonymized course-related data, as described in the study text. Specifically, the notebook ingests an Excel data file titled `All OCEAN 215 data deidentified.xlsx` (available upon reasonable request by email) containing anonymized metrics organized in separate sheets. As indicated by section headers, code in the notebook is used to generate Figs. 2, 3, 4, 5, 6 and Figs. S1, S2, S3 in the Supplemental Materials. Dependencies are minimal and the notebook was last run in Google Colab using the following package versions: NumPy=1.22.4, Pandas=1.5.3, SciPy=1.10.1, Matplotlib=3.7.1.
* The Python script `student_final_project_code_analysis.py` calculates metrics based on students' submitted final project Python code. The script ingests students' individual Jupyter notebook files, counts occurrences of certain strings, and outputs metrics assessing the breadth of students' code usage. We cannot provide the raw project code files, but can offer the calculated anonymized metrics (see above).

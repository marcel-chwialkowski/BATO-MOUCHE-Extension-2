# Lab Research Project

## Project: Accessibility analysis of Paris based on available amenities 

The project is an extension of the BATO-MOUCHE project by Simon Genet, Leopold Maurice and Marie-Olive Thaury. It is also inspired by the work of Yubo Cai (BX24) in his last year's Computer Science Research Project. [Link to the BATO-MOUCH project](https://github.com/LeoMaurice/BATO-MOUCHE-Stat-App). [Link to Yubo's Computer Science Research Project](https://github.com/yubocai-poly/BATO-MOUTCHE-Extension). The project is supervised by Prof. Sarah J. Berkemer. Thank you! 

## External data
Here is where the data used for this project can be found.

1. **Filosofi dataset:** [Données carroyées – Carreau de 200m](https://www.insee.fr/fr/statistiques/4176290?sommaire=4176305#consulter). Here we use the dataset with the name of **Carreau 200m – Geopackage – Métropole - Martinique - La Réunion**.

2. **OSM extracts** Extracts from Open Street Map can be obtained via a number of ways. In some parts of the project, the [OSMnx](https://osmnx.readthedocs.io/en/stable/) library is used for that, you can also download an extract of the whole 
Île-de-France region [here](https://www.interline.io/) (registration required but free). We found it useful for quick manipulation of the extract.


5.  **France GEOJSON files** - Useful for obtaining an OSM extract with a specific shape. Link [here](https://france-geojson.gregoiredavid.fr/)

6.  **GTFS file for IDFM** - Required for calculating travel times. Available [here](https://data.iledefrance-mobilites.fr/explore/dataset/offre-horaires-tc-gtfs-idfm/information/) after registration, but free of charge.

 ## Intermediate results and data required to run the project
We provide analysis results for 3 regions: Paris, Paris with Petite Couronne, Petite Couronne, and the datasets required to run the project. They can be found [here](https://drive.google.com/drive/u/1/folders/1TutJX84GgBQe1-8TYyga9kIER5iEqLLb). 

## Organisation of the repo
1. helpers - contains helper functions for data extractions, calculating the 2SFCA scores and visualisations. Supplied by the BATO-MOUCHE project, extended and modified for better performance by us.
2. relics - a folder with some files which we end up not using. Contains an implementation of travel time calculations using the GraphiQL API for our locally hosted OpenTripPlanner server. In the end we didn't use it as r5py performs better for large quantities of data, but the OTP might be interesting for planning single journeys.
3. transportation - contains all the important jupyter notebooks:
    1. 2SFCA_general_analysis.ipynb - notebook with guide on how to compute 2SFCA scores for an area
    2.  Clustering.ipynb - Clustering which we did on the pcparis.gpkg dataset
    3.  Regression.ipynb - Regression which we did on the pcparis.gpkg dataset
    4.  SpatialRegression.ipynb - recreation of spatial regression done by the BATO MOUCHE team.
4. requirements.txt - used for installing libraries necessary to run this project.
       
The above files work for other geopackages as well. Moreover, the notebooks on data extraction for Paris, Paris with Petite Couronne and Petite Couronne are in this notebook.

## Setting up the repository
In order to run the notebooks, create a 'data' folder and put the required datasets there. Data required to run the analyses is specified within the *2SFCA_General_Analysis* notebook. 

## Required installs

The file requirements.txt contains the libraries necessary to run this project. We recommend setting up a python virtual environment for the project, and within it running:
```bash
pip install -r requirements.txt
```
To ensure that the *r5.py* library is correctly installed, additionally follow the steps listed [here][https://r5py.readthedocs.io/en/stable/user-guide/installation/installation.html]

## More Information

For more details on resources and dataset description. Please check this [README.md](https://github.com/LeoMaurice/BATO-MOUCHE-Stat-App/blob/main/README.md) file.

## References:
- **Moreno, Carlos** (2016). *La ville du quart d'heure: pour un nouveau chrono-urbanisme*. La Tribune, 5, May.
- **Birkenfeld, C.**, **Victoriano-Habit, R.**, **Alousi-Jones, M.**, **Soliz, A.**, and **El-Geneidy, A.** (2023). *Who is living a local lifestyle? Towards a better understanding of the 15-minute-city and 30-minute-city concepts from a behavioural perspective in Montréal, Canada*. Journal of Urban Mobility, 3, 100048. [DOI: 10.1016/j.urbmob.2023.100048](https://doi.org/10.1016/j.urbmob.2023.100048)
- **Thaury, M.-O.**, **Genet, S.**, **Maurice, L.**, **Tubaro, P.**, and **Berkemer, S. J.** (2024). *City composition and accessibility statistics in and around Paris*. Frontiers in Big Data, 7, 1354007. [DOI: 10.3389/fdata.2024.1354007](https://doi.org/10.3389/fdata.2024.1354007)
- **Cai, Yubo** (2024). *BATO-MOUTCHE-Extension*. [GitHub Repository](https://github.com/yubocai-poly/BATO-MOUTCHE-Extension). Accessed: 2024-11-30.
- **Haklay, M.** and **Weber, P.** (2008). *OpenStreetMap: User-Generated Street Maps*. IEEE Pervasive Computing, 7(4), 12-18. [DOI: 10.1109/MPRV.2008.80](https://doi.org/10.1109/MPRV.2008.80)
- **General Transit Feed Specification (GTFS) Reference** (2024). [Google Developers](https://developers.google.com/transit/gtfs/reference/#general_transit_feed_specification_reference). Accessed: 2024-11-30.
- **Luo, W.** and **Wang, F.** (2003). *Measures of spatial accessibility to health care in a GIS environment: synthesis and a case study in the Chicago Region*. Environment and Planning B: Planning and Design, 30, 865-884. [DOI: 10.1068/b29120](https://doi.org/10.1068/b29120)
- **Benhlima, O.**, **Riane, F.**, **Puchinger, J.**, and **Bahi, H.** (2024). *Development of a Variable Multimodal Balanced Floating Catchment Area Approach for Spatial Accessibility Assessment*. Geographical Analysis. [DOI: 10.1111/gean.12398](https://doi.org/10.1111/gean.12398)
- **OpenTripPlanner** (2024). [OpenTripPlanner](https://www.opentripplanner.org/). Accessed: 2024-11-30.
- **Conway, M. W.**, **Byrd, A.**, and **van Eggermond, M.** (2018). *Accounting for uncertainty and variation in accessibility metrics for public transport sketch planning*. Journal of Transport and Land Use, 11(1). [DOI: 10.5198/jtlu.2018.1074](https://doi.org/10.5198/jtlu.2018.1074)
- **Conway, M. W.** and **Stewart, A. F.** (2019). *Getting Charlie off the MTA: a multiobjective optimization method to account for cost constraints in public transit accessibility metrics*. International Journal of Geographical Information Science, 33(9), 1759-1787. [DOI: 10.1080/13658816.2019.1605075](https://doi.org/10.1080/13658816.2019.1605075)
- **Conway, M. W.**, **Byrd, A.**, and **van der Linden, M.** (2017). *Evidence-based transit and land use sketch planning using interactive accessibility methods on combined schedule and headway-based networks*. Transportation Research Record, 2653, 45-53. [DOI: 10.3141/2653-06](https://doi.org/10.3141/2653-06)
- **Fink, C.**, **Klumpenhouwer, W.**, **Saraiva, M.**, **Pereira, R.**, and **Tenkanen, H.** (2022). *r5py: Rapid Realistic Routing with R5 in Python (0.0.4)*. Zenodo. [DOI: 10.5281/zenodo.7060438](https://doi.org/10.5281/zenodo.7060438)
- **Knap, E.**, **Ulak, M. B.**, **Geurs, K. T.**, **Mulders, A.**, and **van der Drift, S.** (2023). *A composite X-minute city cycling accessibility metric and its role in assessing spatial and socioeconomic inequalities—a case study in Utrecht, the Netherlands*. Journal of Urban Mobility, 3, 100043. [DOI: 10.1016/j.urbmob.2022.100043](https://doi.org/10.1016/j.urbmob.2022.100043)
- **Ozili, Peterson** (2022). *The Acceptable R-Square in Empirical Modelling for Social Science Research*. SSRN Electronic Journal. [DOI: 10.2139/ssrn.4128165](https://doi.org/10.2139/ssrn.4128165)

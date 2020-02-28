# Datathon 2

**Objective** : "study loss and predict which teachers will abandon. Loss is defined as the fact a school that decided to adopt a specific material from *Ediciones SM* during 2018 school year, cancel it in 2019." *(predict churn for 2019)*

## Structure of File

- **Modeling** : repository for all notebooks used for modeling product churn.
- **Analysis** : repository for all images, graphs and notebooks used to explore the data.
- **Instructions** : repository with unaltered documentation provided by the professor.
- **Data** : repository for all data provided and generated from notebooks.

## Notes

> Keep in mind we are Company: 1 in the Survey sheets.
> Marketing_materials: numbers in marketing actions correspond to a score on how effective a action was. Makreting_actions
> **Representative does not equal seller_id**
> Data is real so aditional information can be used, such as grades by region or province.

## KPIs For Analysis

- [ ] client_load = client x seller_ID
- [ ] seller_load = seller_ID / client
- [ ] actions_per_client = marketing_actions / client
- [ ] sku_intreast = subject * course per client
- [ ] copies_x_client = # copies per action by client
- [ ] effort_x_customer = average_actions per customers per year
- [ ] action_effectivness = # copies / actions per year
- [ ] effectiveness_of_seller = # copies per seller by client
- [ ] percent_market_share = # copies of client over total # copies
- [ ] ABC client classification
- [ ] churn_x_client = calculate churn rate by year per client (16, 17, 18)
- [ ] churn_x_seller = calculate churn rate by year per seller (16, 17, 18)
- [ ] churn_x_SKU = calculate churn rate by year per SKU (16, 17, 18)
- [ ] new customer per year
- [ ] new customer per year per seller
- [ ] distinct materials per publisher
- [ ] distinct materials per seller
- [ ] distinct materials per client
- [ ] sales ratio per seller by year = #copies / distinct(customer_heading) per year

# Predicting Carbon Emissions of Cloud Computing

The goal of this project is to predict the carbon emissions of GitHub cloud computing. You can our documentation on our code and methodology in our [Wiki](../../wiki/).

---

Authors: [Théo Bacqueyrisse](https://github.com/TheoBacqueyrisse) and [Benjamin Rocheteau](https://github.com/ben-rocheteau)

This project is for the [Data Mining](https://www.tse-fr.eu/sites/default/files/TSE/ecole/doc/syllabi/2023-2024/m2_s1_datamining_gil-casals_halford_2023-2024.pdf) course of the [TSE D3S M2](https://www.tse-fr.eu/master-data-science-social-sciences?lang=en). 

---

## Table of Contents

1. [Our Project](#our-project)
2. [Using our Code](#using-our-code)
3. [Repository Layout](#repository-layout)

## Our Project

The goal of our project is to bring light onto the hidden cost of cloud computing: the carbon emissions generated by the servers hosting the service. Since we don't own or see the servers which run the calculations when we use cloud computing services, the costs of running those servers, beyond the fee paid to the company providing the cloud computing service, tend to be largely forgotten. 

To this end, we decided to focus on one kind of cloud computing in particular: [GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#overview). The data is easily accessible via the [GitHub REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28), and to generate our carbon emissions, we utilise Climatiq's carbon emissions model, easily accessible via their [API](https://www.climatiq.io/docs). 

Our code is in two parts: the first part gets the data on GitHub Actions, and uses the Climatiq API to generate predictions, and the second is a Streamlit App to let people see our results. 

## Using our Code

In order to use the first part of our code, you need the following things: 

- A GitHub Personal Access Token
- A Climatiq API token

  And in terms of the functions themselves, you can find documentation for the functions and how they are meant to be used in our [Wiki](../../wiki/).

  As to the second part of our code, you just need to run the code in `Streamlit_App.ipynb` to launch the app. 

## Repository Layout



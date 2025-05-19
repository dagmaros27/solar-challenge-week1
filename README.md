# MoonLight Energy Solutions: Solar Challenge Week 1

Welcome to the Solar Challenge Week 1 project for MoonLight Energy Solutions! This repository contains the data and analysis for identifying high-potential regions for solar installation, supporting the company's mission to enhance operational efficiency and sustainability through data-driven solar investments.

## Project Overview

As an Analytics Engineer at MoonLight Energy Solutions, your objective is to analyze environmental measurement data provided by the engineering team. The goal is to uncover key trends and insights that will inform strategic recommendations for solar deployment, aligning with the company's long-term sustainability goals.

## Objectives

- Perform exploratory data analysis (EDA) and statistical analysis on solar and environmental data.
- Identify regions with the highest potential for solar installation.
- Provide actionable recommendations to support MoonLight Energy Solutions' sustainability strategy.

## Dataset Description

The dataset is aggregated from Solar Radiation Measurement Data and includes the following features:

| Column        | Description                                                                            |
| ------------- | -------------------------------------------------------------------------------------- |
| Timestamp     | Date and time of each observation (yyyy-mm-dd hh:mm)                                   |
| GHI (W/m²)    | Global Horizontal Irradiance: total solar radiation on a horizontal surface            |
| DNI (W/m²)    | Direct Normal Irradiance: solar radiation on a surface perpendicular to the sun's rays |
| DHI (W/m²)    | Diffuse Horizontal Irradiance: indirect solar radiation on a horizontal surface        |
| ModA (W/m²)   | Sensor/module A irradiance measurement                                                 |
| ModB (W/m²)   | Sensor/module B irradiance measurement                                                 |
| Tamb (°C)     | Ambient temperature in degrees Celsius                                                 |
| RH (%)        | Relative humidity (%)                                                                  |
| WS (m/s)      | Wind speed (meters per second)                                                         |
| WSgust (m/s)  | Maximum wind gust speed (meters per second)                                            |
| WSstdev (m/s) | Standard deviation of wind speed                                                       |
| WD (°N to E)  | Wind direction in degrees from north                                                   |
| WDstdev       | Standard deviation of wind direction                                                   |
| BP (hPa)      | Barometric pressure (hectopascals)                                                     |
| Cleaning      | Cleaning event indicator (1 = cleaned, 0 = not cleaned)                                |
| Precipitation | Precipitation rate (mm/min)                                                            |
| TModA (°C)    | Temperature of Module A (°C)                                                           |
| TModB (°C)    | Temperature of Module B (°C)                                                           |
| Comments      | Additional notes                                                                       |

## Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd solar-challenge-week1
   ```

# Project Description

The purpose of the project is to analyze Airbnb data related to listings in Los Angeles city and answer three business questions. The questions are:
* Can I predict the price of a home/room that aren’t yet in the market?
* What are the most important factors in determining the price?
* Which days are the busiest?

## Libraries
The following Libraries were used in this project:
* numpy
* pandas
* matplotlib
* sklearn

## Project Motivation
For this project, I was interestested in using Los Angeles Airbnb data to better understand and answer the follwoing questions:
* Can I predict the price of a home/room that aren’t yet in the market?
* What are the most important factors in determining the price?
* Which days are the busiest?

The reason for choosing data about Los Angeles because I used to live there and I wanted to see if things have changed since then.

## Folders and Files
The folder 'data' contains the two compressed files, due to size limitation:
* calendar 2.csv.zip: which contains the listings with dates of availability
* listings 2.csv.zip: which contains the listings with features

The folder 'source' contains jupyter notebook and the html version of the notebook.

## Results
The heighest R2 score for price prediction is ~0.736. To predict the price, the number of bedrooms and the security deposit are the two most inportant factor in determining the price. Finally, the analysis conclude that the second and third weeks of May are the busiest during one year span.

Please check my blog post for more details
[How do you choose your AirBnb in Los Angeles?](https://medium.com/@abdullah_ib/applying-machine-learning-on-los-angeles-airbnb-data-43694c5480d0)


## License
The datasets used in this analysis were acquired from Inside Airbnb database under a Creative Commons CC0 1.0 Universal (CC0 1.0) "Public Domain Dedication" license.
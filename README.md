## Supporting Montreal's local businesses and restaurants after the pandemic, and helping customers and citizens explore new experiences.

## Inspiration
We were inspired to create Montreat after witnessing many of our favorite local businesses shutting down as a result of the pandemic, and were wanting to promote small businesses and help them recover from a difficulty few years. Our goal was to promote local restaurants and stores over large chains and corporations, as well as providing more transparency for users to search through businesses.

## What it does
Montreat is a website that allows users to search for restaurants and businesses, with a focus on small, local, family-owned businesses. It limits the appearance of larger fast-food corporations and chains. The site also provides users with an extensive set of filters to find the perfect business for their needs. We also implemented a chatbot which, given a user's query, returns a list of businesses accordingly.

## How we built it
We constructed the website using React and various plugins, which required many of our teammates to learn React and other technologies entirely from scratch. 
The chatbot was built with the Twinword API and Google Maps API. The Twinword API takes in a user input and returns a set of keywords, including cuisines, proximity, etc. Given these keywords, the Google Maps API filters through businesses local to Montreal and returns the results. The chatbot currently has support for restaurants, grocery stores, butchers, cafes, delis, and pharmacies.

## Challenges we ran into
We experienced great difficulty incorporating the back-end and front-end together for the website, as it involved extensive knowledge of both technologies, which our teammates didn't have. We also had difficulty having the interactive map display results, for some time. Some issues with the chatbot that we faced were with limited data and the API. Neither the Google Maps API or a government dataset of businesses in Montreal had any information on cuisines of restaurants, so the filtering for that component is far from perfect, and is based on keywords in the name of the restaurant itself, or in the notes for it. Furthermore, we experienced some difficulties with the Twinword API failing to stay connected, requiring us to reset the runtime for the code many times.

## Accomplishments that we're proud of
We were very proud that we were able to integrate our front and back-end, as we did not have experience working with both together. We were also very proud of the layout of the website and the features available, as well as the functionality of the chatbot.

## What we learned
We all learned how to use a wide variety of tools that we had minimal to no experience with. Our teammates working on front-end learned how to use React from scratch, as well as working with R and JavaScript, which we had limited experience in. Our back-end teammates learned how to use APIs for the first time, as well as learning how to incorporate the front-end and back-end.

## What's next for Montreat
Montreat has a promising future ahead, with hopes to further improve the chatbot functionality, incorporate more search features and tools for users, as well as an idea to add soup kitchens and food trucks and other under-represented businesses in our map. We believe that local businesses that aren't given a platform on sites like Google Maps should be promoted in our project.

Note: ChatGPT was used for some aspects of the code-writing for this project.

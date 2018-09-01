# Comparing News Sources and their Fingerprints

Is there a way to quantify how biased or wide-coverage a news source is? Nowadays, with concerns about "fake news" and untrustworthy media, people use their intuitions and political beliefs to decide what is fake and what isn't. In this project, I attempt to find objective patterns between different categories of news sources and between individual news sources themselves.

##Rmd Sections:
In the Rmd file, I first scrape headlines from multiple news sources and find common keywords among those headlines. By finding the frequency of each of these common words for each news source, we can aggregate a "fingerprint" for each source at the time the headlines were collected. We can then utilize these fingerprints to build neural nets which predict sources, party bias, and more based on new fingerprints.

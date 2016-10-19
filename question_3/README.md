# What is this directory for?
This directory contains a possible implementation of double blind testing on possible search engines.

# Issues
Search engines do not like web scraping, so most modern day search engines do not allow web servers to ping their servers and scrape the content
that easily even when using a user agent of sorts.

To avoid scraping, search engines may change tag IDs.

# Purpose
The point of the double blind testing is to unbiasedly allow users to pick which results were preferrable. This application takes the link and the description
from the search engines and outputs the results in an unordered list. From there, users can pick which results they prefer.

However, there are some issues that arise, in which the output shown does not always show the search engine description. Grabbing the correct tag can be quite difficult
as search engines may try to change IDs and structures to avoid web scraping; otherwise the IP can get blocked.

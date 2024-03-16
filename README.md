Explanation of COMPOSITE_Text_Scrape_CLEANED.xlsx file:

0) using automated code found in this repository 383 pairs of URLS where privacy statements were identified where a website
   had both non-CCPA privacy statement language and CCPA privacy statement language
1) a Beautiful Soup scraping program was written but was found to not scrape data in a clean enough format to be used
2) each pair was reviewed manually and the privacy statement language inserted into this .xlsx file
   a) NOTE that .csv and .xlsx files only allows 32,767 characters and some of the privacy statements where longer then this
   b) in this case the text of the privacy statement was continued in the the cell below of the same Column D
4) this is an .xlsx file instead of a .csv file because a .csv file will not save the color-coding.
5) The color coding means the following:
   a) GREEN = a pair of privacy statements where the CCPA statement is completely separate from the non-CCPA statement
   b) YELLOW= a pair of privacy statements where the CCPA is either:
      i) embedded in the main privacy state (usually as a numbered paragraph) but has been separated out; or
      ii) a separate CCPA statement was labled as being a SUPPLEMENT to the main privacy statement meaning they are to be read together
   c) RED = either the page would not load at all or it loaded and there was no content. If only one of the pair is red then the other has no color
   d) ORANGE = the main privacy statement and the CCPA privacy statement are identical
6) the idea with the color coding is we may want to only use the pairs where the non-CCPA and CCPA privacy statements are completely separate.
   a) When Column D is filterd for GREEN only the result is 460 non-blank lines indicating there are 230 pairs where the statements are separate
   b) When Column D is filterd for YELLOW the result is 294 non-blank lines indicating there are 147 pairs wher the statements are blended

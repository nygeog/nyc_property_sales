# NYC Property Sales data BBL for Condos, Base and Billing

**BBL** - Borough, Block and Lot, basically a Tax Parcel ID for New York City. 

While working on a data challenge (more details on that to follow) using [New York City (NYC Annualized Sales data] (https://www1.nyc.gov/site/finance/taxes/property-annualized-sales-update.page), I ran into a **BBL** complexity that I feel like hasn't been fully hashed out in the **NYC Open Data** Community. [Please let me know](mailto:daniel.martin.sheehan@gmail.com) if there are other resources about this topic or if I'm missing something. 

*Disclaimer: this was done during a data challenge for which getting a lot of tasks done in a short amount of time was the primary focus. I think fully understanding data, its value, limitations (known unknowns/considering unkown unkowns) and the story of the outliers, is more important than coding it up quickly or getting results quickly. I was not paid for this challenge, but I also may not be entirely free to release all of the details of this whole exercise (again, more on that to follow).* 

The gist of a small yet important part of this data challenge was that the NYC Annualized Sales data (NYC Sales) needed to be matched to [Pluto data (thus also including MapPluto)](http://www1.nyc.gov/site/planning/data-maps/open-data/pluto-mappluto-archive.page) (NYC *"land use and geographic data at the tax lot level"*). However, as we'll see below, that match can only fully be done using a 3rd data source. 

## 1. Getting the NYC Annualized Sales data 2003-2014

[Click here for a Python file to download xls files, read to dataframes and merge](https://github.com/nygeog/nyc_property_sales/blob/master/code/01-get-sales-data-and-merge.py). This will download both Rolling and Annualized Sales. We'll only look at the Annualized Sales but I have the Rolling Sales download code in there as well. You'll need the following Python libraries installed:

* urllib
* datetime
* pandas
* glob
* os
* xlrd (--upgrade this, as earlier versions ran into trouble with reading some apartment numbers as dates)

## 2. Matching on BBL

Now, I realize that tax lots in NYC change, and more proper metholodogy would include matching the NYC Sales data to the proper year of Pluto/MapPluto release, but in order to more easily demonstrate this BBL issue and relationship, I will use only one cut of Pluto/MapPluto data. 

	Show code excerpt or link to code

There are quite a bit of records that did not match. Now, some of those in the world of **'big data'** may view mismatches as noise or outliers, in this instance, this mismatch is a crucial subset of the data. Significantly, this mismatch subset represents Condo sales in NYC, hardly an outlier in NYC real estate sales. 

It's at this point that the reader should check out this [excerpt from Colin Reilly's: NYC Building Footprints Part II](https://nycitymap.wordpress.com/2014/12/23/nyc-building-footprints-part-ii/) where he discusses the **differences between the Billing BBL and the Base BBL**. 

>For all tax lots, except condominiums (condos), there is a single representative BBL across all City agencies. Condos are the exception due to the fact that each individual unit (i.e., apartment) within a condo building has its own BBL. Therefore, condos have multiple BBLs per tax lot. It is my understanding that the Billing BBL was created by The Department of Finance (DOF) as a way of representing a condo’s management entity for the purpose of correspondence and record keeping. **Billing BBL**s always have 75 as the first two digits in the block portion of the BBL (e.g., 7501.). Unfortunately there does not seem to be agreement across all City agencies, or even within an agency, on a unique BBL for condo lots.
	
>DOF uses the **Billing BBL** for RPAD and the **Base BBL** (also referred to as the FKA [Formerly Known As]) for the Digital Tax Map and ACRIS. DCP uses the billing BBL for MapPluto.
	
>The building footprints use the Billing BBL. The building footprints carry the BBL as a means of providing a way of associating buildings to tax lots. Since the BBLs are managed outside of the building footprints, the BBLs are synchronized periodically. Due to the different update frequency of MapPluto and the building footprints, inconsistencies can be present. In the December 2014 extract there were 5,199 BBL mismatches representing 0.4% of the total.
	
>There are also cases where buildings do not fall within an official tax lot. For these, DCP assigns a ‘dummy’ lot number of 9999. An example is the Subway station at 96th and Broadway (BIN 1089286, BBL 10124399990). These ‘dummy’ lots are in PAD but do not exist in MapPluto.

Colin's blogpost was hugely helpful. Also helpful in first being exposed to this Condo BBL problem was a meetup about ACRIS data from a few years back [Betatalk w/ NYU Furman Center - Meet NYC's ACRIS](http://www.meetup.com/betanyc/events/147317952/) and some conversations since then with folks very familiar with MapPluto. 

## 3. Exploring NYC Digital Tax Map (DTM)

	maybe through in a CartoDB map of the files. 
	is there an iframe tool for embedding
	attribute tables? 

As we start to get into the DTM, we notice that there are BBL's for .... explain the different data tables.


## Assumptions and Limitations

One assumption I have is Condo BBL's are unique to a Condo Unit. I'm unsure if a building of Condo's is completely torn down and rebuilt if those unit's are assigned new BBL's or if they carry over the older BBL's. 


Now, since all of this was done for a project that I'm not salaried for/nor a paper I'm a co-author on, so I'm not really willing to vouch for all of this completely and definitively. But I do hope this is useful to those out there looking to get their hands dirty with NYC Sales data and do good work with this data. 

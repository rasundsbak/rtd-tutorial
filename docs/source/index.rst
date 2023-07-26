01 Welcome to the pilot course on how to use ComtradR
======================================
This project has its documentation hosted on Read the Docs: https://readthedocs.org/
This project has a GitHub repository: https://github.com/rasundsbak/rtd-tutorial/tree/3.0.y

Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. note::

   This project is under active development.
---

.. note::

   This project has no references yet. References will be added at a later stage. Thanks to ropensci/comtradr for making the package available again at `github <https://github.com/ropensci/comtradr/tree/main>`.

---

01 Introduction
===============
This is a report after following a bachelor course of STV 2020 Spring term 2023, University of Oslo. This text may be used as a tutorial for using Comtrade. In the following, it will be outlined how data from the United Nations' Comtrade database [@CRANPackageComtradr] can be used to point out structural problems related to oil industry. This will be the academic example used to demonstrate both the process of data collection, as well as the processing and division of data into relevant units. While working on this project, the United Nations API delivery was modernized and changed from being facilitated for R and RStudio into Python. The ComtradR is still being maintained under the GitHib initiative of OpenSci[@muir2023; @ROpenSciOpenTools]. This project will be developed according to the progress of the technical development of the official Comtrade database. A repository on how to generate data with Python, for import to RStudio may come at a later time.

02 The research question
========================
OPEC countries, their oil export and democracy development. The statistics shown will be from the OPEC countries. Data on Trade value in Crude oil will be collected from Comtrade legacy database [@muir2023]. "Trade value" was chosen because it is the variable in this category that includes the most data. If choosing another category, the number of missing values would be larger. The development of the values of Trade value will be shown from the period 1995-2004. Then then the results of the Opec countries on a corruption index from the World Bank governance Indicators will be introduced [@kaufmann2023]. Finally, a regression analysis with corruption level as the dependent variable will be shown. The unit of analysis will be land- years. The process of restructuring the data will be shown.

03 The academic problem
=======================
We are going to look at data from the two institutions of Comtrade and World bank.

**Q1 How does the distribution of Export of Crude oil from the OPEC countries look like for the years from 1995 until today?**

**Q2 How does the available corruption index of the OPEC countries look like?**

**Q3 Is there a tendency for the OPEC countries that higher income from oil export leads to higher levels of corruption?**

In order to answer these questions, data will be taken from two sources. Firstly, numbers on trade is taken from the Comtrade database. Secondly, indicators on democracy and corruption levels are taken from the Worldwide Governance Indicators.

This project should be seen as a pedagogical example on how to extract and analyze data for political and social science, rather than real social science. The main focus here is on the technical processes, rather than the scientific value of the findings.


A good way to start up an R script
==================================

If you do not know your directory, use the command "getwd". Then, copy the directory from the answer you got, and adjust it to fit the path that suits you. In the .R file, at the very begining::

   getwd
   setwd("/Users/ragnhildsundsbak/Documents/LearningR2023/ComtradeProjectNew")

I always start with the setwd. It is a good idea to combine it with opening the library(here). Many people prefer to use projects in RStudio. The reason why I no not, is that i feel the setwd command and "here" package gives me both better knowledge and control over my system.

In order to follow the process in this script, we need the following pagkages. Note that if you do not have them installed, you must first use the command install.packages("package name"). Since this is to be done only once, I often use the # tag to make the coding turn into a comment that will not be executed.

Installation example::

   install.packages("comtradr")
   install.packages("rjson")

   after installation, change to:
   #install.packages("comtradr")
   #install.packages("rjson")

Then::

   library(here)
   library(comtradr)
   library(rjson)
   library(ggplot2)
   library(dplyr)
   library(plotly)
   library(conflicted)
   library(janitor)
   library(tidyverse)
   library(scales)


It is also necesary to rule out the conflicts between the packages that are in use::

   conflict_scout()

   conflicts_prefer(stats::fisher.test) 
   conflicts_prefer(dplyr::filter)
   conflicts_prefer(plotly::layout)
   conflicts_prefer(dplyr::lag)
   conflicts_prefer(fi::stats) 
   conflicts_prefer(stats::chisq.test) 
   conflicts_prefer(scales::col_factor)
   conflicts_prefer(scales::discard)

We are ready to start the process of getting data.

The function defined in this example, get.Comtrade(), extracts data from 
UN Comtrade using either the csv or the json format::

   get.Comtrade <- function(url="http://comtrade.un.org/api/get?"
                         ,maxrec=50000
                         ,type="C"
                         ,freq="A"
                         ,px="HS"
                         ,ps="now"
                         ,r
                         ,p
                         ,rg="all"
                         ,cc="TOTAL"
                         ,fmt="json")
   {string<- paste(url
                 ,"max=",maxrec,"&" #maximum no. of records returned
                 ,"type=",type,"&" #type of trade (c=commodities)
                 ,"freq=",freq,"&" #frequency
                 ,"px=",px,"&" #classification
                 ,"ps=",ps,"&" #time period
                 ,"r=",r,"&" #reporting area
                 ,"p=",p,"&" #partner country
                 ,"rg=",rg,"&" #trade flow
                 ,"cc=",cc,"&" #classification code
                 ,"fmt=",fmt        #Format
                 ,sep = "")
   if(fmt == "csv") {
       raw.data<- read.csv(string,header=TRUE)
       return(list(validation=NULL, data=raw.data))
   } else {
    if(fmt == "json" ) {
      raw.data<- fromJSON(file=string)
      data<- raw.data$dataset
      validation<- unlist(raw.data$validation, recursive=TRUE)
      ndata<- NULL
      if(length(data)> 0) {
        var.names<- names(data[[1]])
        data<- as.data.frame(t( sapply(data,rbind)))
        ndata<- NULL
        for(i in 1:ncol(data)){
          data[sapply(data[,i],is.null),i]<- NA
          ndata<- cbind(ndata, unlist(data[,i]))
   }
        ndata<- as.data.frame(ndata)
        colnames(ndata)<- var.names}
      return(list(validation=validation,data =ndata))
         }
      }
   }

Then I am making a chunk where I define specifically what I want from the Comtrade database. I run the ct_commodity_lookup. The response from RStudio console will show what is the content of the data we are going to look at::

   ct_commodity_lookup("2709")
   $`2709`
   [1] "2709 - Petroleum oils and oils obtained from bituminous minerals; crude"        
   [2] "270900 - Oils; petroleum oils and oils obtained from bituminous minerals, crude"

The answer gives us the numerical code that we need for out next chunk::

   ```{r, 07-data-retrieval, echo=FALSE}
   RS1 <- get.Comtrade(ps= "1995,1996,1997,1998,1999", 
                    c="2709", 
                    r="12,24,178,226,266,364,368,414,434,566,682,784,862",
                    p="0",
                    rg="2")

   RS2 <- get.Comtrade(ps= "2000,2001,2002,2003,2004",
                    c="2709",
                    r="12,24,178,226,266,364,368,414,434,566,682,784,862",
                    p="0",
                    rg="2")
   ```

The result is two tibbles, that must be bound together. The reason why we do this twice, is that Comtrade only wants to give five years of data each time. I have not tried to take more than five years, but suspect that it might result in NULL output in the data file.

Storing the data is useful, in case the database has down time. It also allows you to gradially make your iwn little databank for reuse in your project.

Example of a process like this::

   # store the data in case the database is down in future

   ```{r, 10-storing-data-locally, echo=FALSE}
   write.csv(RS1$data, "/Users/ragnhildsundsbak/Documents/LearningR2023/ComtradeProjectNew/95_99Opec.csv")

   write.csv(RS1$validation, "/Users/ragnhildsundsbak/Documents/LearningR2023/ComtradeProjectNew/Validation95_99Opec.csv")

   write.csv(RS2$data, "/Users/ragnhildsundsbak/Documents/LearningR2023/ComtradeProjectNew/00_04Opec.csv")

   write.csv(RS2$validation, "/Users/ragnhildsundsbak/Documents/LearningR2023/ComtradeProjectNew/Validation00_04Opec.csv")
   ```
furthermore::

   #Take out the data to work further
   RS1 <- as_tibble(RS1$data)
   RS2 <- as_tibble(RS2$data)


   #Check it out
   View(RS1)
   View(RS2)
   ```

The process starts getting interesting::

   ```{r, 12-binding-rows, echo=FALSE}
   RS3 <- bind_rows(RS1, RS2)

   View(RS3)
   ```

And then::

   ```{r, 13-preparing-visualization, echo=FALSE}

   Year <- c(RS3$yr)
   Value <- c(RS3$TradeValue)
   Land <- c(RS3$rtTitle)
   ```
text::

   ```{r, 14-convert-to-numeric, echo=FALSE}
   # Denne er essensiell for aa lykkes med grafikk
   Year <- as.numeric(as.character(RS3$yr)) # Convert factor to numeric Year

   Value <- as.numeric(as.character(RS3$TradeValue)) # Convert factor to numeric Vekt
   
   class(RS3$rtTitle)
   ```

and...::

   ```{r, 15-ggplot-visualization, echo=FALSE}
   # This seems to work:
   FirstVisualisation <- ggplot(RS3, aes(x=Year , y = (log(Value)), group = Land, colour = Land)) + 
   geom_line(size=1)

   FirstVisualisation <- FirstVisualisation +
     geom_point(size=2)

   FirstVisualisation
   ```
Resulting in this table:

   .. image:: rplot.png


03.01 Not the most sophisticated plot, but we have to move on
-------------------------------------------------------------
Many things can be said about the formatting of this image, and some of them mught even be unfavourable. However, there are other sites on the web that may learn you how to make beautiful and very sophisticated outputs with RStudio. In this lesson, we are going to focus on breaking down data into a meaninhful regression analysis.

03.02 Etiam tincidunt
---------------------

"Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
"There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain..."

This is an ordinary paragraph, introducing a block quote.

    "It is my business to know things.  That is my trade."

    -- Sherlock Holmes



04 Lorem ipsum dolor sit amet
=============================
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut eleifend augue, et pretium turpis. Fusce in tortor a tellus luctus tristique a at metus. Pellentesque in suscipit ipsum. Ut bibendum elit orci, eget efficitur mauris fringilla eget. Aliquam vitae risus lectus. Nam quis ante magna. Nunc hendrerit tellus at tortor dapibus, ut porttitor enim tincidunt. Etiam nisl purus, fermentum sit amet justo ac, lobortis congue ipsum. Cras nisl nisi, vehicula ac suscipit vitae, consectetur at ligula. Morbi faucibus dignissim dictum. Phasellus bibendum iaculis tellus, sed vehicula est luctus imperdiet. Pellentesque dictum enim est, at condimentum mauris iaculis et. Nulla posuere congue luctus. Aliquam nec sem pretium massa mollis ornare. Proin vel nulla eu dolor consequat fermentum nec et velit. Ut quis sapien non lacus pretium elementum.

01 Suspendisse consequat sagittis leo at accumsan
----------------------------------------------

02 Suspendisse consequat sagittis leo at accumsan
----------------------------------------------


05 Quisque at finibus orci
==========================
Quisque at finibus orci. Suspendisse sit amet magna rutrum nisl tincidunt eleifend. Nulla tempus turpis justo, aliquam viverra ex bibendum at. Praesent accumsan ligula in magna consequat consectetur. Morbi vestibulum tempor odio et commodo. Suspendisse potenti. Suspendisse congue vitae erat eget pellentesque. Donec imperdiet posuere dapibus. Etiam maximus sodales eros, lobortis vulputate mauris commodo ut. Maecenas iaculis sem a tempor tempus. Nulla diam nibh, lacinia non dolor ut, imperdiet aliquet augue. Aenean elit quam, mattis eu ligula a, dapibus sodales nunc. Vivamus a commodo magna, non imperdiet metus.

.. _Suspendisse consequat sagittis leo at accumsan:
Suspendisse consequat sagittis leo at accumsan
----------------------------------------------
- Suspendisse consequat sagittis leo at accumsan. 
- Donec dapibus euismod mi ac tempus. 

In.hac_habitasse() platea dictumst. 
Etiam varius nisi eu nunc fringilla ultricies. Ut sapien neque, sollicitudin sed eros id, ornare luctus mauris. Sed ac auctor lorem. Curabitur vitae justo est. Sed quis est at urna malesuada vestibulum sit amet vitae nisi. Vivamus fringilla, nisl quis maximus dignissim, felis justo pulvinar nisi, vitae scelerisque mauris nibh commodo nunc. Nunc eu est nisl. Duis luctus sed sapien eu feugiat. Suspendisse efficitur sagittis neque, non fringilla justo egestas ut. Phasellus posuere pretium est, ac sollicitudin diam egestas in.

.. _Etiam tincidunt:
Etiam tincidunt
---------------
- Etiam tincidunt: https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/#id1

ex ac viverra semper, diam eros laoreet felis, vel maximus purus nunc a augue. Cras ultricies elementum enim. Praesent sed pharetra ipsum. Nullam vel risus tellus. Sed finibus risus at condimentum laoreet. Sed volutpat convallis sapien, id pharetra ante. Quisque sagittis lobortis mattis.

.. _Suspendisse vulputate est vitae nunc porta:
Suspendisse vulputate est vitae nunc porta
------------------------------------------
Suspendisse vulputate est vitae nunc porta, in tempor sem convallis. Vivamus turpis turpis, imperdiet et viverra et, sodales nec ligula. Nullam ultrices diam sed nisl imperdiet sollicitudin. Quisque id nulla dapibus, tincidunt odio vitae, euismod erat. In in aliquet libero, sed pharetra nisi. Maecenas vel erat pretium, aliquet sapien vitae, ornare neque. Aliquam facilisis, diam vel porttitor tincidunt, tortor eros molestie arcu, nec vulputate enim justo eget nulla. Nam gravida interdum ligula id convallis. Aenean suscipit auctor blandit. Maecenas iaculis lectus in neque mattis, ut hendrerit nunc imperdiet. Sed sed sem sed turpis egestas fringilla. Quisque nec est quis lacus consectetur faucibus tempor vel ex. Integer lobortis augue ac orci vestibulum egestas non blandit diam. Nulla vel lacus nec ex tempus luctus nec eget tortor. 


Contents
--------

.. toctree::

   01 Welcome to Lumache's documentation!
   01 Introduction
   02 The research question
   03 The academic problem
   04  
   05 
   04 Quisque at finibus orci
      Suspendisse consequat sagittis leo at accumsan
      Etiam tincidunt
      Suspendisse vulputate est vitae nunc porta
      
   
   


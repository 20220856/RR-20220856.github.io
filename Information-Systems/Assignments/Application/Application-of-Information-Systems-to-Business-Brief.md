# IT5015 - Application of Information Systems to Business Brief - 20220856

---

# Part 1, Task 1: Development of Data Model for Eye Candy Cinemas

Using the conceptual design of the Report provided to Eye Candy Cinemas, a final Entity Relationship Diagram has been created. It includes all relevant data of each cinema complex, individual theatres, sound systems within, screening times of films, and data on the films themselves.

![20220856-ERD-2023-01-10_22-23](https://user-images.githubusercontent.com/110361869/211512270-5e8ade4f-5ce2-4703-a889-0cdf9936e055.png)



Additionally, a breakdown of the ERD, as well as individual elements can be found below for additional context as to how the ERD directly corresponds to Eye Candy Cinemas. These breakdowns include all Entities used in the ERD, the Attributes of individual Entities, a brief Description of Attributes, the Data Types of Attributes, the Primary Key of the Entity (as well as other Candidate Keys), and the Cardinality of each dataset to another.

---

## Cinema Table

|Entity|Attribute|Description|Data Type|PK/CK/FK|Cardinality|
|:---:|---|---|---|---|:---:|
|Cinema|Cinema_ID|A Numeric Identifier for the Cinema|INT|PK & CK|Theatre *(One-to-Many)*|
||Cinema_Name|The Name of the Cinema *(AKL or WLG)*|VARCHAR|CK||
||Cinema_Address_1|The first line of Address for the Cinema|VARCHAR|||
||Cinema_Address_2|The Suburb of the Cinema|VARCHAR|||
||Cinema_City|The City of the Cinema|VARCHAR|||
||Cinema_Email|The Email address of the Cinema|VARCHAR|||
||Cinema_Phone|The Phone Number of the Cinema|INT|||

For the Cinema Table, no referential constraints apply, as the contained information is entirely independant of other datasets.

---

## Theatre Table

|Entity|Attribute|Description|Data Type|PK/CK/FK|Cardinality|
|:---:|---|---|---|---|:---:|
|Theatre|Theatre_ID|A Numeric Identifier for a Theatre|INT|PK, CK and FK|Screening *(One-to-Many)*|
||Theatre_Seats|The capacity of all seats within the Theatre|INT|||
||Cinema_ID|The Cinema ID, denoting which cinema the theatre is located|INT|FK|Cinema *(Many-to-One)*|
||Sound_ID|The Sound System ID, denoting which system the theatre uses|INT|FK|Sound System *(Many-to-One)*|

For the Theatre Table, both the Cinema_ID and Sound_ID attributes are referential constraints - the information from both the Cinema Table and the SoundSystem Table are being referenced. This is because the theatre could not otherwise:
- Be located within a Cinema Complex.
- Have the Sound System in use be determined.

---

## Screening Table

|Entity|Attribute|Description|Data Type|PK/CK/FK|Cardinality|
|:---:|---|---|---|---|:---:|
|Screening|Screening_ID|The Numeric Identifier for a Screening|INT|PK & CK||
||Theatre_ID|The Theatre ID, denoting the theatre for the screening|INT|FK|Theatre *(Many-to-One)*|
||Film_ID|The Film ID, denoting the film for the screening|INT|FK|Film *(Many-to-One)*|
||Screening_DateTime|The Date and time of the screening|SMALLDATETIME|||
||Screening_Price|The Price for a ticket to the screening|DECIMAL|||

For the Screening Table, both the Theatre_ID and Film_ID attributes are referential constraints - information from the Theatre Table and Film Table are being referenced. This is important, otherwise:
- The Theatre within which the Screening was set to take place could not be determined.
- The Film that the Screening was intended to display could not be determined.

---

## Film Table

|Entity|Attribute|Description|Data Type|PK/CK/FK|Cardinality|
|:---:|---|---|---|---|:---:|
|Film|Film_ID|The Numeric Identifier for a Film|INT|PK, CK & FK|Screening *(One-to-Many)*|
||Film_Title|The Title of the film|VARCHAR|CK||
||Film_Director|The Director of the Film|VARCHAR|||
||Film_Duration|The complete runtime of the Film|INT|||
||Film_Year|The Year the film was released|INT|||
||Film_Classification|The Classification of the film|VARCHAR|||
||Film_IMDB|A link to the IMDB Rating/Review of the Film|VARCHAR|||

For the Film Table, there are no referential constraints. The information regarding a film is not dependant on any other Data - it is fixed.

---

## SoundSystem Table

|Entity|Attribute|Description|Data Type|PK/CK/FK|Cardinality|
|:---:|---|---|---|---|:---:|
|Sound System|Sound_ID|The Numeric Identifier for a Sound System|INT|PK, CK & FK|Theatre *(One-to-Many)*|
||Sound_Name|The Model Name of the Sound System|VARCHAR|||
||Sound_Manufacturer|The Manufacturer of the Sound System|VARCHAR|||

For the SoundSystem Table, there are no referential constraints. The Table is not dependant on any information in order to exist, and - in fact - only exists for referencing in the Theatre Table.

---

## Data Normalisation

In order to preserve the integrity of data, prevent data duplication, and aid in the effective categorisation of information, data must be normalised. In this instance, the data has been normalised to the **Third Normal Form (3NF)**. The fulfilled criteria are explained below.

### The Data is provably standardised to the **First Normal Form (1NF)** because;
- The data tables are scaleable, and can easily have more data inserted.
- Each data entry only contains ONE form of value.
- Values of the same TYPE are organised in columns.
- Each column has an entirely unique name.
- Data can otherwise be stored in any order, and doing so does not compromise the integrity of information.

### The Data is provably standardised to the **Second Normal Form (2NF)** because;
- It has shown to be correctly standardised to (1NF).
- There are no Partial Dependancies within the data.

A partial dependancy is when data within an entity consists of duplicated data. Using a practical example from the data for Eye Candy Cinemas, a partial dependancy could be the inclusion of "Sound_ID" **AND** "Sound_Name" in the Theatre Table. Due to the fact that "Sound_Name" is already accounted for by "Sound_ID", this would be data duplication, and thus a partial dependancy. Ensuring that there are no such occurrences ensures that the tables are in (2NF).

### The Data has been provably standardised to **Third Normal Form (3NF)** because;
- It has been shown to be correctly standardised to (1NF) and (2NF).
- There are no Transitive Dependancies within the data.

A transitive dependancy is when an attribute of a table is dependant on a **non-primary** attribute in order to exist. An example of this would be if the "Screening_DateTime" attribute was separated into "Screening_Date" and "Screening_Time". Although "Screening_Date" would NOT be a primary attribute, "Screening_Time" would be dependant on it in order to contextually make sense, therefore would be transitively dependant. Ensuring that this example, along with any others like it, are NOT transitively dependant ensures that the tables are standardised to (3NF).

---

## Task 2: Designing Data Queries for Eye Candy Cinemas

The purpose of this database is to interface with, and provide data to a Web application. Several necessary functions have been identified, and must have correspondant data queries in order to complete.

These are;
- The ability to search for a Cinema
- The ability to show information regarding a Cinema
- The ability to show a schedule of upcoming movies
- The ability to show detailed information of a specific screening

Additionally, Eye Candy Cinemas has requested a special, additional feature;
- The ability to monitor the number of screenings per day/week at each location and theatre.

In order to achieve these functions, a number of queries must be able to be run on the database to ensure that the data required can be attained. Below are tables for the five functions, and their corresponding queries.


|Function|Queries|Description|
|:---:|:---:|:---:|
|Search For Cinema|SearchCinemaByCity|Search for a Cinema within a City
||SearchTheatreBySeatingAndCity|Search for a Cinema within a City by the capacity of the Seating
||SearchTheatreBySoundSystemAndCity|Search for a Cinema within a City by its Sound System

|Function|Queries|Description|
|:---:|:---:|:---:|
|Show Cinema Information|ShowCinemaAddresses|Show the First and Second lines of Address, and the City
||ShowCinemaTheatres|Display the Number of Theatres within a Cinema
||ShowTheatreIDAndSeats|Displays the Seating Capacity of each of the Theatres within a Cinema
||ShowTheatreIDAndSoundSystem|Displays the Sound System of each Theatre within a Cinema

|Function|Queries|Description|
|:---:|:---:|:---:|
|Search Film Schedule|SearchFilmByTitle|Search for Film session details by the title of the Film
||SearchFilmByCinema|Shows all films screening at a Cinema Complex
||SearchFilmByDay|Show all film screenings on a given Weekday
||SearchFilmByTicketPrice|Search all films with a specified ticket price

|Function|Queries|Description|
|:---:|:---:|:---:|
|Show Film Screenings|SearchScreeningByTheatre|Show all screenings within a specified Theatre
||SearchScreeningByDateTime|Show all screenings within a specified Date and Time
||ShowScreeningInfo|Display Film Director, Year of Release, Classification, and IMDB Link

|Function|Queries|Description|
|:---:|:---:|:---:|
|Monitor Movie Screenings|ListCinemaScreenings| List all screening sessions for a Cinema within a specified timeframe
||ListTheatreScreenings|List all screening sessions for an individual Theatre within a specified timeframe
||AverageSessionsPerWeek|Provide an Average of the total screenings per day over a week.

## Review of Database Design

In order to accomodate these search queries, two changes had to be made to the database in order to ensure the function of these detailed requirements;
- To the Cinema Table, "Cinema_Theatres" was added, in order to show the number of Theatres in each Cinema. This information was not available prior. **HOWEVER, this was later removed, as the sum of Theatres with "Cinema_ID=1" could be determined instead.**
- To the Screening Table, "Screening_Day" was added, in order to show what weekday the screening is on. Previously, only the date was available.
- In the Screening Table, "Screening_DateTime"'s datatype was changed from DateTime to SmallDateTime. Accuracy to 0.003 seconds is not required.
- In the Film Table, "Film_Duration" was changed to a single INT of the runtime in minutes - "Film_Duration_Mins", rather than TIME.
- Otherwise, all required data for the queries should already be accounted for within the data tables.

### The Changes to the database as a result are displayed below using an ERD;

Old: <br>
![20220856-ERD-2022-12-06_03-22](https://user-images.githubusercontent.com/110361869/211560321-9e271ef2-72c6-4bf6-b910-6a20690c286d.png)

New: <br>
![20220856-ERD-2023-01-10_19-59](https://user-images.githubusercontent.com/110361869/211560420-7b2a9882-3258-4c8b-8919-4bc9105d7523.png)

---

## Task 3: Preparing Data Content for Eye Candy Cinemas

In the absence of any real data available, content for the above tables must be fabricated from scratch. Data will, however, be somewhat correlated to existing competitors of Eye Candy Cinemas.

[The sample data content for Eye Candy Cinemas can be found here](./datacontent.md)

---

## Part 2, Task 1: Database Implimentation

The Database for Eye Candy Cinemas has successfully been created in MySQL, and [can be found here](https://github.com/20220856/RR-20220856.github.io/raw/main/Information-Systems/Assignments/Application/Eye-Candy-Cinema-Database.rar).

## Part 2, Task 2: Creation and Testing of Queries

In order to fulfil the conditions outlined by Eye Candy Cinemas, a number of queries must be created and tested to ensure correct functionality of the future Web Application. At least TWO queries must be created per requested function.

### F1: Search For Cinema

Q1: SearchCinemaByCity

BEGIN <br>
SELECT *  <br>
FROM cinema <br>
WHERE cinema_city="Auckland"; <br>
END <br>

This query takes one variable input from the user - the name of a city. In this specific case, "Auckland" or "Wellington" will return information corresponding to the Cinema complex in that city, and any other entry will return null.

Q2: SearchTheatreBySeatingAndCity

BEGIN <br>
SELECT * <br>
FROM theatre <br>
WHERE cinema_id=1 AND theatre_seats<100; <br>
END <br>

This Query takes TWO variable inputs from the user, a "1" or a "2" *(corresponding to either "Auckland" or "Wellington" respectively)*, and an algebraeic expression for the number of seats within a theatre *(In this case, less than 100)*. This will return how many THEATRES within a cinema *(specified within "Auckland" or "Wellington")* have the requested number of seats. If either of the values are invalid, null is returned.

### F2: Show Cinema Information

Q3: ShowTheatreIDAndSeats

BEGIN <br>
SELECT  theatre_id, theatre_seats<br>
FROM theatre; <br>
END <br>

This query does not take variable inputs from a user. Its purpose for the web application is to provide a collation of the number of seats correspondant to each theatre within BOTH cinema complexes, for ease of selection for the end-user. Also, because of this, there is no chance of a null value return - as there is no input in the first place.

Q4: SearchTheatreBySoundSystem

BEGIN <br>
SELECT theatre_id, sound_id <br>
FROM theatre <br>
WHERE sound_id=3; <br>
END <br>

This Query takes one variable input from a user - the numberic "Sound_ID", corresponding to a sound system within a theatre *(in this case, "3" - or Dolby Atmos)*. The query will then return a list of all theatres that have the corresponding sound system installed. A value of anything other than *("1", "2", or "3")* will result in a return of null.

### F3: Search Film Schedule

Q5: SearchFilmByTicketPrice

BEGIN <br>
SELECT * <br>
FROM screening <br>
WHERE screening_price LIKE 10.00; <br>
END <br>

This Query takes one variable input - the cost in dollars of a ticket *(in this case, "10.00", the cheapest)*, and displays a list of all film screenings corresponding to that price. It could also be used with an arithmetic expression, such as *("screening_price<13.00")*. Any inputs not corresponding to a decimal input will be met with null output.

Q6: SearchFilmByDay

BEGIN <br>
SELECT * <br>
FROM screening <br>
WHERE screening_day LIKE "Friday"; <br>
END <br>

This Query takes one variable input - a weekday *(in this case, "Friday")*, and compiles a list of films screening on that day. Any non-weekday inputs will return null.

### F4: Show Film Screenings

Q7: SearchScreeningByCinema

BEGIN <br>
SELECT * <br>
FROM screening <br>
WHERE theatre_id=1; <br>
END <br>

This query returns all Screenings scheduled to take place in a specified Cinema complex. In this case, within the Auckland Complex. Any input other than *("1" or "2")* will result in null output.

Q8: ShowScreeningInfo

BEGIN
SELECT *
FROM screening;
END

This query has no variable inputs, and serves to provide a list of all screenings currently available. Due to this, there is no chance of a null output.

### F5: Monitor Movie Screenings

Q9: AverageScreeningsPerWeek

Full disclosure, I could not get this to work. However, I imagine it was somewhat along the lines of this;

BEGIN
SELECT * NOT NULL
FROM screening AND COUNT(screening_id)/7;
END

I know this is not right, but I could not figure out how to insert arithmetic expressions and allow MySQL to "Print" - if there is such an equivalence to be made.

Q10: ListCinemaScreenings

BEGIN
SELECT *
FROM screening
WHERE screening_datetime BETWEEN "2022-01-12 00:00:00" AND "2022-01-13 00:00:00";
END

This Query has two variable inputs, both of which are datetimes - it allows for all films in a cinema to be displayed when they fall between the two specified datetimes. Any inserted values other than datetimes will return a null output.

---

This concludes the Application of Information Systems to Business Brief for Eye Candy Cinemas.

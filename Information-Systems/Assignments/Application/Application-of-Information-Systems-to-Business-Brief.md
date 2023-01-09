# IT5015 - Application of Information Systems to Business Brief - 20220856

---

# Task 1: Development of Data Model for Eye Candy Cinemas

Using the conceptual design of the Report provided to Eye Candy Cinemas, a final Entity Relationship Diagram has been created. It includes all relevant data of each cinema complex, individual theatres, sound systems within, screening times of films, and data on the films themselves.

![205660295-12cd7497-8352-4460-8463-f954e49cdc26](https://user-images.githubusercontent.com/110361869/211253075-1300e4ef-733e-4029-9cbf-91d691eee578.png)



Additionally, a breakdown of the ERD, as well as individual elements can be found below for additional context as to how the ERD directly corresponds to Eye Candy Cinemas. These breakdowns include all Entities used in the ERD, the Attributes of individual Entities, a brief Description of Attributes, the Data Types of Attributes, the Primary Key of the Entity (as well as other Candidate Keys), and the Cardinality of each dataset to another.

---

## Cinema Dataset

|Entity|Attribute|Description|Data Type|PK/CK/FK|Cardinality|
|:---:|---|---|---|---|:---:|
|Cinema|Cinema_ID|A Numeric Identifier for the Cinema|INT|PK & CK|Theatre *(One-to-Many)*|
||Cinema_Name|The Name of the Cinema *(AKL or WLG)*|VARCHAR|CK||
||Cinema_Address_1|The first line of Address for the Cinema|VARCHAR|||
||Cinema_Address_2|The Suburb of the Cinema|VARCHAR|||
||Cinema_City|The City of the Cinema|VARCHAR|||
||Cinema_Email|The Email address of the Cinema|VARCHAR|||
||Cinema_Phone|The Phone Number of the Cinema|INT|||

For the Cinema Dataset, no referential constraints apply, as the contained information is entirely independant of other datasets.

---

## Theatre Dataset

|Entity|Attribute|Description|Data Type|PK/CK/FK|Cardinality|
|:---:|---|---|---|---|:---:|
|Theatre|Theatre_ID|A Numeric Identifier for a Theatre|INT|PK, CK and FK|Screening *(One-to-Many)*|
||Theatre_Seats|The capacity of all seats within the Theatre|INT|||
||Cinema_ID|The Cinema ID, denoting which cinema the theatre is located|INT|FK|Cinema *(Many-to-One)*|
||Sound_ID|The Sound System ID, denoting which system the theatre uses|INT|FK|Sound System *(Many-to-One)*|

For the Theatre Dataset, both the Cinema_ID and Sound_ID attributes are referential constraints - the information from both the Cinema Dataset and the SoundSystem Dataset are being referenced. This is because the theatre could not otherwise:
- Be located within a Cinema Complex.
- Have the Sound System in use be determined.

---

## Screening Dataset

|Entity|Attribute|Description|Data Type|PK/CK/FK|Cardinality|
|:---:|---|---|---|---|:---:|
|Screening|Screening_ID|The Numeric Identifier for a Screening|INT|PK & CK||
||Theatre_ID|The Theatre ID, denoting the theatre for the screening|INT|FK|Theatre *(Many-to-One)*|
||Film_ID|The Film ID, denoting the film for the screening|INT|FK|Film *(Many-to-One)*|
||Screening_DateTime|The Date and time of the screening|DATETIME|||
||Screening_Price|The Price for a ticket to the screening|DECIMAL|||

For the Screening Dataset, both the Theatre_ID and Film_ID attributes are referential constraints - information from the Theatre Dataset and Film Dataset are being referenced. This is important, otherwise:
- The Theatre within which the Screening was set to take place could not be determined.
- The Film that the Screening was intended to display could not be determined.

---

## Film Dataset

|Entity|Attribute|Description|Data Type|PK/CK/FK|Cardinality|
|:---:|---|---|---|---|:---:|
|Film|Film_ID|The Numeric Identifier for a Film|INT|PK, CK & FK|Screening *(One-to-Many)*|
||Film_Title|The Title of the film|VARCHAR|CK||
||Film_Director|The Director of the Film|VARCHAR|||
||Film_Duration|The complete runtime of the Film|TIME|||
||Film_Year|The Year the film was released|INT|||
||Film_Classification|The Classification of the film|VARCHAR|||
||Film_IMDB|A link to the IMDB Rating/Review of the Film|VARCHAR|||

For the Film Dataset, there are no referential constraints. The information regarding a film is not dependant on any other Data - it is fixed.

---

## SoundSystem Dataset

|Entity|Attribute|Description|Data Type|PK/CK/FK|Cardinality|
|:---:|---|---|---|---|:---:|
|Sound System|Sound_ID|The Numeric Identifier for a Sound System|INT|PK, CK & FK|Theatre *(One-to-Many)*|
||Sound_Name|The Model Name of the Sound System|VARCHAR|||
||Sound_Manufacturer|The Manufacturer of the Sound System|VARCHAR|||

For the SoundSystem Dataset, there are no referential constraints. The Dataset is not dependant on any information in order to exist, and - in fact - only exists for referencing in the Theatre Dataset.

---


1st normal form = good database design
2nd normal form = no partial dependancy (ie. all data should only be represented once)
3rd normal form = no transitive dependancy (ie. no data dependance of non-primary keys)


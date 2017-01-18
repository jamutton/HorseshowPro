# Horseshow Pro

HorseshowPro is an web-app tool for managing 4H Horse Shows.  I grew up with horses and rode in 4H and the show process remains mostly archaic to this day.  Since my sister and parents are still involved and manage the process, this project was started to help bring some technology to help them.

## Goals
The following goals were set for the current version:

* Provide a streamlined way to handle multiple shows, riders, entries and results, import, workflow... that kind of crap.
* Reduce paperwork by doing much of the data-entry in an app as opposed to using paper at the show. (removed for class-judging. Show Judges are prima donna's and refuse such optimizations as reducing waste)
* Improve the output of the show by providing comments and historical data to riders, helping them to improve. (removed, Judges wont enter comments electronically and it's too difficult to find volunteers that can read their glyphs)
* Streamline the show process by automating the required reporting for the various show awards.  Eliminate common human errors. (removed, until such time as judges can be found that know what a smartphone is)
* Provide for alternate input methods during the show (tablet).
* Keep long term records, because parents lie.

## Future/Todo
There are many ways this could be further improved:

* Move to a better database backend and/or revamp the sql to be less nasty (not as much of a problem when we're not doing complex reports)
* Help with fees, budgeting and journal entry (still a largely manual process)

A lot of reporting functionality was removed from this version just to streamline the github commit and maintenance/migration to a modern django version. The problem is that while show judges insist on using paper, there needs to be a translation layer to make it electronic.  All that is really needed is to gather the current placings and danishes for each class but, with all the volunteers typically needed to make a Horseshow operate, this is impractical.  We must, therefore, do without lots of other automation that could be used.  If judgings are saved electronically, the following features could be restored:
* Automatic qualifications reporting
* Automatic medals scoring/tracking
* Automatic highpoint scoring
* Web-based (or external display) Highpoint leaderboard
* year/year comparasion reports

#

## Troubleshooting
* read the code...
* make sure you follow the setup instructions

## Contact
* Don't... I really only do this for the benefit of my sister.  Maybe someday I'll make it so the sql doesn't suck and do something about the drunken JS but it is not this day.  If you can get my sister to ask me then maybe...

# Importing data
Typically, after setup, there will be two stages of data import, initial bootstrapping followed by operational entry.  For bootstrapping, the loaddata SQL command script is used after Django sets up its database.  Ongoing operational entry can be either via the Django administrator or in bulk, through CSV.

## Database
cd data
sqlite show.db
sqlite> .read loaddata

## Input CSV
Typically, horse show entries have been mailed and/or phoned in but by using Google forms or some other means of online entry, the process can be streamlined. Whatever service used, the output must be exportable to CSV.  We define the following fields in the import (enum-options are based on related tables)
* RidersName (first last)
* RidersNumber
* HorsesName
* ContactEmail
* ContactPhone
* AgeDivision (_enum_)
  * Junior
  * Intermediate
  * Senior
* RidingDivision (_enum_)
  * novice
  * greenhorse
  * regular
* Club (_enum from club primary keys_)
  * Barn Buddies
  * Classic Riders
  * Evergreen Equestrians
  * Golden Horseshoes
  * Happy Hayburners
  * Lucky Horseshoes
  * Mounted Mischief
  * Mt Si Riderz
  * Vashon Rock Riders
  * Thunder Rail
  * other... (how does this get captured)
* Volunteer Jobs (_should these be captured to some kind of text field associated with the rider?_)
  * Showmanship and Western ingate, Ring steward, scribe, Announcer
  * Trail and Driving - in gate, scribe, set up/take down, trail manager, ring steward
  * Bareback and English classes- in gate, announcer, scribe, ring steward, pooper scooper and trash pickup
  * Over Fences/Dressage - In gate, scribe, warm up arena attendant, pole setter, pooper scooper and trash pickup, ribbon table, set up/take down
  * OTHER:
* Performance Classes:
  * showmanship
  * Saddle Seat eq
  * Hunt seat/english eq
  * Discipline Rail english
  * Bareback Eq
  * Discipline Rail Western
  * Stock seat eq
  * trail
* Performance Medals:
  * showmanship
  * Hunt Seat
  * Saddle Seat
  * Stock Seat
  * Trail
* Electronic Signature of Parent/Guardian : __BOOL__
* Name of Parent/Guardian : __STRING__
* Electronic Signature of Rider : __BOOL__
* Name of rider agreeing to statement : __STRING__



CSV:
0-Timestamp,
1-Riders name,
2-Riders number,
3-Horses name,
4-Contact Email,
5-Contact Phone Number,
6-Age division,
7-Riding Division,
8-Club,
9-Volunteer jobs: Where I would like to help out,
10-Performance classes,
11-Performance Medals [Showmanship],
12-Performance Medals [Hunt Seat],
13-Performance Medals [Saddle Seat],
14-Performance Medals [Stock Seat],
15-Performance Medals [Trail],
16-Electronic Signature of Parent or Guardian,
17-Name of Parent or Guardian responsible for rider at event,
18-Electronic Signature of Rider,
19-Name of rider agreeing to statement

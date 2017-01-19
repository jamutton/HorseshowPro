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

* Add backup/restore functionality.
* Move to a better database backend and/or revamp the sql to be less nasty (not as much of a problem when we're not doing complex reports)
* Help with fees, budgeting and journal entry (still a largely manual process)

A lot of reporting functionality was removed from this version just to streamline the github commit and maintenance/migration to a modern django version. The problem is that while show judges insist on using paper, there needs to be a translation layer to make it electronic.  All that is really needed is to gather the current placings and danishes for each class but, with all the volunteers typically needed to make a Horseshow operate, this is impractical.  We must, therefore, do without lots of other automation that could be used.  If judgings are saved electronically, the following features could be restored:
* Automatic qualifications reporting
* Automatic medals scoring/tracking
* Automatic highpoint scoring
* Web-based (or external display) Highpoint leaderboard
* year/year comparasion reports

# Setup
## Prerequisites
* git (or download a zip of the release)
* Python 2.7 (with django 1.10+ and dependencies)
* sqlite3 libraries/tools for your platform
* memcached installed and running on the default port on localhost

First you need to setup the code
* clone the repo
* cd to the repo directory
* this will create the database in the "data" directory
  * python manage.py migrate
  * python manage.py makemigrations horse_show
  * python manage.py migrate

Next you need to create a superuser.  This is the initial user that has access to everything so choose a password appropriately and all that stuff.  To create a user, you'll use python-Django's tools for populating the database with an initial model.  Enter the following into the command window:
~~~~
python manage.py createsuperuser
Username (leave blank to use 'yourusername'): admin
Email address: admin@example.com
Password:
Password (again):
Superuser created successfully.
~~~~

Now you need to prepopulate the database with some standard settings/model-data. You could do this from the administrator but these are very common designations that we can pre-feed in to save time in the admin.  You'll use the sqlite3 tools for submitting this:
~~~~
sqlite3 show.db
sqlite> .read loaddata
~~~~

Lastly, you need to start the python-Django server.  To do that type `python manage.py runserver` into your command prompt. If you want to access it over a wireless network or from a tablet, use this instead `python manage.py runserver 0.0.0.0:8000` and it will listen on all interfaces.

# Running
Once you've completed the setup and have memcache and python running.  Point your browser to: `http://localhost:8000/HSPro/`.  If all has worked properly, you should see Horseshow Pro's opening page.  You'll need to start by logging in with your newly created user and creating a show and classes.

## Printing class lists and Welcome sheets
From the main page, you can hit the `Actions` menu and `Select Show` to choose from the available shows.  Once in a show, the class list is shown with a search box.  From there you can filter the class list to grab the specific class you're after and print class lists.  You can also print *Rider Welcome Sheets* from the menu as well.  The welcome sheets give a rider the list of classes they're entered in along with some note space and the qualification-potential of the class.  At this point, if you've just installed there will not be any shows to see data for so you'll need to setup your show first.

_**The following sections require you to login**_

## Creating a show
Click the `Admin Actions` menu and select `Show Administrator`.  This will take you to the main admin page.  Click the `+ Add` button for `Shows`.  Enter a show name, pick a date and set the enddate to the same day.  You'll also need a location but not having created one yet, you'll need to click on the plus icon next to the location drop-down.  This will popup a window for adding a location and then return when you click `Save`.  You can finish by hitting the Show-page's `Save` button.  You can then use the breadcrumb navigation near the top-left of the page to get back to the Administration `Home`.

### Adding Classes
Next up, you'll need to add some classes to your show.  Click on the `+ Add` button for `Classes` from the Admin page.  Enter a few classes by minimally providing the `Name` and the `Seat`.  You can use the `Save and add another` button to streamline adding several classes quickly.   **If you intend on using the CSV import you will need to provide some optional fields so _listen carefully_.**

#### Designing your class names for CSV Import
If you use Google-forms or some other online data entry system to collect rider entries, the CSV must conform to a specific field assignment.  Moreover, after doing this a while, it's been found that if you give the entrant the ability to check boxes for all age divisions (like having a specific "Showmanship Sr" and "Showmanship Jr") they will invariably check the wrong ones.  It is therefore recommended (*actually, it's required*) that you only provide the non-age division entry checkboxes and also collect the rider's age division separately in whatever online form you use.  The CSV import will match on the classname against the `Text to match with entry form` from your class entry along with the value of the `Division` field.  These must be filled in then if you wish to use CSV import.  More specifics on CSV import later.

### Scheduling Classes
With classes created, you must now schedule them in the show.  From the Admin Page, press the `+ Add` next to the `Class Schedules` item.  From this page you can start to add/order classes for a show.  Select the class/seat/division from the first drop-down, map it to the appropriate show and enter in a numeric `ShowPosition`.  The `ShowPosition` will be used for ordering your class lists in the show display.  You can also optionally add a non-numeric `ClassNumber` which will be used in welcome sheets (if for example you want to do a 1A, 1B and 1C or something like that).

## Adding RidersName
Once the entries start flowing, you can use the CSV import (if your data is emitted properly), or you can enter riders manually.  If a rider is not in the system you'll have to add them before taking any class entries.  To add a rider click the `+ Add` button next to `Riders` on the Admin page.  Fill in all the rider information, including the hidden fields.

### Entering a rider in a class
With riders on-board, it's time to enter them into a class.  Click the `+ Add` next to the `Entries` item from back on the Admin page. This will take you to the rider entry form.  Select the rider's `Number` from the list, the `Show` from the list and each `ShowClass` they will be entered in.

**At this point, you've added everything you need to print class lists, welcome forms and run a show.  From here on out it's just more of the same.**

## Backing up your data
You should periodically copy the show.db file to a backup while the service is not running.  In the future it would be nice to have a backup tool in the app but it's not there now so brute force is required.

# Troubleshooting
* read the code...
* make sure you follow the setup instructions
* If you're getting an error in the console about the database, you may have a corrupt database.  Might have to work from a backup.

## Contact
* Don't... I really only do this for the benefit of my sister.  Maybe someday I'll make it so the sql doesn't suck and do something about the drunken JS but it is not this day.  If you can get my sister to ask me then maybe...

# Importing data
Typically, after setup, there will be two stages of data import, initial bootstrapping followed by operational entry.  For bootstrapping, the loaddata SQL command script is used after Django sets up its database as described in the Setup section.  Ongoing operational entry can be either via the Django administrator or in bulk, through CSV.

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

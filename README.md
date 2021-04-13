# Squirrel Tracking Web Application


<img src="https://www.pngarea.com/pngs/18/5415510_squirrel-png-ice-age-squirrel-hd-png-download.png" alt="Great Day" width="500" height="500">


<ul>
  <li> Tools For Analytics Final Project </li>
  <li> Group Name: Group41 </li>
  <li> Authors: Wenhao Yang, Endong Teng</li>
  <li> UNI: wy2378, et2697</li>
</ul>

## Description
<p>
It is a web application with five pages in total implemented by Django framework. The users would be able to add, update, and view the squirrel data.
</p>

## Details
<ul>
  <li> Management Commands </li>
    <p> Import the data from the 2018 census file could be realized using the following command

  ```sh
  python manage.py import_squirrel_data /path/to/file.csv
  ```

  Export: used to export the data in CSV format. The file path should be specified to the location of output destination.

   ```sh
  python manage.py export_squirrel_data /path/to/file.csv
   ```
   </p>
  <li> Web pages </li>
    <p>
  (1) Home page with 4 major links that linked to Sightings, Stats, Add, and Location Part.  

         Located at: /
    
  (2) A map page displays the recorded sightings with all marks. 

         Located at: /map

  (3) The squirrel sightings page allows the user to view the specific data and link to update the squirrel data.

         Located at: /sightings

  (4) This page allows users to edit specific squirrels data.

          Located at: /sightings/<unqiue-squirrel-id>

  (5) The add page under the sightings would allow users to create a new record. 

          Located at: /sightings/add

  (6) The page with overall statistics of the sightings

          Located at: /sightings/stats

 </p>
</ul>


## Server Link
<ul>
  <li> xxxxdsdsdsdsdx </li>

</ul>



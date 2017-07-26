# Canadian Nutrient File

## What?

This project allows you to import the [Canadian Nutrient File](https://www.canada.ca/en/health-canada/services/food-nutrition/healthy-eating/nutrient-data/canadian-nutrient-file-2015-download-files.html) into a Mongo database with very little effort. The models I built are pretty basic, they follow their data structure, with the hope that future releases will be as easy to import.

Just download the files somewhere, extract the zip file, and run the importer. Done.

The pdfs provided with the download will explain everything to you, so I won't really talk about the data itself here. They're better at it than I am, tbh.


## How?

### Latest stable / pip

    # Optional, use a virtualenv
    virtualenv .
    . bin/activate
    # Install us
    pip install canadian-nutrient-file
    # Run the importer, takes about 200 seconds on a recent computer
    CNF_MONGO_DB=mycnf cnf import --source=/path/to/data/dir [--batch=1000]
    # ^ See cnf/settings.py on github for more vars you can set
    # Run the demo flask app and open a browser
    CNF_MONGO_DB=mycnf cnf runserver
    open http://localhost:8888/

### Git version / buildout

    git clone https://github.com/cyrilrbt/canadian-nutrient-file.git
    cd canadian-nutrient-file
    # I use bootstrap because it's awesome! See buildout.org
    python3 bootstrap.py
    # Install all dependencies
    bin/buildout
    # Change settings if you feel like it. You can also set env vars.
    vim cnf/settings.py
    # Run the importer, takes about 200 seconds on a recent computer
    bin/cnf import --source=/path/to/data/dir [--batch=1000]
    # Run the demo flask app and open a browser
    bin/cnf runserver
    open http://localhost:8888/


from flask import current_app as app
# Just a shorthand
db = app.db


class CNFDocument(db.Document):
    meta = {
        'allow_inheritance': True,
        'abstract': True,
    }


class CNFFoodName(CNFDocument):
    meta = {
        'collection': 'cnf_food_name'
    }
    id = db.StringField(primary_key=True)
    code = db.StringField()
    food_group = db.ReferenceField('CNFFoodGroup')
    food_source = db.ReferenceField('CNFFoodSource')
    description = db.StringField()
    description_f = db.StringField()
    date_of_entry = db.DateTimeField()
    date_of_publication = db.DateTimeField()
    country_code = db.StringField()
    scientific_name = db.StringField()


class CNFFoodGroup(CNFDocument):
    meta = {
        'collection': 'cnf_food_group'
    }
    id = db.StringField(primary_key=True)
    code = db.StringField()
    name = db.StringField()
    name_f = db.StringField()


class CNFFoodSource(CNFDocument):
    meta = {
        'collection': 'cnf_food_source'
    }
    id = db.StringField(primary_key=True)
    code = db.StringField()
    description = db.StringField()
    description_f = db.StringField()


class CNFNutrientAmount(CNFDocument):
    meta = {
        'collection': 'cnf_nutrient_amount'
    }
    food = db.ReferenceField('CNFFoodName')
    nutrient_name = db.ReferenceField('CNFNutrientName')
    nutrient_source = db.ReferenceField('CNFNutrientSource')
    nutrient_value = db.DecimalField()
    standard_error = db.StringField()
    number_of_observations = db.IntField()
    date_of_entry = db.DateTimeField()


class CNFNutrientName(CNFDocument):
    meta = {
        'collection': 'cnf_nutrient_name'
    }
    id = db.StringField(primary_key=True)
    nutrient_code = db.StringField()
    nutrient_symbol = db.StringField()
    unit = db.StringField()
    name = db.StringField()
    name_f = db.StringField()
    tagname = db.StringField()
    nutrient_decimals = db.StringField()


class CNFNutrientSource(CNFDocument):
    meta = {
        'collection': 'cnf_nutrient_source'
    }
    id = db.StringField(primary_key=True)
    code = db.StringField()
    description = db.StringField()
    description_f = db.StringField()


class CNFConversionFactor(CNFDocument):
    meta = {
        'collection': 'cnf_conversion_factor'
    }
    food = db.ReferenceField('CNFFoodName')
    measure = db.ReferenceField('CNFMeasureName')
    value = db.StringField()
    date_of_entry = db.DateTimeField()


class CNFMeasureName(CNFDocument):
    meta = {
        'collection': 'cnf_measure_name'
    }
    id = db.StringField(primary_key=True)
    name = db.StringField()
    name_f = db.StringField()


class CNFYieldAmount(CNFDocument):
    meta = {
        'collection': 'cnf_yield_amount'
    }
    food = db.ReferenceField('CNFFoodName')
    yield_name = db.ReferenceField('CNFYieldName')
    amount = db.StringField()
    date_of_entry = db.DateTimeField()


class CNFYieldName(CNFDocument):
    meta = {
        'collection': 'cnf_yield_name'
    }
    id = db.StringField(primary_key=True)
    name = db.StringField()
    name_f = db.StringField()


class CNFRefuseAmount(CNFDocument):
    meta = {
        'collection': 'cnf_refuse_amount'
    }
    food = db.ReferenceField('CNFFoodName')
    refuse_name = db.ReferenceField('CNFRefuseName')
    amount = db.StringField()
    date_of_entry = db.DateTimeField()


class CNFRefuseName(CNFDocument):
    meta = {
        'collection': 'cnf_refuse_name'
    }
    id = db.StringField(primary_key=True)
    name = db.StringField()
    name_f = db.StringField()
